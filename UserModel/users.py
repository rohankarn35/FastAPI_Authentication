from pydantic import BaseModel,EmailStr
from utility import *



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str or None = None


class User(BaseModel):
    username: str
    email: EmailStr or None = None
    full_name: str or None = None


class UserInDB(User):
    hashed_password: str

    @classmethod
    def from_mongo(cls, user_data):
        # Exclude extra fields (_id) from input data
        user_data.pop("_id", None)
        return cls(**user_data)

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str