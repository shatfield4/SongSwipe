from flask import Flask, render_template, url_for, redirect, request
import requests, json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv
import os
import userfunctions
from flask_sqlalchemy import SQLAlchemy
from getToken import getUser

app = Flask(__name__)

# Honestly idk this starts sqlite or something
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Load env variables
load_dotenv(find_dotenv())

# Env Variables
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT_URI")

# Intialize spotipy instance
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#@app.route("/")
#def index():  
#    return render_template("index.html")

@app.route('/')
def index():
    response = getUser(CLIENT_ID, REDIRECT_URI, 5000)
    return redirect(response)
        
@app.route('/callback/')
def callback():
    # Auth Step 4: Requests refresh and access tokens
    SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"

    REDIRECT_URI_ = REDIRECT_URI + ":5000/callback/"

    auth_token = request.args['code']

    code_payload = {
        "grant_type": "authorization_code",
        "code": auth_token,
        "redirect_uri": REDIRECT_URI_,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }

    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload)

    # Auth Step 5: Tokens are Returned to Application
    response_data = json.loads(post_request.text)

    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

    print(access_token)

    return render_template("index.html", access_token = access_token)

if __name__ == "__main__":
    app.run(debug=True)