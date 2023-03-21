from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import os

from spotify import Spotify

load_dotenv()

class YoutubeId:
    
    def __init__(self) -> None:
        pass

    def get_id(self, developer_key, )

DEVELOPER_KEY = os.environ["YOUTUBE_API_KEY"]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# song_names = Spotify().song_names
song_names = ['Run BTS', 'MORE']

for song in song_names:
    search_response = youtube.search().list(
        q=song,
        type="video",
        part="id,snippet",
        maxResults=1
    ).execute()
    
    video_id = search_response["items"][0]["id"]["videoId"]