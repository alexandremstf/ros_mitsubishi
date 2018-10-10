import Communication
import time

class RobotArm :

	def __init__(self) :
		self.comn = Communication.Communication('/dev/ttyUSB0')

	def init(self) :
		commands = []
		commands.append('OPEN=NARCUSR')
		commands.append('CNTLON')
		commands.append('SRVON')
		commands.append('CNTLOFF')
		self.comn.send(commands)
		self.comn.read()

	def reset(self) :
		commands = []
		commands.append('CNTLOFF')
		commands.append('RSTALRM')
		commands.append('SRVOFF')
		commands.append('STATE')
		commands.append('CNTLON')
		self.comn.send(commands)

	def moveJointPosition(self, position) :
		commands = []
		commands.append('CNTLON')
		commands.append('EXECJOVRD 80.0')
		commands.append('EXECJCOSIROP = ' + position)
		commands.append('EXECMOV JCOSIROP')
		commands.append('CNTLOFF')
		self.comn.send(commands)

	def moveCartesianPosition(self, position) :
		commands = []
		commands.append('CNTLON')
		commands.append('EXECSPD 200.0')
		commands.append('EXECPCOSIROP = ' + position)
		commands.append('EXECMVS PCOSIROP')
		commands.append('CNTLOFF')
		self.comn.send(commands)

	def handOpen(self) :
		commands = []
		commands.append('CNTLON')
		commands.append('EXECHOPEN 1')
		commands.append('CNTLOFF')
		self.comn.send(commands)

	def handClose(self) :
		commands = []
		commands.append('CNTLON')
		commands.append('EXECHCLOSE 1')
		commands.append('CNTLOFF')
		self.comn.send(commands)

	def readJointPosition(self) :
		commands = []
		commands.append('CNTLON')
		commands.append('JPOSF')
		commands.append('CNTLOFF')

		self.comn.send(commands)
		time.sleep(0.2)

		return self.comn.read()

	def readCartesianPosition(self) :
		commands = []
		commands.append('CNTLON')
		commands.append('PPOSF')
		commands.append('CNTLOFF')

		self.comn.send(commands)
		time.sleep(0.5)

		return self.comn.read()
