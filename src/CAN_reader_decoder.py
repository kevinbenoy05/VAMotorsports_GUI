import cantools, can, json, datetime
# List of DBC Files
ams = cantools.db.load_file("dbc_files\\ams.dbc")
cm200 = cantools.db.load_file("dbc_files\\cm200.dbc")
IZZE_IRTS_BRAKE = cantools.db.load_file("dbc_files\\IZZE_IRTS_BRAKE_V2.dbc")
vcu = cantools.db.load_file("dbc_files\\vcu.dbc")
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
def logData(id, message):
    file = ""
    if 0x4c8 <= id <= 0x4d6: 
            file = "json_logs\\IZZE_IRTS_BRAKE.json"
    elif 0x100 <= id <= 0x6b2:
        file = "json_logs\\ams.json"
    elif 0xad <= id <= 0xb1:
        file = "json_logs\\cm200.json"
    elif 0x2f0a000 <= id <= 0x2f0a044:
        file = "json_logs\\vcu.json"
    with open(file, "a") as log:
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "message": decodeMessage(id, message)
        }
        log.write(json.dumps(entry) + "\n")
"""Read data from a CAN Bus -> Logs it into it's respective JSON file
    - MUST BE IMPLEMENTED LATER WITH HARDWARE ACCESS"""
def readCANBus():
    bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=250000)  # This has to be fixed with our CAN bus
    for message in bus:
        logData(message.arbitration_id, message.data)