import serial

serialCom = serial.Serial(port = 'COM1', 
baudrate = 9600,
parity = serial.PARITY_EVEN, 
stopbits = serial.STOPBITS_ONE, 
bytesize = serial.EIGHTBITS)

#print serialCom

serialCom.write(('1;1;OPEN=NARCUSR'+'\r').encode())
serialCom.write(('1;1;CNTLON'+'\r').encode())
serialCom.write(('1;1;SRVON'+'\r').encode())
serialCom.write(('1;1;CNTLOFF'+'\r').encode())

serialCom.close()
