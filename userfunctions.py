#THIS BRANCH IS BEHIND - WORKING ON A FUNCTION.


from flask import redirect
import spotipy
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
from sqlite_test import Sqlite_test

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
        resultsFromGenre = sp.recommendations(seed_genres=validGenres)
        pp.pprint(resultsFromGenre)
        print('\n\n\n')
        pp.pprint(getSongsFromGenres(validGenres))

def getSongsFromGenres(validGenres):
    
    tracks = ['3qN5qMTKyEEmiTZD38BNTT']

    resultsFromGenre = sp.recommendations(seed_genres=validGenres)
    songRecs = sp.recommendations(seed_tracks=tracks)

    # tracks = ['3qN5qMTKyEEmiTZD38BNTT', '2RttW7RAu5nOAfq6YFvApB', '3oIhthYPSKwAwJLA8JClkV', '6kwAbEjseqBob48jCus7Sz']

    #This if statement is suppose to compare songs with the same genres as fetched before,
    #but Spotify doesn't give out the track genre based off this error "KeyError: 'genres'". 
    #Code runs fine til it gets tp the if statement. Will be actively working on this.

    if (songRecs['genres'][validGenres] == resultsFromGenre['genres']):
        for x in range(0, len(songRecs['tracks'])):
            pp.pprint(sp.recommendations(seed_tracks=tracks)['tracks'][x]['name'])

    return songRecs
    #  genreRec = ""

    #  for ele in validGenres:
    #      genreRec += ele

    #  return sp.category_playlists(category_id=genreRec, limit=20, offset=0)
    
    #Just some random psuedocode that I didn't use
    #if songwithgenre == genre {
    # return song
    # }





# if __name__ == '__main__':
    
    
    # sqlite.addToSavedArtists("SZA", "RB")
    # sqlite.removeArtist("SZA")
    # sqlite.cursor.execute("DROP TABLE Song")


artist_name = input("Input artist name: ")
pp.pprint(getArtist(artist_name))
print("\n\n\n\n")
getReccomendationFromArtist(artist_name)


