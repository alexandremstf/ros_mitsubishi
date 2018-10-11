class StringHandler :

	def __init__(self) :
		print 'ok'

	def jointPositionStringConstructor(self, j1, j2, j3, j4, j5) :
		
		j1String = str(j1)
		j2String = str(j2)
		j3String = str(j3)
		j4String = str(j4)
		j5String = str(j5)

		jointPosition = '(' + j1String + ', ' + j2String + ', ' + j3String + ', ' + j4String + ', ' + j5String + ')' 
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
