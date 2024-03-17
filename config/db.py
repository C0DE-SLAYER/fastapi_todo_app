from pymongo import MongoClient
conn = MongoClient('mongodb://localhost:27017/')

db = conn.todo_db

collection_name = db['todos']