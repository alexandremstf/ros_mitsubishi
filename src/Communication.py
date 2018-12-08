#!/usr/bin/env python

import serial
import time

class Communication :

    def __init__(self, serialPort) :
        self.serialCommunication = serial.Serial(
            port     = serialPort,
            baudrate = 9600,
            timeout  = 0.5,
            parity   = serial.PARITY_EVEN,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS)

    def __del__(self) :
        self.serialCommunication.close()

    def send(self, list) :
        for command in list :
            self.serialCommunication.write(('1;1;' + command + '\r').encode())
            self.serialCommunication.flush

    def readAll(self) :
        readSerial = self.serialCommunication.read_all()
        time.sleep(0.2)
        return readSerial

    def readUntil(self, character, size) :
        readSerial = self.serialCommunication.read_until(character, size)
        return readSerial