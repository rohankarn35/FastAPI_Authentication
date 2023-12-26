from fastapi import *
from fastapi.security import *
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from Routes.route import authen_route





app = FastAPI()
app.include_router(authen_route)





