from spotify import Spotify
from youtube_id import YoutubeId
from dotenv import load_dotenv
import os
import re

# Load_dotenv function is execute for local environment variables
load_dotenv()

class App:
    def __init__(self):
        self.spotify = Spotify()
        self.youtube_id = YoutubeId()
        self.client_id = os.environ["CLIENT_ID"] #Replace with your Spotify Client ID
        self.client_secret = os.environ["CLIENT_SECRET"] # Replace with your Spotify CLient Secret
        self.developer_key = os.environ["YOUTUBE_API_KEY"] # Replace with your YouTube API Key
        self.playlist_link = "https://open.spotify.com/playlist/7FaRRy07GXHSF4c4CKJSaP?si=3942427326c14b2a" # Replace with your own Spotify Playlist's Link
        self.app(self.client_id, self.client_secret, self.playlist_link)
        


    def app(self, client_id, client_secret, playlist_link):
        first = "https://open.spotify.com/playlist/"
        last = "?si="
        
        start = playlist_link.index(first) + len(first)
        end = playlist_link.index(last, start)
        playlist_id = playlist_link[start:end]
        self.spotify.get_access_token(client_id, client_secret, playlist_id)
        self.youtube_id.get_id(developer_key=self.developer_key, song_names=self.spotify.song_names)
        
app = App()