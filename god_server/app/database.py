from pymongo import MongoClient
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")

client = MongoClient(MONGO_DETAILS)
database = client.god_server
clock_tasks_collection = database.get_collection("clock_tasks")

def get_db():
    return client

def create_clock_task(db, encrypted_data):
    clock_task = db.clock_tasks_collection.insert_one({"encrypted_data": encrypted_data})
    return str(clock_task.inserted_id)

def get_clock_task(db, clock_task_id):
    task = db.clock_tasks_collection.find_one({"_id": ObjectId(clock_task_id)})
    return task["encrypted_data"] if task else None
