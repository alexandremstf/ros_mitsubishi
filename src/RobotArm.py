#!/usr/bin/env python

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
		
		# clean trash in serial
		for i in range(10) :
			self.comn.readAll()

	def turnOff(self) :
		commands = []
		commands.append('CNTLON')
		commands.append('RSTALRM')
		commands.append('SRVOFF')
		commands.append('STATE')
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

	def moveJointPosition(self, j1, j2, j3, j5, j6, speed) :
		jointPosition = self.stringHandler.jointPositionStringConstructor(j1, j2, j3, j5, j6)
		speedString = self.stringHandler.speedStringConstructor(speed)

		commands = []
		commands.append('CNTLON')
		commands.append('EXECJOVRD ' + speedString)
		commands.append('EXECJCOSIROP = ' + jointPosition)
		commands.append('EXECMOV JCOSIROP')
		commands.append('CNTLOFF')
		self.comn.send(commands)

		# Waits the robot reaches the joint position
		jointPositionDict = self.stringHandler.getJointPositionByString(self.readJointPosition())
		while (jointPositionDict["J1"] != j1 or jointPositionDict["J2"] != j2 or jointPositionDict["J3"] != j3 or jointPositionDict["J5"] != j5) :
			time.sleep(0.5)
			jointPositionDict = self.stringHandler.getJointPositionByString(self.readJointPosition())

	def moveCartesianPosition(self, x, y, z, a, b, speed) :
		cartesianPosition = self.stringHandler.cartesianPositionStringConstructor(x, y, z, a, b)
		speedString = self.stringHandler.speedStringConstructor(speed)

		commands = []
		commands.append('CNTLON')
		commands.append('EXECSPD ' + speedString)
		commands.append('EXECPCOSIROP = ' + cartesianPosition)
		commands.append('EXECMOV PCOSIROP')
		commands.append('CNTLOFF')
		self.comn.send(commands)

		# Waits the robot reaches the cartesian position
		cartesianPositionDict = self.stringHandler.getCartesianPositionByString(self.readCartesianPosition())
		while (cartesianPositionDict["X"] != x or cartesianPositionDict["Y"] != y or cartesianPositionDict["Z"] != z or cartesianPositionDict["A"] != a or cartesianPositionDict["B"] != b):
			time.sleep(0.5)
			cartesianPositionDict = self.stringHandler.getCartesianPositionByString(self.readCartesianPosition())

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

		return self.comn.readUntil('\n', 100)

	def readCartesianPosition(self) :
		commands = []
		commands.append('CNTLON')
		commands.append('PPOSF')
		commands.append('CNTLOFF')
		self.comn.send(commands)

		return self.comn.readUntil('\n', 65)