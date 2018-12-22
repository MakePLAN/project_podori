import serial

ser = serial.Serial('/dev/cu.usbmodem1421', 9600)
while True:
    print("ben")
    print( ser.readline() )