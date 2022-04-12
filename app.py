from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv
import os

app = Flask(__name__)

# Load env variables
load_dotenv(find_dotenv())

# Env Variables
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT_URI")

# Intialize spotipy instance
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route("/")
def hello_world():  
    print("Hello")
    # related = sp.artist_related_artists('spotify:artist:3jOstUTkEu2JkjvRdBA5Gu')
    
    results = sp.current_user_saved_tracks()
    
    for idx, item in enumerate(results['items']):
        track = item['track']

        print(idx, track['artists'][0]['name'], " – ", track['name'])
        
    return render_template('index.html')




@app.route("/recommendations")
def reccomendations():
    return render_template('recommendations.html', )