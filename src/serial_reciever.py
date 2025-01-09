import serial, CAN_reader_decoder
"""Splits and gets the ID and payload of a message
    NOTE: This may change depending on how the car Returns CAN messages 
"""
def parse(message):
    try:
        splitMessage = message.split()
        if(len(splitMessage)==2):
             id = splitMessage[0].split(":")[1]
             message = splitMessage[1].split(":")[1]
        return {
            "id": id.strip(),
            "message": message.strip()
        }
    except Exception as e:
        return None
"""Converts and logs data from Port to its associated JSON file"""
def getSerialData():
    try:
        with serial.Serial("COM3", 9600, 1) as port:
            while True:
                data = port.readLine().decode("utf-8").strip()
                if data != None:
                    print(data)
                    can = parse(data)
                    CAN_reader_decoder.logDataToDB(can["id"], can["message"])
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")    