"""
How to implement deque Using circular array
Circular array implementation deque
For implementing deque, we need to keep track of two indices, front and rear.
We enqueue(push) an item at the rear or the front end of queue and dequeue(pop) an item
from both rear and front end.

1. Create an empty array ‘arr’ of size ‘n’
initialize front = -1 , rear = 0
Inserting First element in deque, at either front or rear will lead to the same result.

After insert Front Points = 0 and Rear points = 0
Insert Elements at Rear end

a). First we check deque if Full or Not
b). IF Rear == Size-1
       then reinitialize Rear = 0 ;
    Else increment Rear by '1'
    and push current key into Arr[ rear ] = key
Front remain same.

Insert Elements at Front end

a). First we check deque if Full or Not
b). IF Front == 0 || initial position, move Front
                     to points last index of array
       front = size - 1
    Else decremented front by '1' and push
         current key into Arr[ Front] = key
Rear remain same.

Delete Element From Rear end


a). first Check deque is Empty or Not
b).  If deque has only one element
        front = -1 ; rear =-1 ;
    Else IF Rear points to the first index of array
         it's means we have to move rear to points
         last index [ now first inserted element at
         front end become rear end ]
            rear = size-1 ;
    Else || decrease rear by '1'
            rear = rear-1;

Delete Element From Front end


a). first Check deque is Empty or Not
b).  If deque has only one element
            front = -1 ; rear =-1 ;
    Else IF front points to the last index of the array
         it's means we have no more elements in array so
          we move front to points first index of array
            front = 0 ;
    Else || increment Front by '1'
            front = front+1;
"""

# implementation of De - queue using circular array
# A structure to represent a Deque

class Deque
    {
    static final int MAX = 100;
    int arr[];
    int front;
    int rear;
    int size;

    public Deque(int size)
    {
    arr = new int[MAX];
    front = -1;
    rear = 0;
    this.size = size;
    }

  """
 Operations on  Deque:
    void insertfront(int key)
    void insertrear(int key)
    void deletefront()
    void deleterear()
    bool isFull()
    bool isEmpty()
    int getFront()
    int getRear()
  """

   # Checks whether Deque is full or not.
    def isFull():
     return ((front == 0 & & rear == size - 1) | | front == rear + 1)


    # Checks whether Deque is empty or not.
    def isEmpty():
        return (front == -1);


    # Inserts an element at front
    def insertfront(key):
        # check whether Deque if full or not
        if (isFull()):
            System.out.println("Overflow")
        return


    # If queue is initially empty
    if (front == -1):
        front = 0
        rear = 0


    # front is at first position of queue
    elif (front == 0):
        front = size - 1

    else: # decrement front end by '1'
        front = front-1

    # insert current element into Deque
    arr[front] = key

#  function to inset element at rear end of Deque.
def insertrear( key):
    if (isFull()):
        System.out.println(" Overflow ")
    return


    # If queue is initially empty
    if (front == -1):
        front = 0
        rear = 0;

    # rear is at last position of queue
    elif (rear == size - 1):
        rear = 0

    # increment rear end by '1'
    else:
        rear = rear+1

    # insert current element into Deque
    arr[rear] = key


# Deletes element at front end of Deque
def deletefront():
    # check whether Deque is empty or not
    if (isEmpty()):
        System.out.println("Queue Underflow\n");
        return
    #  Deque has only one element
    if (front == rear):
        front = -1
        rear = -1
    else:
        # back to initial  position
        if (front == size - 1):
            front = 0
        else:
            # increment front by  '1' to remove current # front value from Deque
            front = front + 1

# Delete element at rear end of Deque void
def deleterear():
    if (isEmpty()):
        print(" Underflow")
        return
    # Deque has only one element
    if (front == rear):
        front = -1
        rear = -1
    elif (rear == 0):
        rear = size-1
    else:
        rear = rear-1


#  Returns front element of Deque
def getFront():
    # check whether Deque is empty or not
    if (isEmpty()):
        print(" Underflow")
        return -1
    return arr[front]


# function return rear element of Deque int
def getRear():
    # check whether Deque is empty or not
    if (isEmpty() or rear < 0):
        print(" Underflow\n")
        return -1

    return arr[rear]


# Driver program to test above function

if __name__=='__main__':
    dq = Deque(5)
    print("Insert element at rear end : 5 ")
    dq.insertrear(5)

    print("insert element at rear end : 10 ")
    dq.insertrear(10)

    print("get rear element : " + dq.getRear())

    dq.deleterear()
    print("After delete rear element new rear become : " +dq.getRear())

    print("inserting element at front end")
    dq.insertfront(15)

    print("get front element: " + dq.getFront())

    dq.deletefront()

    print("After delete front element new front become : " + dq.getFront())
