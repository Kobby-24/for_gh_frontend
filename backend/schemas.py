from datetime import datetime
from pydantic import BaseModel

class Station(BaseModel):
    name: str
    url: str
    base_tax: float

class GetStation(BaseModel):
    name: str  


class Payment(BaseModel):
    user_id: int
    amount: float
    payment_date: datetime
    method: str
    status: str
    foreign_percentage: float
    local_percentage: float


class Artist(BaseModel):
    name: str
    origin: str

class SongPlay(BaseModel):
    played_at: datetime
    title: str
    artist: Artist
    station: Station


    


class UserLogin(BaseModel):
    username: str
    password: str
class UserResponse(UserLogin):
    username: str
    email: str
    role: str
    created_at: datetime
    updated_at: datetime
    last_login: datetime
    station: GetStation | None = None
    
class User(UserResponse):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserInDB(User):
    hashed_password: str
    role: str
    