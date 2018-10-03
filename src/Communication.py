import serial
import time

class Communication :

    def __init__(self, serialPort) :
        self.serialCommunication = serial.Serial(
            port     = serialPort,
            baudrate = 9600,
            parity   = serial.PARITY_EVEN,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS)

    def __del__(self) :
        self.serialCommunication.close()

    def send(self, list) :
        for command in list :
            self.serialCommunication.write(('1;1;' + command + '\r').encode())
            time.sleep(0.1)

    def read(self) :
        return self.serialCommunication.read_all()
