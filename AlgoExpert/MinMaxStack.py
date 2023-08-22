class MinMaxStack:
    def __init__(self):
        self.minMaxStack =[]
        self.stack =[]

    # O(1) time | O(1) space
    def peek(self):
        self.minMaxStack.pop()
        return self.stack.pop()

     # O(1) time | O(1) space
    def push(self, number):
        newMinmax ={"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax =self.minMaxStack[len(self.minMaxStack) -1]
            newMinmax["min"] =min(lastMinMax["min"],number)
            newMinmax["max"] =max(lastMinMax["max"],number)
        self.minMaxStack.append(newMinmax)
        self.stack.append(number)

     # O(1) time | O(1) space
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) -1]["min"]

    # O(1) time | O(1) space
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) -1]["max"]

