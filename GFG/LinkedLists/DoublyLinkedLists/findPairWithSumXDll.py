# program to find a pair with given sum x.


# structure of node of doubly linked list
class Node:
    def __init__(self,x):
        self.data =x
        self.next =None
        self.prev =None

# Function to find pair whose sum
# equal to given value x
def pairSum(head, x):
    # set two pointers, first to the
    # beginning of the DLL and second to the end of DLL.
    first =head
    second =head

    while(second.next != None):
        second =second.next

    # To track if we find a pair or not
    found =False

    # The loop terminates when either of
    # the two pointers become None, or they
    # cross each other (second.next == first), or
    # they become same (first == second)
    while (first != None and second !=None and
           first != second  and second.next !=first):
        # Pair found
        if((first.data +second.data) == x):
            found =True
            print("(", first.data, ",",
                  second.data, ")")
            # move first in forward direction
            first =first.next

            # Move second in backward direction
            second =second.prev

        else:
            if ((first.data + second.data) < x ):
                first =first.next
            else:
                second =second.prev

    # if pair is not present
    if (found ==False):
        print("No pair found")


# A utility function to insert a new node
# at the beginning of a doubly linked list
def insert(head, data):
    temp =Node(data)

    if not head:
        head =temp
    else:
        temp.next =head
        head.prev =temp
        head =temp

    return head

# Driver code for the program
if __name__ =='__main__':
    head =None
    head =insert(head,9)
    head =insert(head,8)
    head =insert(head,6)
    head =insert(head,5)
    head =insert(head,4)
    head =insert(head,3)
    head =insert(head,2)
    head =insert(head,1)

    x =7

    pairSum(head, x)

