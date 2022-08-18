from fastapi import APIRouter
from schemas.scehmas import UserRequest, UserResponse
from db.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from db.models.models import Users
from datetime import date
import time
user_router = APIRouter()

@user_router.get("/", description="Root Users")
def root():
    return "Root API"


@user_router.post("/", description="Create users", response_model=UserResponse)
def create_user(user:UserRequest, db: Session = Depends(get_db)):
    user_dict = user.dict()
    ed_user = Users(**user_dict, date_created=int(time.time()))
    db.add(ed_user)
    db.commit()
    our_user = db.query(Users).filter_by(id=ed_user.id).first()
    our_user.date_created = date.fromtimestamp(our_user.date_created)
    return our_user

# @user_router.get("/{user_id}/", description="Get user by id", res)
