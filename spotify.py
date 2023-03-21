import requests
import os
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

class Spotify:
    
    def __init__(self):
        self.song_names = []
        self.artist_names = []
        
    def get_access_token(self, client_id, client_secret, playlist_id):
        
        # Get access token from Spotify account using client ID and Secret
        auth_response = requests.post("https://accounts.spotify.com/api/token", {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        })

        access_token = auth_response.json()["access_token"]

        # Once we have the access token, we now can get list of tracks from the playlist
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", headers=headers)

        # Get all meta data and actual data for all tracks
        all_tracks_info = response.json()["items"]

        # Loop through all tracks to get track and artist's name
        for track in all_tracks_info:
            self.song_names.append(track["track"]["name"])
            
        return self.song_names