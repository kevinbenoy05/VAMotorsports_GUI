import test_pb2, serial
ser = serial.Serial("/dev/ttyACM0", 9600)
handshake = test_pb2.Test()
handshake.handshake = 1
ser.write(handshake.SerializeToString())
print("test")

