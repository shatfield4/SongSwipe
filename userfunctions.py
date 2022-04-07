from flask import redirect
import spotipy
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv
import os

# Load env variables
load_dotenv(find_dotenv())

# Env Variables
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT_URI")

# Intialize spotipy instance
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

pp = pprint.PrettyPrinter(indent=2)

def getArtist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def getArtistGenres(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]['genres']
    else:
        return None

artist_name = input("Input artist name: ")

pp.pprint(getArtist(artist_name))
print("\n")
pp.pprint(getArtistGenres(artist_name))

print(sp.recommendation_genre_seeds())