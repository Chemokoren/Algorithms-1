class QueueLine:
    def __init__(self) -> None:
        self.q =[]

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if(len(self.q) > 0):
            self.q.pop(0)

    def front(self):
        if(len(self.q)== 0):
            return None
        return self.q[0]


sol = QueueLine()
sol.enqueue(1)
sol.enqueue(2)
sol.enqueue(3)
sol.enqueue(4)
sol.enqueue(5)
print(sol.q)
print(" front of the queue: ",sol.front())
print("sol before dequeue", sol.q)
sol.dequeue()
print("sol after dequeue: ",sol.q)



