from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()


CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

song_names = []
artist_names = []

# Get access token from Spotify account using client ID and Secret
auth_response = requests.post("https://accounts.spotify.com/api/token", {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
})

access_token = auth_response.json()["access_token"]

# Once we have the access token, we now can get list of tracks from the playlist

playlist_id = "0m0xz4tyUyhQuJXQEwtyWq"
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", headers=headers)

# Get all meta data and actual data for all tracks
all_tracks_info = response.json()["items"]

# Loop through all tracks to get track and artist's name
for track in all_tracks_info:
    song_names.append(track["track"]["name"])
    artist_names.append(track["track"]["album"]["artists"][0]["name"])

