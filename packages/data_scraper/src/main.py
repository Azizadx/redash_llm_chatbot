import os
from dotenv import load_dotenv  # Import the dotenv library
from yb_statistics import YTstats
load_dotenv()
API_KEY = os.getenv("API_KEY")
CHANNEL_ID = os.getenv("CHANNEL_ID")

yt = YTstats(API_KEY, CHANNEL_ID)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()
