"""
Min Max Stack Construction
"""
class MinMaxStack:
    def __init__(self) -> None:
        self.minMaxStack =[]
        self.stack =[]

    # O(1) time | O(1) space
    def peek(self):
        return self.stack[len(self.stack)-1]

    # O(1) time | O(1) space
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    # O(1) time | O(1) space
    def push(self, number):
        newMinMax ={"min":number, "max":number}
        if(len(self.minMaxStack)):
            lastMinMax = self.minMaxStack[len(self.minMaxStack)- 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    # O(1) time | O(1) space
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) -1]["min"]

    # O(1) time | O(1) space
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) -1]["max"]
    
sol = MinMaxStack()
sol.push(5)
print("min val: ",sol.getMin())
print("min val: ",sol.getMax())
sol.push(7)
print("after pushing 7: \n")
print("min val: ",sol.getMin())
print("min val: ",sol.getMax())
sol.push(2)
print("after pushing 2: \n")
print("min val: ",sol.getMin())
print("min val: ",sol.getMax())