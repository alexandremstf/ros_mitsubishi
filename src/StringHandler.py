#!/usr/bin/env python

class StringHandler :
	
	def jointPositionStringConstructor(self, j1, j2, j3, j4, j5) :
		
		j1String = str(j1)
		j2String = str(j2)
		j3String = str(j3)
		j4String = str(j4)
		j5String = str(j5)

		jointPosition = '(' + j1String + ', ' + j2String + ', ' + j3String + ', ' + j4String + ', ' + j5String + ', 0.000)' 
		return jointPosition


	def cartesianPositionStringConstructor(self, x, y, z, a, b) :

		xString = str(x)
		yString = str(y)
		zString = str(z)
		aString = str(a)
		bString = str(b)
		
		cartesianPosition = '(' + xString + ', ' + yString + ', ' + zString + ', ' + aString + ', ' + bString + ', 0.000)(6,0)'
		return cartesianPosition


	def speedStringConstructor(self, speed) :
		speedString = str(speed)
		return speedString

	def getJointPositionByString(self, string):
		#The joint string from robot is like this:
		#QoKJ1;0.00;J2;21.19;J3;72.78;J4;****;J5;86.03;J6;0.00;;****,****;50;0.00;00000000

		elements = string.split(";")
		jointPosition = {
			"J1": float(elements[1]),
  			"J2": float(elements[3]),
  			"J3": float(elements[5]),
  			"J4": float(elements[9]),
  			"J5": float(elements[11]),
		}
		
		return jointPosition

	def getCartesianPositionByString(self, string):
		#The cartesian string from robot is like this:
		#QoKX;250.00;Y;0.00;Z;450.00;A;0.00;B;180.00;;6,0;50;0.00;00000000

		elements = string.split(";")
		cartesianPosition = {
			"X": float(elements[1]),
  			"Y": float(elements[3]),
  			"Z": float(elements[5]),
  			"A": float(elements[7]),
  			"B": float(elements[9]),
		}
		
		return cartesianPosition


