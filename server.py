from flask import Flask, render_template, url_for
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv
import os
import userfunctions
from flask_sqlalchemy import SQLAlchemy
import datetime

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

x = datetime.datetime.now()

@app.route("/data")
def apistuff():  
    return {
        'name': 'Songswipe',
        'date': x,
        'language': 'Python'
    }

if __name__ == '__main__':
    app.run(debug=True)