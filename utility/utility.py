from main import *
from passlib.context import CryptContext
from UserModel.users import *
from config.db import client
from pymongo import MongoClient
from datetime import *
from jose import JWTError, jwt
from fastapi.security import *

db = client["addfs"]
collection = db['Users']

def verify_password(plain_password,hased_password):
    return pwd_context.verify(plain_password,hased_password)

def get_password_hased(password):
    return pwd_context.hash(password)

def get_UserInDB(username:str):
    user_data = collection.find_one({"username":username})
    if user_data:
        return UserInDB(**user_data)

def authenticate_user(username:str,password:str):
    user = get_UserInDB(username=username)
    if not user or not verify_password(password,user.password):
        return False
    else:
        return user

def create_access_token(data:dict, expire_delta: timedelta or None = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.now() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials", headers={"www-authenticate":"bearer"})
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username= username)
    except JWTError:
        raise credentials_exception
    user = get_userInDB(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400,detail="Account has been disabled")
    return current_user




