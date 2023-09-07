import pymongo
import pandas as pd
from pymongo import * 
def get_data_from_mongo():
    # Replace with your actual MongoDB Atlas connection string
    mongo_uri = "mongodb+srv://rupeshzore5549:Rupesh1234@rzcluster.m8zrurd.mongodb.net/?retryWrites=true&w=majority"

    # Create a MongoClient
    client = pymongo.MongoClient(mongo_uri)

    # Access your MongoDB database
    db = client["DATABASE"]  # Replace "mydatabase" with your database name

    # Access your MongoDB collection
    collection = db["My collection"]  # Replace "mycollection" with your collection name

    # Find the document containing the JSON file (assuming it's stored in a field called "file_field_name")
    cursor = collection.find()
    data = list(cursor)

    df = pd.DataFrame(data)

get_data_from_mongo()