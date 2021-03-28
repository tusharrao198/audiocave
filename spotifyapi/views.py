from django.shortcuts import render, redirect
from decouple import config
# from rest_framework.views import APIView
# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from spotifyapi.models import Spotifytoken, Votecount
from .utils import update_or_create_user_tokens, check_spotify_athenticated, execute_SpotifyAPIrequest
from music_room.models import Room
import requests
# print(f'\n\nconfig = {config("CLIENT_ID")}\n\n')

@api_view(["GET"])
def AuthURL(request):
    scopes = ["user-read-playback-state", 'user-modify-playback-state', 'user-read-currently-playing','streaming', 'user-read-email', 'user-read-private']
    url = Request('GET', "https://accounts.spotify.com/authorize", params={
        'scope': scopes,
        'response_type': 'code',
        'client_id': config("CLIENT_ID"),
        'redirect_uri': config("REDIRECT_URI"),
    }).prepare().url
    # print(F"GET url ={url} ")
    return Response({"url":url}, status=status.HTTP_200_OK)

# spotify_callback
def Spotify_Callback(request, format=None):
    print("Spotify_Callback called")
    code = request.GET.get('code')
    error  = request.GET.get("error")
    # print(f"spotify_callback code ={code} ")
    # print(f"Checking redirect uri= {config('REDIRECT_URI')}")
    # sending request to get access_token
    response = post('https://accounts.spotify.com/api/token', data={
     'grant_type':"authorization_code",
     "code" : code,
     'redirect_uri': config("REDIRECT_URI"),
     'client_id': config("CLIENT_ID"),
     'client_secret': config("CLIENT_SECRET"),
    }).json()

    access_token = response.get("access_token")
    refresh_token = response.get("refresh_token")
    token_type = response.get("token_type")
    expires_in = response.get("expires_in")
    error = response.get("error")
    # print(f'access_token = {response.get("access_token")}\n')
    # print(f'refresh_token={response.get("refresh_token")}\n')
    # print(f'token_type ={response.get("token_type")}\n')
    # print(f'expires_in ={response.get("expires_in")}\n')
    if not request.session.exists(request.session.session_key):
        # print("# if not then we create")
        request.session.create()
    update_or_create_user_tokens(request.session.session_key, access_token, token_type, expires_in, refresh_token)

    print("DJANGO redirect feature worked")
    return redirect('http://127.0.0.1:8000/homepage/')  # fo redirecting to a different app in django
    # return redirect('http://localhost:3000/homepage')


@api_view(["GET"])
def is_Authenticated(request):
    # print("isAuthenticated Called")
    is_authenticated = check_spotify_athenticated(request.session.session_key)
    return Response({"Status":is_authenticated} , status=status.HTTP_200_OK)


@api_view(["GET"])
def getCurrentSong(request):
    roomCode = request.session.get('Room_code')
    room = Room.objects.filter(code=roomCode)
    if room.exists():
        room=room[0]
    else:
        return Response({"BAD REQUEST": "ROOM NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)

    hostid = room.host
    endpoint = 'player/currently-playing'
    # if room.host == request.session.session_key:   # when host is accessing
    #     # print("# when host is accessing getCurrentSong")
    #     # response = execute_SpotifyAPIrequest(hostid, endpoint)
    #     response = execute_SpotifyAPIrequest(hostid, endpoint)
    #     if 'error' in response or 'item' not in response:
    #         return Response({"No Content": "Nothing Is playing"}, status=status.HTTP_204_NO_CONTENT)
    # else:
    #     # print("ACCESSED BY USER OF THE ROOM NOT THE HOST")
    device_id = execute_SpotifyAPIrequest(hostid)['id']
    try:
        response = execute_SpotifyAPIrequest(hostid, endpoint)
        item = response['item']
        votes = Votecount.objects.filter(room=room, song_id=item['id'])
        song_info = {
            "device_id": device_id,
            "artist_name": item['album']['artists'][0]['name'],
            "artist_uri": item['album']['artists'][0]['uri'],
            "image_url": item['album']["images"][0]['url'],
            "progress": response['progress_ms'],
            "duration": item["duration_ms"],
            "song_uri": item['uri'],
            "song_id":item['id'],
            "song_name": item['name'],
            "type": item['type'],
            "is_playing": response['is_playing'],
            "vote": len(votes),
            "votes_required": room.votes_count_to_skip,
        }
        if room.current_song != song_info['song_id']:
            room.current_song = song_info['song_id']
            room.save(update_fields=["current_song"])
            votes = Votecount.objects.filter(room=room.code).delete()

        # print(f"\n\n\nsong_info={song_info}\n\n\n")
        return Response(song_info, status=status.HTTP_200_OK)
    except:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

def play_Song(session_key):
    # print("playsong called",session_key)
    endpoint = "player/play"
    return execute_SpotifyAPIrequest(session_key, endpoint , put_=True)

def pause_Song(session_key):
    # print("pause song called",session_key)
    endpoint = "player/pause"
    return execute_SpotifyAPIrequest(session_key, endpoint , put_=True)

def skip_Song(session_key):
    # print("skip song called",session_key)
    endpoint = "player/next"
    return execute_SpotifyAPIrequest(session_key, endpoint , post_=True)

@api_view(["PUT"])
def pauseSong(request):
    roomCode = request.session.get('Room_code')
    room = Room.objects.filter(code=roomCode)[0]
    if request.session.session_key == room.host or room.guest_can_pause:
        pause_Song(room.host)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    return Response({}, status=status.HTTP_403_FORBIDDEN)

@api_view(["PUT"])
def playSong(request):
    roomCode = request.session.get('Room_code')
    room = Room.objects.filter(code=roomCode)[0]
    if request.session.session_key == room.host or room.guest_can_pause:
        play_Song(room.host)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    return Response({}, status=status.HTTP_403_FORBIDDEN)

@api_view(["POST"])
def skipSong(request):
    roomCode = request.session.get('Room_code')
    room = Room.objects.filter(code=roomCode)
    if room.exists():
        room=room[0]
        votes = Votecount.objects.filter(room=room, song_id=room.current_song)
        votes_needed = room.votes_count_to_skip
        if request.session.session_key == room.host or len(votes) +1 >= votes_needed:
            votes.delete()
            skip_Song(room.host)
        else:
            vote = Votecount(
                user_id = request.session.session_key,
                room=room, song_id=room.current_song
            )
            vote.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)























# class AuthURL(API_View):
#     def get(self, request, format=None):
#         scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
#         url = Request('GET', "https://accounts.spotify.com/authorize", params={
#             'scope': scopes,
#             'response_type': 'code',
#             'client_id': config("CLIENT_ID"),
#             'redirect_uri': config("REDIRECT_URI"),
#         }).prepare().url
#
#         return Response({"url":url}, status=status.HTTP_200_OK)
