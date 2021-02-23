from django.shortcuts import render, redirect
from decouple import config
# from rest_framework.views import APIView
# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from spotifyapi.models import Spotifytoken
from .utils import update_or_create_user_tokens, check_spotify_athenticated, execute_SpotifyAPIrequest
from music_room.models import Room
import requests
# print(f'\n\nconfig = {config("CLIENT_ID")}\n\n')

@api_view(["GET"])
def AuthURL(request):
    scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
    url = Request('GET', "https://accounts.spotify.com/authorize", params={
        'scope': scopes,
        'response_type': 'code',
        'client_id': config("CLIENT_ID"),
        'redirect_uri': config("REDIRECT_URI"),
    }).prepare().url
    print(F"GET url ={url} ")
    return Response({"url":url}, status=status.HTTP_200_OK)

# spotify_callback
def Spotify_Callback(request, format=None):
    print("Spotify_Callback called")
    code = request.GET.get('code')
    error  = request.GET.get("error")
    print(f"spotify_callback code ={code} ")
    print(f"Checking redirect uri= {config('REDIRECT_URI')}")
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
        print("# if not then we create")
        request.session.create()
    update_or_create_user_tokens(request.session.session_key, access_token, token_type, expires_in, refresh_token)

    print("DJANGO redirect feature worked")
    return redirect('http://127.0.0.1:8000/homepage/')  # fo redirecting to a different app in django
    # return redirect('http://localhost:3000/homepage')


@api_view(["GET"])
def is_Authenticated(request):
    print("isAuthenticated Called")
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
    if room.host == request.session.session_key:   # when host is accessing
        print("# when host is accessing getCurrentSong")
        response = execute_SpotifyAPIrequest(hostid, endpoint)
        if 'error' in response or 'item' not in response:
            return Response({"No Content": "Nothing Is playing"}, status=status.HTTP_204_NO_CONTENT)
    else:
        print("ACCESSED BY USER OF THE ROOM NOT THE HOST")
        response = execute_SpotifyAPIrequest(hostid, endpoint)

    item = response['item']
    song_info = {
        "artist_name": item['album']['artists'][0]['name'],
        "artist_uri": item['album']['artists'][0]['uri'],
        "images": item['album']["images"][-1],
        "song_uri": item['album']['uri'],
        "song_name": item['album']['name'],
        "type": item['type'],
        "is_playing": response['is_playing'],
        "pause": response['actions']['disallows']['pausing'],
    }
    print(f"\n\n\nsong_info={song_info}\n\n\n")
    return Response(song_info, status=status.HTTP_200_OK)


























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
