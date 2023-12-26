from fastapi import *
from passlib.context import CryptContext
from UserModel.users import *
from config.db import client
from pymongo import MongoClient
from datetime import *
from jose import JWTError, jwt
from fastapi.security import *

db = client["FastUser"]
collection = db['Userbase']
ALGORITHM = "HS256"
SECRET_KEY="02bf4db4ee6178cc094e3a41fb5d07316127543db677a116d11ecdf27801d752"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password,hased_password):
    return pwd_context.verify(plain_password,hased_password)

def get_password_hased(password):
    return pwd_context.hash(password)

def get_UserInDB(username:str):
    user_data = collection.find_one({"username":username})
    if user_data:
        return UserInDB(**user_data)

def authenticate_user(username: str, password: str):
    user = get_UserInDB(username=username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    else:
        return user


def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
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
    user = get_UserInDB(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user





