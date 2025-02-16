import serial, test_pb2
ser = serial.Serial("/dev/ttyACM0", 9600)
handshakerecieve = test_pb2.Test()
while True:
    print("recieve")
    handshakerecieve.ParseFromString(ser.read())
    print("received!")
    print(handshakerecieve.handshake)