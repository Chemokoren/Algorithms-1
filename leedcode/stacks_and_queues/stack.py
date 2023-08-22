class PlateStack:
    def __init__(self):
        self.st =[]

    def push(self, x):
        self.st.append(x)

    def pop(self):
        if(len(self.st)>0):
            self.st.pop()

    def top(self):
        if(len(self.st) == 0):
            return None
        return self.st[-1]

    def getLen(self):
        return len(self.st)

sol = PlateStack()
sol.push(5)
sol.push(3)
sol.push(2)
sol.push(1)
print(sol.st)
sol.pop()
print("sol after popping: ", sol.st)
print("top vaal: ", sol.top())
print("sol after top: ", sol.st)
print("get length of stack: ", sol.getLen())    