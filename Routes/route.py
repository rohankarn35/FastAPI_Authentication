from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from pymongo import MongoClient
from utility.utility import *
from main import *


authen_route = APIRouter()

@authen_route.post("/token",response_model=Token)
async def login_for_access_token(form_data:OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect Username or Password",headers={"WWW-Authenticate": "Bearer"})
    access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": form_data.username}, expires_delta=access_token_expire)
    return {"access_token": access_token,"token_type":"Bearer"}

@authen_route.get("/users/me",response_model=User)
async def read_users_me(current_user:User = Depends(get_current_user)):
    return current_user

@authen_route.get("/user/me/item")
async def read_own_items(current_user:User = Depends(get_current_user)):
    return {"item":1,"owner":current_user}

@authen_route.post("/register",response_model=User)
async def create_user(user:UserCreate):
    # check username already exists or not
    existing_user = get_UserInDB(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exist")
    existing_email = get_UserInDB(user.email)
    if existing_email:
        raise HTTPException(status_code=409,detail="Email is already in use")
    hashed_password = get_password_hased(user.password)
    user_data = user.dict()
    user_data["hashed_password"] = hashed_password  
    del user_data["password"]
    collection.insert_one(user_data)
    return user_data

