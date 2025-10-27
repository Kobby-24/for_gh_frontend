import os
import time
import csv
import datetime
import requests
import dotenv

dotenv.load_dotenv()

# --- CONSTANTS ---
STREAM_URL = os.getenv("STREAM_URL")
STATION_NAME = os.getenv("STATION_NAME")
AUDD_API_TOKEN = os.getenv("AUDD_API_TOKEN")
GHANAIAN_ARTISTS_FILE = os.getenv("GHANAIAN_ARTISTS_FILE")

# --- FUNCTIONS ---

def record_stream(duration=30):
    """Record audio snippet from radio stream"""
    filename = f"recordings/{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    os.system(f'ffmpeg -y -i "{STREAM_URL}" -t {duration} -acodec copy {filename}')
    return filename