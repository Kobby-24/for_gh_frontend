from sqlalchemy.orm import Session
import os
import models
from record_stream import record_stream
from identify_song import identify_song
from log_result import log_song_play





def scan_station(db: Session, station: models.Station):
    """Runs the full scan-and-log process for a single station."""
    print(f"Recording from {station.name}...")
    file_path = record_stream(station_name=station.name, stream_url=station.stream_url)

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print("Recording failed or created an empty file.")
        return

    print("Identifying song...")
    song_info = identify_song(file_path)

    if song_info:
        title = song_info.get("title", "Unknown Title")
        artist = song_info.get("artist", "Unknown Artist")
        log_song_play(db, station, title, artist)
    else:
        print("No song detected.")