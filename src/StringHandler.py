#!/usr/bin/env python

class StringHandler :
	
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

		jointPosition = { "J1": None, "J2": None, "J3": None, "J5": None, "J6": None }

		split1 = string.split("J1;")
		if (len(split1) > 1) :
			split2 = split1[1].split(";")
			if (len(split2) > 1) :
				jointPosition["J1"] = float(split2[0])

		split1 = string.split("J2;")
		if (len(split1) > 1) :
			split2 = split1[1].split(";")
			if (len(split2) > 1) :
				jointPosition["J2"] = float(split2[0])
		
		split1 = string.split("J3;")
		if (len(split1) > 1) :
			split2 = split1[1].split(";")
			if (len(split2) > 1) :
				jointPosition["J3"] = float(split2[0])

		split1 = string.split("J5;")
		if (len(split1) > 1) :
			split2 = split1[1].split(";")
			if (len(split2) > 1) :
				jointPosition["J5"] = float(split2[0])

		split1 = string.split("J6;")
		if (len(split1) > 1) :
			split2 = split1[1].split(";")
			if (len(split2) > 1) :
				jointPosition["J6"] = float(split2[0])
		
		return jointPosition

	def getCartesianPositionByString(self, string):
		#The cartesian string from robot is like this:
		#QoKX;250.00;Y;0.00;Z;450.00;A;0.00;B;180.00;;6,0;50;0.00;00000000

		elements = string.split(";")

		if (len(elements) == 15 and not "MITSUBISHI" in string and not "Qe" in string) :
			cartesianPosition = {
				"X": float(elements[1]),
				"Y": float(elements[3]),
				"Z": float(elements[5]),
				"A": float(elements[7]),
				"B": float(elements[9]),
			}
		else :
			cartesianPosition = {
				"X": None,
				"Y": None,
				"Z": None,
				"A": None,
				"B": None,
			}
		
		return cartesianPosition