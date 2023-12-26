from fastapi import *
from fastapi.security import *
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from UserModel.users import *
from Routes.route import authen_route

SECRET_KEY="02bf4db4ee6178cc094e3a41fb5d07316127543db677a116d11ecdf27801d752"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()
app.include_router(authen_route)





