from flask import Flask, jsonify, request, render_template, url_for, redirect
import spotipy, requests, json
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, find_dotenv
import os
import userfunctions
from flask_sqlalchemy import SQLAlchemy
from getToken import getUser
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

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
scope = 'user-follow-read'

oAuth = auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=scope, redirect_uri=REDIRECT_URI)
sp = spotipy.Spotify(auth_manager=oAuth)


# client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Initialize userfunctions
userf = userfunctions

# Responds to GET requests on this route. Returns an artist from URI
#   Example:
#       127.0.0.1:5000/api/getartist/justin%20bieber
#   The above will return getArtist("Justin Bieber") in JSON
@app.route("/api/getartist/<string:artist>", methods = ["GET"])
def api_getArtist(artist):  
    output = userf.getArtist(artist)

    # Output is a dict. Jsonify converts to JSON format
    return jsonify(output)

# Same as above, same syntax when requesting an artist from URI
# Returns recommendations with associated info
@app.route("/api/getreco/<string:artist>", methods = ["GET"])
def api_getRecoFromArtist(artist):
    output = userf.getReccomendationFromArtist(artist)

    return jsonify(output)

# This is a POST request. Responds to POST with a parameter
# Right now just returns what the user passed as param as a list
# Something like this can be used as the redirect attribute in React?
# Maybe when it detects a right/left swipe
@app.route("/api/swiperight", methods = ["POST"])
def api_postSwipeRight():
    input_json = request.get_json(force=True)
    dictToReturn = {"text":input_json["text"]}

    return jsonify(dictToReturn)

@app.route("/")
def index():  
    return render_template("index.html")

@app.route('/auth/')
def auth():
    response = getUser(CLIENT_ID, REDIRECT_URI, 5000)
    return redirect(response)

@cross_origin(supports_credentials=True)
@app.route('/data/')
def data():
    # liked_artist = request.args['artist_liked']
    liked_artist = userf.getFollowedArtists()['name']
    response = userf.getRelatedArtists(liked_artist)
    # response = {"name": "Justin Bieber", "img_url": "https://i.scdn.co/image/ab676161000051748ae7f2aaa9817a704a87ea36", "song_url": "spotify:artist:1uNFoZAHBGtllmzznpCI3s", "genre": "Pop"}
    print(liked_artist)
    print(response)
    return jsonify(response)

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

    #return {"access_token": access_token}
    return redirect(f"https://songswipe-0.netlify.app?access_token={access_token}", code=307)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
