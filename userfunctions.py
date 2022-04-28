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
# Intialize spotipy instance

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
# oAuth = auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=scope, redirect_uri=REDIRECT_URI)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

pp = pprint.PrettyPrinter(indent=2)

sqlite = Sqlite_test(r'database.db')


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

    # Find all genres that match the artist to all genres
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

    # Get song reccomendations from the artist specified
    if len(validGenres) > 0:
        print('\n\n\nReccomendations:')

        reccomendationsOutput = sp.recommendations(seed_genres=validGenres)

        songReccomendationIds = []
        songReccomendationNames = []
        songPreviewUrls = []

        # Get song names and IDs from spotipy
        for x in range(0, len(reccomendationsOutput['tracks'])):
            songReccomendationIds.append(reccomendationsOutput['tracks'][x]['id'])
            songReccomendationNames.append(reccomendationsOutput['tracks'][x]['name'])
            songPreviewUrls.append(reccomendationsOutput['tracks'][x]['preview_url'])


        pp.pprint(songReccomendationIds)
        pp.pprint(songReccomendationNames)
        pp.pprint(songPreviewUrls)


        # pp.pprint(sp.recommendations(seed_genres=validGenres)['tracks'][0]['name'])
        print('\n\n\n')






if __name__ == '__main__':
    
    
    # sqlite.addToSavedArtists("SZA", "RB")
    # sqlite.removeArtist("SZA")
    # sqlite.cursor.execute("DROP TABLE Song")


    artist_name = input("Input artist name: ")
    # pp.pprint(getArtist(artist_name))
    print("\n\n\n\n")
    getReccomendationFromArtist(artist_name)

