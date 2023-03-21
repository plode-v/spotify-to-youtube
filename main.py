from spotify import Spotify
from youtube_id import YoutubeId
from dotenv import load_dotenv
import os

# Load_dotenv function is execute for local environment variables
load_dotenv()

spotify = Spotify()
youtube_id = YoutubeId()

playlist = "0m0xz4tyUyhQuJXQEwtyWq" #Replace with your playlist ID

client_id = os.environ["CLIENT_ID"] #Replace with your Spotify Client ID
client_secret = os.environ["CLIENT_SECRET"] # Replace with your Spotify CLient Secret
developer_key = os.environ["YOUTUBE_API_KEY"] # Replace with your YouTube API Key


def app(client_id, client_secret, playlist_id, youtube_id):
    spotify.get_access_token(client_id, client_secret, playlist_id)
    
    youtube_id.get_id(developer_key, spotify.my_songs)

app(client_id, client_secret, playlist, youtube_id)