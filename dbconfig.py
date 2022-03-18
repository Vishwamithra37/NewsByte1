from http import client
import pymongo
from config import URL_LIFETIME

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["newsBytes_url_shortner"]
dac=db["url_shortner"]
dac.drop_indexes()
dac.create_index([("short_url",pymongo.ASCENDING)],unique=True)
dac.create_index([("created_at",pymongo.ASCENDING)],expireAfterSeconds=URL_LIFETIME)

