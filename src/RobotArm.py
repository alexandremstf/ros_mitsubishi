import Communication
import time
import StringHandler

class RobotArm :

	def __init__(self) :
		self.comn = Communication.Communication('/dev/ttyUSB0')
		self.stringHandler = StringHandler.StringHandler()

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

	def moveJointPosition(self, j1, j2, j3, j4, j5, speed) :
		jointPosition = self.stringHandler.jointPositionStringConstructor(j1, j2, j3, j4, j5)
		speedString = self.stringHandler.speedStringConstructor(speed)

		commands = []
		commands.append('CNTLON')
		commands.append('EXECJOVRD ' + speedString)
		commands.append('EXECJCOSIROP = ' + jointPosition)
		commands.append('EXECMOV JCOSIROP')
		commands.append('CNTLOFF')
		self.comn.send(commands)

	def moveCartesianPosition(self, x, y, z, a, b, speed) :
		cartesianPosition = self.stringHandler.cartesianPositionStringConstructor(x, y, z, a, b)
		speedString = self.stringHandler.speedStringConstructor(speed)

		commands = []
		commands.append('CNTLON')
		commands.append('EXECSPD ' + speed)
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
