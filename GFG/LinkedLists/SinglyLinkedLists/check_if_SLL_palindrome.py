
"""
Function to check if a singly linked list is palindrome

Given a singly linked list of characters, write a function that returns true if the 
given list is a palindrome, else false.

R -> A -> D -> A -> R

METHOD 1: Use a Stack
A simple solution is to use a stack of list nodes. This mainly involves three steps:
- Traverse the given list from head to tail and push every visited node to stack.
- Traverse the list again. For every visited node, pop a node from the stack and compare
data of popped node with currently visited node.
- If all nodes matched, then return true, else false

"""
# program to check if SLL is palindrome using stack
# Time complexity: O(n).
class Node:
    def __init__(self, data):
        self.data =data
        self.next =None

# Function to check if LL is palindrome or not
def ispalindrome(head):
    # temp pointer
    slow =head

    stack =[]

    ispalin =True

    # push all elements of the list to the stack
    while slow !=None:
        stack.append(slow.data)

        #move ahead
        slow =slow.next

    # Iterate in the list again and check by popping from the stack
    while head != None:
        # Get the top most element
        i =stack.pop()

        # check if data is not same as popped element
        if(head.data == i):
            ispalin =True
        else:
            ispalin =False

        # move ahead
        head =head.next

    return ispalin


# Addition of linked list
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)

# Initialize the next pointer of every current pointer
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = None

# Call function to check palindrome or not
result = ispalindrome(one)

print("isPalindrome:", result)



"""
Method 2: reversing the list

This method takes O(n) time and O(1) space

- get the middle of the LL
- reverse the second half of the LL
- check if the first half and second half are identical
- construct the original LL by reversing the second half again 
    and attaching it back to the first half

Time Complexity: O(n) 
Auxiliary Space: O(1)  
"""

class LinkedList2:

    def __init__(self):
        self.head =None

    # Function to check if given LL is pallindrome or not
    def isPalindrome(self, head):

        slow_ptr = head
        fast_ptr = head
        prev_of_slow_ptr = head

        # To handle odd size list
        midnode = None

        # Initialize result
        res = True

        if (head != None and head.next != None):

            # Get the middle of the list & Move slow_ptr by 1 & fast_ptr by 2,
            # slow_ptr will have the middle node
            while (fast_ptr != None and
                   fast_ptr.next != None):
                # We need previous of the slow_ptr
                # for linked lists  with odd
                # elements
                fast_ptr = fast_ptr.next.next
                prev_of_slow_ptr = slow_ptr
                slow_ptr = slow_ptr.next

            # fast_ptr would become NULL when there are even elements in the
            # list and not NULL for odd elements.
            # We need to skip the middle node for odd case and store it somewhere so
            # that we can restore the original list
            if (fast_ptr != None):
                midnode = slow_ptr
                slow_ptr = slow_ptr.next

            # Now reverse the second half and compare it with first half
            second_half = slow_ptr

            # NULL terminate first half
            prev_of_slow_ptr.next = None

            # Reverse the second half
            second_half = self.reverse(second_half)

            # Compare
            res = self.compareLists(head, second_half)

            # Construct the original list back & Reverse the second half again
            second_half = self.reverse(second_half)

            if (midnode != None):

                # If there was a mid node (odd size # case) which was not part of either
                # first half or second half.
                prev_of_slow_ptr.next = midnode
                midnode.next = second_half
            else:
                prev_of_slow_ptr.next = second_half
        return res

    # Function to reverse the LL(this function may change the head)
    def reverse(self, second_half):

        prev = None
        current = second_half
        next = None

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        second_half = prev
        return second_half

        # Function to check if two input
        # lists have same data
    def compareLists(self, head1, head2):

        temp1 = head1
        temp2 = head2

        while (temp1 and temp2):
            if (temp1.data == temp2.data):
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return 0

        # Both are empty return 1
        if (temp1 == None and temp2 == None):
            return 1

        # Will reach here when one is NULL
        # and other is not
        return 0

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node =Node(new_data)
        new_node.next =self.head
        self.head =new_node

    def printList(self):
        temp =self.head
        while(temp):
            print(temp.data, end="->")
            temp =temp.next
        print("NULL")


if __name__ == '__main__':

    l = LinkedList2()
    s = ['a', 'b', 'a', 'c', 'a', 'b', 'a']

    for i in range(7):
        l.push(s[i])
        l.printList()

        if (l.isPalindrome(l.head) != False):
            print("Is Palindrome\n")
        else:
            print("Not Palindrome\n")
        print()


    """
    Method 3 - Using Recursion
    
    use two pointers left and right. Move right and left using recursion 
    and check for the following in each recursive call
    - sub-list is palindrome
    - value at current left and right are matching
    
    if both conditions(above) are true, return true.
    
    Time Complexity: O(n) 
Auxiliary Space: O(n) if Function Call Stack size is considered, otherwise O(1).
    """

# class Node:
#     self.data =None
#     self.next =None
#
#     # Linked list node
#     def __init__(self, d):
#         data = d
#         next = null
#
#
# class LinkedList:
#
#     # Head of the list
#     self.head =None
#     self.left =None
#
#         # Initial parameters to this function are
#         # & head and head
#     def isPalindromeUtil(Node right):
#             left = head;
#
#         # Stop recursion when right becomes null
#         if (right == null)
#             return true;
#
#         # If sub - list is not palindrome  then  no need to
#         # check for the current left and right, return false
#         boolean isp = isPalindromeUtil(right.next);
#         if (isp == false):
#             return false
#
#         # Check values at current left and rightboolean
#         isp1 = (right.data == left.data);
#
#         left = left.next;
#
#         # Move left to next node;
#         return isp1
#
#     # A wrapper over isPalindrome(Node head)
#     def isPalindrome(Node head):
#         result = isPalindromeUtil(head)
#         return result
#
#     # Push a node to linked list.Note that
#     # this function changes the head
#     def push(char new_data):
#         # Allocate the node and put in the data Node
#         new_node = new
#         Node(new_data)
#
#         # Link the old list off the the new one
#         new_node.next = head;
#
#         # Move the head to point to new node
#         head = new_node;
#
#
#     # A utility function to print a
#     # given linked list
#     void printList(Node ptr)
#     {
#     while (ptr != null)
#         {
#             System.out.print(ptr.data + "->");
#         ptr = ptr.next;
#         }
#         System.out.println("Null");
#         }
#
#         # Driver Code
# if __name__=='__main__':
#     llist =LinkedList()
#     char[]
#     str = {'a', 'b', 'a', 'c', 'a', 'b', 'a'}
#     for i  in range(0, 7):
#             llist.push(str[i]);
#         llist.printList(llist.head);
#
#         if (llist.isPalindrome(llist.head)):
#             print("Is Palindrome")
#             print("")
#         else:
#             print("Not Palindrome")
#             print("")
#
#
#
#
#
#
#
#
#
#
#
