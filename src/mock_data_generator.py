import json, random, socket, time
from datetime import datetime
with open('mock_data/signal_ranges.json', 'r') as file:
    signals = json.load(file)
def getSignals(data): #Get a list of all the signals and ranges in a JSON structured array
    messages = {}
    for bus, msgID in data.items():
        for canID, message in msgID.items():
            messages[canID] = {
                "name": message["name"],
                "signals":[{
                    "name": signal["name"],
                    "start_bit": signal["start_bit"],
                    "length": signal["length"],
                    "min": signal["min"],
                    "max": signal["max"],
                    "units": signal.get("units"),
                }for signal in message["signals"]]
            }
    return messages
messages = getSignals(signals)
def genrateMockCANMsg(canID, message):
    data = [0] * 9
    for signal in message["signals"]:
        value = random.uniform(signal["min"], signal["max"])
        scaled = int(value)
        start_bit = signal["start_bit"]
        length = signal["length"]
        for i in range(length): #Figure out what this does 
            byte_index = (start_bit + i) // 8
            bit_index = (start_bit + i) % 8
            if scaled & (1 << i):
                data[byte_index] |= 1 << bit_index
    return {
         "id": canID,
         "data" : data,
         "message": {
            "name": message.get("name", "Unknown"),  # Ensure no invalid fields
            "signals": message.get("signals", [])   # Default to an empty list
        }
    }
def generateCANDataFile(samples):
    with open("mock_data\\mockData.json", "w") as file:
        mock_data_list = []
        for id, message in messages.items():
            for _ in range(samples):
                mockMsg = genrateMockCANMsg(id, message)
                mockMsg["timestamp"] = datetime.now().isoformat()
                mock_data_list.append(mockMsg)
        json.dump(mock_data_list, file, indent=4)
def streamData():
    host = "0.0.0.0"
    port = 5050
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server.bind((host, port))
    server.listen(1)
    print(f"Streaming CAN data on {host}:{port}")
    
    try:
        connection, address = server.accept()
        print(f"Connection from {address}")
        
        while True:
            for id, message in messages.items():
                try:
                    # Generate mock message
                    mock_message = genrateMockCANMsg(id, message)
                    mock_message["timestamp"] = datetime.now().isoformat()
                    # Send data to the client
                    connection.sendall(json.dumps(mock_message).encode() + b"\n")
                    time.sleep(1)  # Adjust delay to reduce connection stress
                except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError) as e:
                    print(f"Connection lost: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Server closed")
        connection.close()
        server.close()