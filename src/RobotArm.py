import Communication

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
		commands.append('EXECJOVRD 80.0')
		commands.append('EXECJCOSIROP = ' + initialPos)
		commands.append('EXECMOV JCOSIROP')
		commands.append('CNTLOFF')
		self.comn.send(commands)

	def moveToPos(self) :
		commands = []
		initialPos = '(250.000, 0.000, 450.000, 0.000, 180.000, 0.000)(6,0)'
		commands.append('CNTLON')
		commands.append('EXECSPD 200.0')
		commands.append('EXECPCOSIROP = ' + initialPos)
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

	def moveToCartesianPos(self) :
		commands = []
		pos = '(200.000, 200.000, 200.000, 200.000, 0.000, 0.000)(6,0)' #(X,Y,Z,ANGULO GARRA, ANGULO GARRA , 0)
		commands.append('CNTLON')
		commands.append('EXECPCOSIROP = (20.00, 20.00, 400.00, 2.58, 178.02, 0.00)(6,0)')
		commands.append('EXECMVS PCOSIROP')
		commands.append('CNTLOFF')
		self.comn.send(commands)
