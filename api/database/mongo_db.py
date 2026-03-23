from pymongo import MongoClient
from pymongo.database import Database
from typing import Annotated
from fastapi import Depends
import os

MONGO_URL = os.getenv("MONGO_URI")
DB_NAME = "petcare_db"

def get_db():
    client = MongoClient(MONGO_URL)
    db = client[DB_NAME]
    try:
        yield db
    finally:
        client.close()

db_dependency = Annotated[Database, Depends(get_db)]