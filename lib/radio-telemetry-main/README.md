# radio-telemetry

telemetry using the SX1262MB2CAS transceiver

/transmitter: hosted on an arduino on the car, this codebase is responsible for transmitting CAN data from the various sensors on the car and transmitting it over radio to the base computer.

/receiver: hosted on the base computer, this codebase is responsible for receiving the radio communication from the car and logging it to a file.

helpful datasheet located [here](https://www.mouser.com/ProductDetail/Semtech/SX1262MB2CAS?qs=qSfuJ%252Bfl%2Fd69tTGSeW1ezg%3D%3D)

NOTE: create your own virtual environment if working in the receiver folder and use `pip install -r requirements.txt` to install the dependencies.

NOTE: the /transmitter folder uses Platformio. learn more [here](https://platformio.org/) and download the vscode extension [here](https://platformio.org/install/ide?install=vscode)
