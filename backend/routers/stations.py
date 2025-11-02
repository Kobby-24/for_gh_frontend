from fastapi import APIRouter
from utils.stations import get_station_export, get_all_stations

router = APIRouter()

@router.get("/stations/{station_id}/export")
def station_export(station_id: int):
    return get_station_export(station_id)

@router.get("/stations")
def all_stations():
    return get_all_stations()