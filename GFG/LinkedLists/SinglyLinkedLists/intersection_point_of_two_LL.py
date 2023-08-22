"""
Method 1(Simply use two loops) 
Use 2 nested for loops. The outer loop will be for each node of the 1st list and inner loop
will be for 2nd list. In the inner loop, check if any of nodes of the 2nd list is same as
the current node of the first linked list. The time complexity of this method will be O(M * N) 
where m and n are the numbers of nodes in two lists.

"""

"""
Method 2 (Mark Visited Nodes) 
This solution requires modifications to basic linked list data structure. Have a visited flag with
each node. Traverse the first linked list and keep marking visited nodes. Now traverse the second
linked list, If you see a visited node again then there is an intersection point, 
return the intersecting node. 
This solution works in O(m+n) but requires additional information with each node. 
A variation of this solution that doesn’t require modification to the basic data structure & 
can be implemented using a hash. Traverse the first linked list and store the addresses of visited
nodes in a hash. Now traverse the second linked list and if you see an address that already exists
in the hash then return the intersecting node.
"""

"""
Method 3- Using difference of node counts

Get count of the nodes in the first list, let count be c1.
Get count of the nodes in the second list, let count be c2.
Get the difference of counts d = abs(c1 – c2)

Now traverse the bigger list from the first node till d nodes so that from here onwards both
the lists have equal no of nodes

Then we can traverse both the lists in parallel till we come across a common node. 

(Note that getting a common node is done by comparing the address of the nodes)

Time Complexity: O(m+n) 
Auxiliary Space: O(1)

"""
# program to get intersection point of two linked list
class Node:
    def __init__(self,d):
        self.data = d
        self.next = None
	
class LinkedList:
    
    def __init__(self):
        self.head1 =Node(None)
        self.head2 =Node(None)

    #function to get the intersection point of two linked lists head1 and head2     
    def getNode(self):
        c1 = self.getCount(self.head1)
        c2 = self.getCount(self.head2)
        d = None

        if (c1 > c2):
            d = c1 - c2
            return self._getIntesectionNode(d, self.head1, self.head2)
        else:
            d = c2 - c1
            return self._getIntesectionNode(d, self.head2, self.head1)
    
    # function to get the intersection point of two linked lists head1 and head2 where head1 has d more nodes than head2
    def _getIntesectionNode(self,d, node1, node2):
        current1 = Node(node1)
        current2 = Node(node2)
        
        for i in range(0,d):
            if (current1 == None):
                return -1
            current1 = current1.next
        
        while (current1 != None and current2 != None):
            if(current1.data == current2.data):
                return current1.data
            current1 = current2
            current2 = current2.next
        return -1

	#Takes head pointer of the linked list and	returns the count of nodes in the list
    def getCount(self,node):
        current = Node(node)
        count = 0
        while(current != None):
            count +=1
            current = current.next
        return count
	

if __name__=='__main__':
    
    # creating first linked list
    list = LinkedList()
    list.head1 =Node(3)
    list.head1.next =Node(6)
    list.head1.next.next =Node(9)
    list.head1.next.next.next = Node(15)
    list.head1.next.next.next.next = Node(30)
    print("list count:",list.getCount(3))

	# creating second linked list
    list.head2 = Node(10)
    list.head2.next = Node(15)
    list.head2.next.next = Node(30)
    print("The node of intersection is ", list.getNode())


"""
Method 4 - Make circle in first list

1. Traverse the first linked list(count the elements) and make a circular linked list.
  (Remember the last node so that we can break the circle later on). 
2. Now view the problem as finding the loop in the second linked list. So the problem is solved. 
3. Since we already know the length of the loop(size of the first linked list) we can traverse 
those many numbers of nodes in the second list, and then start another pointer from the beginning 
of the second list. we have to traverse until they are equal, and that is the required intersection
point. 
4. Remove the circle from the linked list. 

Time Complexity: O(m+n) 
Auxiliary Space: O(1)

"""

"""
Method 5 (Reverse the first list and make equations) 

1) Let X be the length of the first linked list until intersection point.
   Let Y be the length of the second linked list until the intersection point.
   Let Z be the length of the linked list from the intersection point to End of
   the linked list including the intersection node.
   We Have
           X + Z = C1;
           Y + Z = C2;
2) Reverse first linked list.
3) Traverse Second linked list. Let C3 be the length of second list - 1. 
     Now we have
        X + Y = C3
     We have 3 linear equations. By solving them, we get
       X = (C1 + C3 – C2)/2;
       Y = (C2 + C3 – C1)/2;
       Z = (C1 + C2 – C3)/2;
      WE GOT THE INTERSECTION POINT.
4)  Reverse first linked list.
Advantage: No Comparison of pointers. 
Disadvantage : Modifying linked list(Reversing list). 

Time complexity: O(m+n) 
Auxiliary Space: O(1)

"""

"""
Method 6 (Traverse both lists and compare addresses of last nodes)
 This method is only to detect if there is an intersection point or not. 

1) Traverse the list 1, store the last node address
2) Traverse the list 2, store the last node address.
3) If nodes stored in 1 and 2 are same then they are intersecting.
The time complexity of this method is O(m+n) and used Auxiliary space is O(1)
"""


"""
Using Hashing
1) Create an empty hash set. 
2) Traverse the first linked list and insert all nodes’ addresses in the hash set. 
3) Traverse the second list. For every node check if it is present in the hash set. 
If we find a node in the hash set, return the node.

This method required O(n) additional space and not very efficient if one list is large.

"""

#  program to get intersection point of two linked list

class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

class LinkedListIntersect:
    
    #    function to print the list
    def Print(self,n):
        cur = Node(n)
        while(cur != None):
            print(cur.data, end= " ")
            cur = cur.next
        print()
    
    # function to find the intersection of two node
    def MegeNode(self,n1, n2):
        hs = []# # define hashset
        while (n1 != None):
            hs.append(n1)
            n1 = n1.next
        while (n2 != None):
            if (n2 in hs):
                return n2
            n2 = n2.next
        return None

if __name__=='__main__':
    ll = LinkedListIntersect()
    # list 1
    n1 = Node(1)
    n1.next =  Node(2)
    n1.next.next =  Node(3)
    n1.next.next.next =  Node(4)
    n1.next.next.next.next =  Node(5)
    n1.next.next.next.next.next =  Node(6)
    n1.next.next.next.next.next.next = Node(7)
    
    # list 2
    n2 =  Node(10)
    n2.next =  Node(9)
    n2.next.next =  Node(8)
    n2.next.next.next = n1.next.next.next
    ll.Print(n1)
    ll.Print(n2)
    print(ll.MegeNode(n1, n2).data)


"""
Method 8( 2-pointer technique ):

Using Two pointers :

Initialize two pointers ptr1 and ptr2  at the head1 and  head2.
Traverse through the lists,one node at a time.
When ptr1 reaches the end of a list, then redirect it to the head2.
similarly when ptr2 reaches the end of a list, redirect it the head1.
Once both of them go through reassigning,hey will be equidistant from
 the collision point
If at any node ptr1 meets ptr2, then it is the intersection node.
After second iteration if there is no intersection node it returns NULL.

Time complexity : O( m + n ) 
Auxiliary Space:  O(1)
"""

# Python3 program to print intersection of lists

# Link list node
class Node:
	def __init__(self, data = 0, next = None):
		self.data = data
		self.next = next

# A utility function to return intersection node
def intersectPoint(head1, head2):

	# Maintaining two pointers ptr1 and ptr2
	# at the head of A and B,
	ptr1 = head1
	ptr2 = head2

	# If any one of head is None i.e
	# no Intersection Point
	if (ptr1 == None or ptr2 == None):
		return None

	# Traverse through the lists until they
	# reach Intersection node
	while (ptr1 != ptr2):

		ptr1 = ptr1.next
		ptr2 = ptr2.next

	# If at any node ptr1 meets ptr2, then it is
	# intersection node.Return intersection node.
		if (ptr1 == ptr2):
			return ptr1

		# Once both of them go through reassigning,
		# they will be equidistant from the collision point.

		# When ptr1 reaches the end of a list, then
		# reassign it to the head2.
		if (ptr1 == None):
			ptr1 = head2

		# When ptr2 reaches the end of a list, then
		# redirect it to the head1.
		if (ptr2 == None):
			ptr2 = head1

	return ptr1

# Function to print intersection nodes
# in a given linked list
def Print(node):

	if (node == None):
		print("None")
	while (node.next != None):
		print(node.data,end="->")
		node = node.next
	print(node.data)

# Driver code

# Create two linked lists

# 1st Linked list is 3->6->9->15->30
# 2nd Linked list is 10->15->30

# 15 30 are elements in the intersection list

head1 = Node()
head1.data = 10
head2 = Node()
head2.data = 3
newNode = Node()
newNode.data = 6
head2.next = newNode
newNode = Node()
newNode.data = 9
head2.next.next = newNode
newNode = Node()
newNode.data = 15
head1.next = newNode
head2.next.next.next = newNode
newNode = Node()
newNode.data = 30
head1.next.next = newNode
head1.next.next.next = None
intersect_node = None

# Find the intersection node of two linked lists
intersect_node = intersectPoint(head1, head2)

print("INTERSEPOINT LIST :",end="")

Print(intersect_node)
