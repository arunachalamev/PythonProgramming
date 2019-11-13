class ecommerceLogs:
    def __init__(self, logSize):
        self.logArray = list()
        self.size = logSize

    def addRecords(self, order_id):
        self.logArray.append(order_id)
        if len(self.logArray) > self.size:
            self.logArray = self.logArray[1:]
    
    def getLast(self,index):
        return self.logArray[-index]



log = ecommerceLogs(4)
log.addRecords(1)
log.addRecords(2)
assert log.logArray == [1,2]
log.addRecords(3)
log.addRecords(4)
assert log.logArray == [1,2,3,4]
log.addRecords(5)
assert log.logArray == [2,3,4,5]
assert log.getLast(2) == 4
