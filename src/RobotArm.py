
class RobotArm():

	def init(self):
		commands = []
		commands.append('OPEN=NARCUSR')
        commands.append('PARRLNG')
        commands.append('PDIRTOP')
        commands.append('PPOSF')
        commands.append('PARMEXTL')
        commands.append('KEYWDptest')
        commands.append('SRVON')         
        commands.append('RSTALRM')        
        commands.append('STATE')
        commands.append('CNTLON')
        commands.append('EXECJOVRD 25.0')

    def resetAlarm(self):
    	commands = []
    	commands.append('CNTLOFF')        
        commands.append('RSTALRM')            
        commands.append('SRVON')             
        commands.append('STATE')          
        commands.append('CNTLON')

    def moveToInitialPos(self)
    	commands = []
    	initialPos = '0.000, 0.000, 0.000, 0.000, 0.000, 0.000'
    	commands.append('EXECJCOSIROP = ' + initialPos)
        commands.append('EXECMOV JCOSIROP')

    def moveToPos(self)
    	commands = []
    	initialPos = '20.000, 0.000, 0.000, 0.000, 0.000, 0.000'
    	commands.append('EXECJCOSIROP = ' + initialPos)
        commands.append('EXECMOV JCOSIROP')          



		