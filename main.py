from fastapi import *
from fastapi.security import *
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY=""
ACCESS_TOKEN_EXPIRES_IN_MINUTES = 30
ALGORITHM = "HS256"

app = FastAPI()

