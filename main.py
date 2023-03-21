from spotify import Spotify
from dotenv import load_dotenv
import os

load_dotenv()

playlist = "0m0xz4tyUyhQuJXQEwtyWq"

client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

def app(client_id, client_secret, playlist_id):
    spotify = Spotify()
    spotify.get_access_token(client_id, client_secret, playlist_id)