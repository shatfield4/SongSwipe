import base64, json, requests, os

SPOTIFY_URL_AUTH = 'https://accounts.spotify.com/authorize/?'
SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token/'
RESPONSE_TYPE = 'code'   
HEADER = 'application/x-www-form-urlencoded'
REFRESH_TOKEN = ''
    
def getUser(CLIENT_ID, REDIRECT_URI, PORT):
    scope = "streaming user-read-email user-read-private user-library-read user-library-modify user-read-playback-state user-modify-playback-state"

    redirect_uri = "{}:{}/callback/".format(REDIRECT_URI, PORT)

    data = "{}client_id={}&response_type=code&redirect_uri={}&scope={}".format(SPOTIFY_URL_AUTH, CLIENT_ID, redirect_uri, scope) 
    return data