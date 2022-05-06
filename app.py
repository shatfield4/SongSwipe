from flask import Flask, jsonify, render_template, url_for
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv
import os
import userfunctions
from flask_sqlalchemy import SQLAlchemy

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

@app.route("/api/getreco/<string:artist>", methods = ["GET"])
def api_getRecoFromArtist(artist):
    output = userf.getReccomendationFromArtist(artist)

    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)