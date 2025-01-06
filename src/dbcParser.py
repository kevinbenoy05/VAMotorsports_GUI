import cantools, cantools.database, json
files = { # List of DBC files 
    "ams": "dbc_files\\ams.dbc",
    "cm200": "dbc_files\\cm200.dbc",
    "IZZE_IRTS_BRAKE_V2":"dbc_files\\IZZE_IRTS_BRAKE_V2.dbc",
    "vcu": "dbc_files\\vcu.dbc"
}
def getSensors(files):
    sensors = {}
    for name, path in files.items():
        try:
            dbc = cantools.database.load_file(path)
            messages = {}
            for message in dbc.messages:
                messages[hex(message.frame_id)] = {
                    "name": message.name,
                    "signals": [
                        {
                            "name": signal.name,
                            "start_bit": signal.start,
                            "length": signal.length,
                            "units": signal.unit,
                            "comment": signal.comment,
                            "min": signal.minimum,
                            "max": signal.maximum,
                        }for signal in message.signals
                    ]
                }
            sensors[name] = messages
        except cantools.database.errors.Error as e:
            print(f"Error loading {name}: {e}\n")
    return sensors
def printSensors(sensorList): # For debugging
    for dbc_name, messages in sensorList.items():
        print(f"\n=== DBC File: {dbc_name} ===")
        for frame_id, details in messages.items():
            print(f"Frame ID: {frame_id} | Message: {details['name']}")
            for signal in details["signals"]:
                print(f"  - Signal: {signal['name']}, Units: {signal['units']}, Min: {signal['min']}, Max: {signal['max']}")