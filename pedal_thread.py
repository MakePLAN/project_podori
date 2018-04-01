import threading
import time
import serial


class Pedal_Thread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.ser = serial.Serial('/dev/cu.usbmodem14141', 9600)
        self.stop = False
        self.last_digit = None


    def run(self):

        while not self.stop:

            read = self.ser.readline().decode("utf-8")
            #print(read)
            if self.last_digit != read and read != "":
                self.last_digit = int(read)




