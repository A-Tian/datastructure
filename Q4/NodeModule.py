class Node:
    def __init__(self,initdata,position=0):
        self.data = initdata
        self.next = None
        self.position = position

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext