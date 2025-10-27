import os
import time
import csv
import datetime
import requests
import dotenv

dotenv.load_dotenv()


def log_result(station, title, artist, origin):
    """Save to CSV"""
    with open("log.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now(), station, title, artist, origin])