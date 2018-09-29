import Communication

comn = Communication.Communication('/dev/ttyS0')

list = []
list.append('CNTLON')
list.append('SRVOFF')
list.append('CNTLOFF')

comn.send(list)
