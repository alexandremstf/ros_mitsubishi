import serial

communnication = serial.Serial(port = '/dev/ttyUSB0', baudrate = 9600)

communnication.write("1;1;OPEN=NARCUSR")
communnication.write("1;1;PARRLNG")
communnication.write("1;1;PDIRTOP")
communnication.write("1;1;PPOSF")
communnication.write("1;1;PARMEXTL")
communnication.write("1;1;KEYWDptest")
communnication.write("1;1;SRVON")
communnication.write("1;1;RSTALRM")
communnication.write("1;1;STATE")
communnication.write("1;1;CNTLON")

communnication.close()
