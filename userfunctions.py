from flask import redirect
import spotipy
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
from sqlite_test import Sqlite_test
import json

# Load env variables
load_dotenv(find_dotenv())

# Env Variables
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT_URI")

# scope = 'user-read-playback-state'
scope = 'user-follow-read'
# Intialize spotipy instance

# client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
oAuth = auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=scope, redirect_uri=REDIRECT_URI)
sp = spotipy.Spotify(auth_manager=oAuth)

pp = pprint.PrettyPrinter(indent=2)

sqlite = Sqlite_test(r'database.db')



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

def getReccomendationFromArtist(artist):
    artistGenreInfo = getArtistGenres(artist)
    allReccomendationGenres = sp.recommendation_genre_seeds()

    validGenres = []

    if artistGenreInfo != None and len(artistGenreInfo) > 0:
        # Loop through genres grabbed from calling getArtistGenres
        for n in range(0, len(artistGenreInfo)):
            currentGrabbedGenre = artistGenreInfo[n]
            # Loop through all genres from spotify and add them to the validGenres dictionary if there is a match
            for x in range(0, len(allReccomendationGenres['genres'])):
                if currentGrabbedGenre == allReccomendationGenres['genres'][x]:
                    validGenres.append(currentGrabbedGenre)
    else:
        print('No results found...')

    print('Valid Genres: ' + str(validGenres))

    if len(validGenres) > 0:
        print('\n\n\nReccomendations:')
        for i in range(10):
            pp.pprint(sp.recommendations(seed_genres=validGenres)['tracks'][i]['artists'][0]['name'])
    
        # pp.pprint(sp.recommendations(seed_genres=validGenres))
        
        print('\n\n\n')

def getUsername():
    return sp.current_user()['display_name']

def getFollowedArtists():
    followedArtists = len(sp.current_user_followed_artists()['artists']['items'])
    for i in range(followedArtists):
        print(i+1, ".  ", sp.current_user_followed_artists()['artists']['items'][i]['name'])      
    
if __name__ == '__main__':
    
    Current_user = getUsername()
    # sqlite.addToSavedArtists("SZA", "RB")
    # sqlite.removeArtist("SZA")
    # sqlite.cursor.execute("DROP TABLE Song")
    # pp.pprint(sp.current_user()['display_name'])
    
    
    artist_name = input("Input artist name: ")
    pp.pprint(getArtist(artist_name))
    print("\n\n\n\n")
    getReccomendationFromArtist(artist_name)
    
    
    print(Current_user, "'s following artists:\n")
    getFollowedArtists()
    
    pp
    
