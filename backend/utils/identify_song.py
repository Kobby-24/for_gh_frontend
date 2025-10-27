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
ghanaian_artists = os.getenv("GHANAIAN_ARTISTS_FILE").split(",")


def identify_song(file_path):
    """Send file to Audd.io for recognition"""
    try:
        with open(file_path, "rb") as f:
            data = {"api_token": AUDD_API_TOKEN, "return": "spotify,timecode"}
            files = {"file": f}
            result = requests.post("https://api.audd.io/", data=data, files=files)
            response = result.json()
            return response.get("result")
    except Exception as e:
        print("Error identifying song:", e)
        return None