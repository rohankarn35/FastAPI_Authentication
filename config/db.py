from pymongo import MongoClient
from os import getenv

MONGODB_URI = getenv("MONGODB_URI")
client = MongoClient("MONGODB_URI")