from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas import User, UserLogin
from utils.users import create_user, get_user, get_all_users, login as user_login

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=User)
def create_new_user(user: User, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/{username}", response_model=User)
def read_user(username: str, db: Session = Depends(get_db)):
    return get_user(db, username)   

@router.get("/", response_model=list[User])
def read_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_users(db, skip, limit)

@router.post("/login")
def login(request: UserLogin, db: Session = Depends(get_db)):
    return user_login(db, request)