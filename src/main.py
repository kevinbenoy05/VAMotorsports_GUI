from pymongo import MongoClient
from pymongo.server_api import ServerApi
from serial_reciever import getSerialData
from dotenv import load_dotenv
import os


load_dotenv()
username = os.getenv("username")
password = os.getenv("password")
uri = f"mongodb+srv://{username}:{password}@cluster.simtg.mongodb.net/?retryWrites=true&w=majority&appName=cluster"
client = MongoClient(uri, server_api=ServerApi(version='1', strict=True, deprecation_errors=True))

client.connect()
getSerialData()
client.close()