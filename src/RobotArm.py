import Communication

class RobotArm :

	def __init__(self) :
		self.comn = Communication.Communication('/dev/ttyS0')

	def init(self) :
		commands = []
		commands.append('OPEN=NARCUSR')
		commands.append('CNTLON')
		commands.append('SRVON')
		commands.append('EXECJOVRD 70.0')
		commands.append('CNTLOFF')
		self.comn.send(commands)

	def reset(self) :
		commands = []
		commands.append('CNTLOFF')
		commands.append('RSTALRM')
		commands.append('SRVOFF')
		commands.append('STATE')
		commands.append('CNTLON')
		self.comn.send(commands)

	def moveToInitialPos(self) :
		commands = []
		initialPos = '(0.000, 0.000, 0.000, 0.000, 0.000, 0.000)'
		commands.append('CNTLON')
		commands.append('EXECJCOSIROP = ' + initialPos)
		commands.append('EXECMOV JCOSIROP')
		commands.append('CNTLOFF')
		self.comn.send(commands)

	def moveToPos(self) :
		commands = []
		initialPos = '(0.000, 30.000, 30.000, 0.000, 0.000, 0.000)'
		commands.append('CNTLON')
		commands.append('EXECJCOSIROP = ' + initialPos)
		commands.append('EXECMOV JCOSIROP')
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
