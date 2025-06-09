# ────────────────────────────────
# 🔗 ingestion/db_loader.py
# ────────────────────────────────
from pymongo import MongoClient
import mysql.connector

def load_from_mongo(uri, db, collection):
    client = MongoClient(uri)
    return [doc for doc in client[db][collection].find()]

def load_from_mysql(config):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM your_table")
    return cursor.fetchall()
