import threading
import time
import serial

class Handle_Thread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.ser = serial.Serial('/dev/cu.usbmodem1421', 9600, timeout=1)
        self.read = 0
        self.stop = False
        self.send = False
        self.data = 0
        self.first = -1
        self.second = -1

    def run(self):

        while not self.stop:

            self.read = self.ser.readline().decode("utf-8")
            if self.read != "":
                self.read = list(self.read)
                self.first = int(self.read[0])
                self.second = int(self.read[1])
                #print("1: ", self.first, self.second)
                #self.last_digit = self.read
                #print("Pedal: ", self.read)

            if self.send == True:
                print("send: ", self.data)
                self.ser.write(self.data)
                self.send = False
