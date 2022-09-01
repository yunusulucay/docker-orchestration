import requests
import json
import time
from pymongo import MongoClient 
import os

try:
    data = requests.get("https://goweather.herokuapp.com/weather/istanbul")
    data_json = data.json()
except:
    # Default data
    data_json = {
        'temperature': '+29 °C',
        'wind': '19 km/h',
        'description': 'Partly cloudy',
        'forecast': [{'day': '1', 'temperature': '+29 °C', 'wind': '26 km/h'},
        {'day': '2', 'temperature': '+26 °C', 'wind': '13 km/h'},
        {'day': '3', 'temperature': ' °C', 'wind': '27 km/h'}]}

try:

    client = MongoClient(
        "mongodb://my_mongodb:27017",
        username="root",
        password="root_pw")

    my_db = client["api"]

    my_collection = my_db["api_collection"]

    record = {
        "temperature":data_json["temperature"],
        "wind":data_json["wind"],
        "description":data_json["description"]}

    my_db.my_collection.insert_one(record)

    print("Sent to MongoDB")
except Exception as e:
    print(f"COULDN'T CONNECT TO MONGO = {e}")