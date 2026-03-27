from pymongo import MongoClient

client = MongoClient("PASTE_YOUR_CONNECTION_STRING")

db = client["teamup_db"]

users_collection = db["users"]
posts_collection = db["posts"]