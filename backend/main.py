# app/main.py
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from database import SessionLocal
import models
from utils import scan_station

app = FastAPI()

def scan_all_stations():
    """Fetches all stations from DB and runs the scanner for each."""
    print("--- Starting scheduled scan ---")
    db = SessionLocal()
    try:
        stations = db.query(models.Station).all()
        if not stations:
            print("No stations found in the database. Add a station to begin scanning.")
            return
            
        for station in stations:
            scan_station(db, station)
    finally:
        db.close()
    print("--- Scheduled scan finished ---")

@app.on_event("startup")
def start_scheduler():
    scheduler = BackgroundScheduler()
    # Schedule the job to run every 60 seconds
    scheduler.add_job(scan_all_stations, 'interval', seconds=60)
    scheduler.start()
    print("Scheduler started. First scan will run shortly.")

@app.get("/")
def read_root():
    return {"message": "Radio Scanner API is running."}