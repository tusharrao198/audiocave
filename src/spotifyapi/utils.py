from spotifyapi.models import Spotifytoken
from datetime import datetime, timedelta
from decouple import config
import requests
from requests import Request, post
# from django.utils import timezone

BASE_URL = "https://api.spotify.com/v1/me/"

# getting the spotify credentials
def get_user_token(session_key):
    # print("REFRESHING called = ", session_key)
    user_tokens = Spotifytoken.objects.all().filter(user_id=session_key)
    # # user_tokens= Spotifytoken.objects.get(user_id=session_key)
    # print("USER_TOKENS", user_tokens, "\n or ", Spotifytoken.objects.filter(user_id=session_key).user_id)
    if user_tokens:
        # print(f"getting user token with session_key={session_key} and saved data = {user_tokens[0].refresh_token}")
        return user_tokens[0]
        # return user_tokens
    else:
        return None

# updating and storing the credentials
def update_or_create_user_tokens(session_key, access_token, token_type, expires_in, refresh_token):
    tokens = get_user_token(session_key)
    if expires_in is None:
        expires_in = 3600
        # print(f"type = {type(expires_in)} and expires_in={expires_in}")
        expires_in = str(datetime.now() + timedelta(seconds=expires_in))

    else:
        # print("expires_in return as not None")
        expires_in = str(datetime.now() + timedelta(seconds=expires_in))
    if tokens:
        doit = Spotifytoken.objects.filter(user_id=session_key).update(
            user_id = session_key,
            access_token = access_token,
            refresh_token = refresh_token,
            token_type = token_type,
            expires_in = expires_in,
        )
    else:
        doit = Spotifytoken(
            user_id = session_key,
            access_token = access_token,
            refresh_token = refresh_token,
            expires_in = expires_in,
            token_type = token_type,
        )
        doit.save()

def refresh_spotify_token(tokens):
    # data = get_user_token(session_key)
    # user_tokens = Spotifytoken.objects.all().filter(user_id=session_key)
    # data = user_tokens[0]
    # print("REFRESHING CALLED DATA",data)
    refresh_token = tokens.refresh_token
    # print("\n\nrefresh_token form model = ", refresh_token,"\n\n access_token =",tokens.access_token)
    response = requests.post('https://accounts.spotify.com/api/token', data={
        'grant_type': "refresh_token",
        # 'Authorization': 'Basic',
        'Content-Type': 'application/x-www-form-urlencoded',
        'refresh_token': tokens.refresh_token,
        'client_id': config("CLIENT_ID"),
        'client_secret': config("CLIENT_SECRET"),
    }).json()
    # print(f"\n\nResponse returned = {response}\n\n")
    session_key = tokens.user_id
    access_token = response.get("access_token")
    # refresh_token = response.get("refresh_token")
    token_type = response.get("token_type")
    expires_in = response.get("expires_in")
    # print(f'\n\naccess_token = {access_token}\n')
    # print(f'refresh_token={refresh_token}\n')
    # print(f'token_type ={token_type}\n')
    # print(f'expires_in ={expires_in}\n')
    if refresh_token is not None:
        update_or_create_user_tokens(session_key, access_token, token_type, expires_in, refresh_token)
    else:
        return {"Error": "Token not Refreshed"}

def check_spotify_athenticated(session_key):
    # print(f"check_spotify_athenticated called session_key = {session_key}")
    tokens = get_user_token(session_key)
    if tokens:
        check_expiry = datetime.strptime(tokens.expires_in, '%Y-%m-%d %H:%M:%S.%f')
        # print(f"Present time = {datetime.now()} and check_expiry = { check_expiry} and seconds left = {check_expiry - datetime.now()}")
        if check_expiry <= datetime.now():
            print(f"Token expired ,  Refreshing token")
            refresh_spotify_token(tokens)
        else:
            print(f"Token not yet expired, User is Authenticated")
        return True
    return False

def execute_SpotifyAPIrequest(session_key, endpoint=False, put_=False, post_=False):
    tokens = get_user_token(session_key)
    # print(f"\n\nAccess token = {tokens.access_token } \n\n")
    spotify_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {tokens.access_token}",
    }
    # print(f"\n\nSpotify headers = {spotify_headers}\n\n")
    if post_:
        data = requests.post(BASE_URL + endpoint, headers=spotify_headers)
        print("POSTING DATA", data)

    if put_:
        spotify_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {tokens.access_token}",
        }
        # print(f"Sending Put request = {BASE_URL+endpoint}{spotify_headers}")
        # requests.put(BASE_URL+endpoint, headers=spotify_headers)
        Request('PUT', BASE_URL+endpoint , {},  params=spotify_headers).prepare().url
        # print("\n\nPUTTING DATA", data)
    if endpoint==False:
        response_spotify = requests.get(BASE_URL, {}, headers=spotify_headers)
    try:
        response_spotify = requests.get(BASE_URL+endpoint,{}, headers=spotify_headers)
    except:
        pass
    # print("responsespotify JSON", response_spotify)
    try:
        # print("SUCCESS CONNECTED SPOTIFY")
        return response_spotify.json()
    except:
        return {"error": "Error Connection request"}
