"""
How to implement deque Using circular array

Circular array implementation deque

For implementing deque, we need to keep track of two indices, front and rear.
We enqueue(push) an item at the rear or the front end of queue and dequeue(pop) an item
from both rear and front end.

- create an empty array ‘arr’ of size ‘n’
- initialize front = -1 , rear = 0
- inserting First element in deque, at either front or rear will lead to the same result.

After insert Front Points = 0 and Rear points = 0

Insert Elements at Rear end
----------------------------
a). First we check deque if Full or Not
b). IF Rear == Size-1
       then reinitialize Rear = 0 ;
    Else:
         increment Rear by '1'
         and push current key into Arr[ rear ] = key
Front remain same.

Insert Elements at Front end
----------------------------

a). First we check deque if Full or Not
b). IF Front == 0 or initial position:
       move Front to point to last index of array
       front = size - 1
    Else:
         decremented front by '1' and push
         current key into Arr[ Front] = key
Rear remain same.

Delete Element From Rear end
----------------------------

a). first Check deque is Empty or Not
b). If deque has only one element
        front = -1 ; rear =-1 ;
    Elif (Rear points to the first index of array):
          -it means we have to move rear to point to last index 
          [ now first inserted element at front end become rear end ]
          rear = size-1 ;
    Else:
        decrease rear by '1'
        rear = rear-1;

Delete Element From Front end
-----------------------------

a). first Check deque is Empty or Not
b).  If deque has only one element
            front = -1 ; rear =-1 ;
    Elif front points to the last index of the array
        it means we have no more elements in array so
        we move front to point to first index of array
        front = 0
    Else:
        increment Front by '1'
        front = front+1;


Operations on Deque: 

    Mainly the following four basic operations are performed on queue: 

        insertFront(): Adds an item at the front of Deque.
        insertRear(): Adds an item at the rear of Deque. 
        deleteFront(): Deletes an item from front of Deque. 
        deleteRear(): Deletes an item from rear of Deque.

    In addition to above operations, following operations are also supported 

        getFront(): Gets the front item from queue. 
        getRear(): Gets the last item from queue. 
        isEmpty(): Checks whether Deque is empty or not. 
        isFull(): Checks whether Deque is full or not. 
         

 
"""

# implementation of De - queue using circular array
# Time Complexity: O(N) | Auxiliary Space: O(N)
MAX = 100
class Deque(object):
    
 
    def __init__(self,size) -> None:
        self.arr    = [0]* MAX
        self.front  = -1
        self.rear   = 0
        self.size   = size


   # Checks whether Deque is full or not.
    def isFull(self):
     return ((self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1))


    # Checks whether Deque is empty or not.
    def isEmpty(self):
        return (self.front == -1)

    # Inserts an element at front
    def insertfront(self, key):
        # check whether Deque if full or not
        if (self.isFull()):
            print("Overflow")
            return

        # If queue is initially empty
        if (self.front == -1):
            self.front = 0
            self.rear = 0

        # front is at first position of queue
        elif (self.front == 0):
            self.front = self.size - 1

        else: # decrement front end by '1'
            self.front = self.front-1

        # insert current element into Deque
        self.arr[self.front] = key

    #  function to inset element at rear end of Deque.
    def insertrear(self, key):
        if (self.isFull()):
            print(" Overflow ")
            return
        # If queue is initially empty
        if (self.front == -1):
            self.front = 0
            self.rear  = 0

        # rear is at last position of queue
        elif (self.rear == self.size - 1):
            self.rear = 0

        # increment rear end by '1'
        else:
            self.rear = self.rear+1

        # insert current element into Deque
        self.arr[self.rear] = key


    # Deletes element at front end of Deque
    def deletefront(self):
        # check whether Deque is empty or not
        if (self.isEmpty()):
            print("Queue Underflow\n")
            return
        #  Deque has only one element
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            # back to initial  position
            if (self.front == self.size - 1):
                self.front = 0
            else:
                # increment front by  '1' to remove current # front value from Deque
                self.front = self.front + 1

    # Delete element at rear end of Deque void
    def deleterear(self):
        if (self.isEmpty()):
            print("Underflow")
            return
        # Deque has only one element
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        elif (self.rear == 0):
            self.rear = self.size-1
        else:
            self.rear = self.rear-1


    #  Returns front element of Deque
    def getFront(self):
        # check whether Deque is empty or not
        if (self.isEmpty()):
            print(" Underflow")
            return -1
        return self.arr[self.front]


    # function return rear element of Deque int
    def getRear(self):
        # check whether Deque is empty or not
        if (self.isEmpty() or self.rear < 0):
            print(" Underflow\n")
            return -1

        return self.arr[self.rear]



if __name__=='__main__':
    dq = Deque(5)
    print("Insert element at rear end : 5 ")
    dq.insertrear(5)

    print("insert element at rear end : 10 ")
    dq.insertrear(10)

    print("get rear element : ",  dq.getRear())

    dq.deleterear()
    print("After delete rear element new rear become : " , dq.getRear())

    print("inserting element at front end")
    dq.insertfront(15)

    print("get front element: ",  dq.getFront())

    dq.deletefront()

    print("After delete front element new front become : " ,  dq.getFront())
