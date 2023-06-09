from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import itertools # Will delete later when done with testing

class YoutubeId:
    
    def __init__(self):
        self.video_id = []

    def get_id(self, developer_key, song_names):
        try:
            YOUTUBE_API_SERVICE_NAME = "youtube"
            YOUTUBE_API_VERSION = "v3"
            youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=developer_key)

            for song in itertools.islice(song_names, 2): # Delete when done
            # for song in song_names:
                search_response = youtube.search().list(
                    q=song,
                    type="video",
                    part="id,snippet",
                    maxResults=1
                ).execute()
                
                self.video_id.append(search_response["items"][0]["id"]["videoId"])
            print(self.video_id)
            return self.video_id
        except HttpError:
            return ""