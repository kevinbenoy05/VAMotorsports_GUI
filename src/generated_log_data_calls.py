from CAN_reader_decoder import logDataToDB, logDataToJSON
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random, urllib, os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
uri = f"mongodb+srv://{username}:{password}@cluster.simtg.mongodb.net/?retryWrites=true&w=majority&appName=cluster"
client = MongoClient(uri, server_api=ServerApi(version='1', strict=True, deprecation_errors=True))
# Valid data for 100 calls
valid_data = [
    (0x4c8, bytes([10, 20, 30, 40, 50, 60, 70, 80, 34])),
    (0x4d0, bytes([15, 25, 35, 45, 55, 65, 75, 85, 34])),
    (0x4d6, bytes([20, 30, 40, 50, 60, 70, 80, 90, 35])),
    (0x100, bytes([5, 15, 25, 35, 45, 55, 65, 75])),
    (0x150, bytes([10, 20, 30, 40, 50, 60, 70, 80])),
    (0x6b2, bytes([25, 35, 45, 55, 65, 75, 85, 95])),
    (0xad, bytes([5, 10, 15, 20, 25, 30, 35, 40])),
    (0xb0, bytes([15, 20, 25, 30, 35, 40, 45, 50])),
    (0xb1, bytes([20, 25, 30, 35, 40, 45, 50, 55])),
    (0x2f0a000, bytes([1, 2, 3, 4, 5, 6, 7, 8])),
    (0x2f0a010, bytes([9, 10, 11, 12, 13, 14, 15, 16])),
    (0x2f0a044, bytes([17, 18, 19, 20, 21, 22, 23, 24]))
]
#Ping MongoDB 
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Call logData with valid data
# client._connect()
for i in range(100):
    can_id, message = random.choice(valid_data)
    logDataToJSON(can_id, message)
# client.close()