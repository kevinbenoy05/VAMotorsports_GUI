import os
import cantools, json, datetime, urllib
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
# List of DBC Files
ams = cantools.db.load_file("dbc_files\\ams.dbc")
cm200 = cantools.db.load_file("dbc_files\\cm200.dbc")
IZZE_IRTS_BRAKE = cantools.db.load_file("dbc_files\\IZZE_IRTS_BRAKE_V2.dbc")
vcu = cantools.db.load_file("dbc_files\\vcu.dbc")
#MongoDB Setup
load_dotenv()
username = os.getenv("username")
password = os.getenv("password")
uri = "mongodb+srv://{username}:" + urllib.parse.quote(password)+"@cluster.simtg.mongodb.net/?retryWrites=true&w=majority&appName=cluster"
client = MongoClient(uri, server_api=ServerApi(version='1', strict=True, deprecation_errors=True))


"""Decode a CAN Frame
    - Different ID ranges need different DBC files
    - Decode the Message using the DBC file determined by the ID"""
def decodeMessage(id, message):
    try:
        if 0x4c8 <= id <= 0x4d6: 
            return IZZE_IRTS_BRAKE.decode_message(id, message)
        elif 0x100 <= id <= 0x6b2:
            return ams.decode_message(id, message)
        elif 0xad <= id <= 0xb1:
            return cm200.decode_message(id, message)
        elif 0x2f0a000 <= id <= 0x2f0a044:
            return vcu.decode_message(id, message)
        else:
            print(f"ID {hex(id)} not found in any range.")
    except KeyError as e:
        print(f"KeyError: {e}. ID: {hex(id)}, Message: {message}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None


"""Log each collected CAN Frame into a JSON file(Same as DBS file name)"""
def logDataToJSON(id, message):
    file = ""
    if 0x4c8 <= id <= 0x4d6: 
            file = "json_logs\\IZZE_IRTS_BRAKE.json"
    elif 0x100 <= id <= 0x6b2:
        file = "json_logs\\ams.json"
    elif 0xad <= id <= 0xb1:
        file = "json_logs\\cm200.json"
    elif 0x2f0a000 <= id <= 0x2f0a044:
        file = "json_logs\\vcu.json"
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "message": decodeMessage(id, message)
    }
    if os.path.exists(file):
        try:
            with open(file, "r") as log:
                data = json.load(log)
                if not isinstance(data, list):
                    data = []  #
        except (json.JSONDecodeError, FileNotFoundError):
            data = []
    else:
        data = []
    data.append(entry)
    with open(file, "w") as log:
        json.dump(data, log, indent=4)


"""Log's CAN data to it's respective DB on mongoDB"""
def logDataToDB(id, message):
    collectionName = ""
    if 0x4c8 <= id <= 0x4d6: 
            collectionName = "IZZE_IRTS_BRAKE"
    elif 0x100 <= id <= 0x6b2:
        collectionName = "ams"
    elif 0xad <= id <= 0xb1:
        collectionName = "cm200"
    elif 0x2f0a000 <= id <= 0x2f0a044:
        collectionName = "vcu"
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "message": decodeMessage(id, message)
    }
    try:
        database = client["decoded_data"]
        collection = database.get_collection(collectionName)
        collection.insert_one(entry)
    except Exception as e:
        print(f"An error occurred: {e}")


"""Read data from a CAN Bus -> Logs it into it's respective JSON file
    - MUST BE IMPLEMENTED LATER WITH HARDWARE ACCESS"""
# def readCANBus():
#     bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=250000)  # This has to be fixed with our CAN bus
#     for message in bus:
#         logDataToJSON(message.arbitration_id, message.data)


"""Things I need to fix:
    When logging, I can't continuously open and close the client for each add. 
    There must be a way, maybe when the car is on connect and when the car is off close(In C++....)
        Then just call the functions as you need 
    Maybe have a main method that continously gets the serial port output and have it run while you have the fcafr 
        You cannot use without WiFi...."""