from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


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