from pymongo import MongoClient
import os

MONGO_URI = os.getenv('MONGO_URI')
DATABASE = os.getenv('DATABASE')
COLLECTION = os.getenv('COLLECTION')

def connectMongo() -> MongoClient:
    return MongoClient(MONGO_URI)

def getCollection() -> MongoClient:
    client = connectMongo()
    db = client[DATABASE]
    return db[str(COLLECTION)]