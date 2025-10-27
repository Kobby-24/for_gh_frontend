from datetime import datetime
from pydantic import BaseModel

class Station(BaseModel):
    name: str
    url: str

class Artist(BaseModel):
    name: str
    origin: str

class SongPlay(BaseModel):
    played_at: datetime
    title: str
    artist: Artist
    station: Station

class User(BaseModel):
    username: str
    email: str
    password: str
    role: str
    created_at: datetime
    updated_at: datetime
    last_login: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserInDB(User):
    hashed_password: str
    role: str
    