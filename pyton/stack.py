class Stack():
    def __init__(self):
        self.__array = []
        self.__length = 0
    def push(self, elem):
        self.__array.append(elem)
        self.__length+=1
    def getTop(self):
        return self.__array[-1]
    def pop(self):
        self.__array.pop(-1)
        self.__length-=1
    @property
    def length(self):
        return self.__length
    @property
    def array(self):
        return self.__array
