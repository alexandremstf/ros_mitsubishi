#!/usr/bin/env python

class StringHandler :

	def getSpecificPositionByCoordinate(self, string, coordinate):
		position = None

		split1 = string.split(coordinate + ";")
		if (len(split1) > 1) :
			split2 = split1[1].split(";")
			if (len(split2) > 1) :
				position = float(split2[0])

		return position
	
	def jointPositionStringConstructor(self, j1, j2, j3, j5, j6) :
		
		j1String = str(j1)
		j2String = str(j2)
		j3String = str(j3)
		j5String = str(j5)
		j6String = str(j6)

		jointPosition = '(' + j1String + ', ' + j2String + ', ' + j3String + ', 0.0, ' + j5String + ', ' + j6String + ')' 

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

		jointPosition = { 
			"J1": self.getSpecificPositionByCoordinate(string, "J1"), 
			"J2": self.getSpecificPositionByCoordinate(string, "J2"), 
			"J3": self.getSpecificPositionByCoordinate(string, "J3"), 
			"J5": self.getSpecificPositionByCoordinate(string, "J5"), 
			"J6": self.getSpecificPositionByCoordinate(string, "J6") 
		}

		return jointPosition

	def getCartesianPositionByString(self, string):
		#The cartesian string from robot is like this:
		#QoKX;250.00;Y;0.00;Z;450.00;A;0.00;B;180.00;;6,0;50;0.00;00000000

		cartesianPosition = {
			"X": self.getSpecificPositionByCoordinate(string, "X"),
			"Y": self.getSpecificPositionByCoordinate(string, "Y"),
			"Z": self.getSpecificPositionByCoordinate(string, "Z"),
			"A": self.getSpecificPositionByCoordinate(string, "A"),
			"B": self.getSpecificPositionByCoordinate(string, "B"),
		}

		return cartesianPosition

