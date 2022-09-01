from pymongo import MongoClient
import psycopg2
import time
import re

# Wait for PostgreSQL to connect
time.sleep(60)

try:
    # MongoDB Connection
    client = MongoClient(
        "mongodb://my_mongodb:27017",
        username="root",
        password="root_pw")

    my_db = client["api"]

    my_collection = my_db["api_collection"]

    all_files = [i for i in my_db.my_collection.find({})]
    print(all_files)
    print("Get data from MongoDB!")
except Exception as e:
    print(f"ERROR = {e}")

temperature = int(re.findall("\d+",all_files[0]["temperature"])[0])
wind = int(re.findall("\d+",all_files[0]["wind"])[0])
description = all_files[0]["description"]
description = f"'{description}'"

try:
    # PostgreSQL Connection
    conn = psycopg2.connect(
        database="root_db",
        user="root",
        password="root_pw",
        host="postgresql_container")

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS weather_table(id SERIAL PRIMARY KEY, temperature INT, wind INT, description TEXT)")

    cursor.execute(f"INSERT INTO weather_table(temperature, wind, description) VALUES({temperature},{wind},{description})")

    conn.commit()

    cursor.close()

    conn.close()

    print("Data sent to PostgreSQL!")
except Exception as e:
    print(f"ERROR = {e}")
