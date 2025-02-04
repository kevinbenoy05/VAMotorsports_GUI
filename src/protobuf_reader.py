import google.protobuf.message
import json, serial

'''
Continuously read the searial port for protobuf messages while it is on
Get and deserialize those protobuf messages
Convert those incoming messages to JSON
Add each json message(given database  object) to its mongodb database
'''

try:
        with serial.Serial("COM3", 9600, 1) as port:
                proto = port.readline().decode("utf-8").strip()
except serial.SerialException as e:
        print(f"Error: {e}")
except KeyboardInterrupt:
        print("\nExiting...") 