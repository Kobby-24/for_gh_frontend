from schemas import User, UserLogin
import models
from hashing import Hash 
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from token_utils import create_access_token

def create_user(db: Session, user: User):
    existing_user = db.query(models.Users).filter((models.Users.username == user.username) | (models.Users.email == user.email)).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already registered")
    station = db.query(models.Stations).filter(models.Stations.name == user.station).first() if user.station else None
    if not station:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Station not found")
    new_user = models.Users(
        username=user.username,
        email=user.email,
        hashed_password=Hash.bcrypt(user.password),
        role=user.role,
        station_id=station.id if station else None,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, username: str):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(models.Users).offset(skip).limit(limit).all()
    return users

def login(db:Session, request:UserLogin):
    user = db.query(models.Users).filter(models.Users.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    user.last_login = datetime.now()
    db.commit()
    db.refresh(user)
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return{
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "station": user.station.name if user.station else None
    }
