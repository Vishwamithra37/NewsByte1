from http import client
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["newsBytes_url_shortner"]
dac=db["url_shortner"]
