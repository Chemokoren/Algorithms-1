# Python implementtion to count triplets
# in a sorted doubly linked list
# whose sum is equal to a given value 'x'

# srtructure of node of a doubly linked list
class Node:
    def __init__(self):
        self.data =None
        self.prev =None
        self.next =None



# A utility function to insert a new node at the
# beginning of doubly linked list
def insert(head, data):

    # allocate node
    temp =Node(data)
    if((head) == None):
        (head) = temp
    else:
        temp.next =head
        (head).prev =temp
        (head) =temp
    return head

# function to count triplets in a sorted doubly linked list
# whose sum is equal to a given value 'x'
def countTriplets(head, x):
    ptr1 =head
    ptr2 =None
    ptr3 =None
    count =0

    # generate all possible triplets
    while (ptr1 != None):
        ptr2 =ptr1.next
        while(ptr2 !=None):
            ptr3 =ptr2.next
            while(ptr3 !=None):

                # if elements in the current triplet sum up to 'x'
                if ((ptr1.data +ptr2.data +ptr3.data) ==x):

                    # increment count
                    count = count + 1
                ptr3 =ptr3.next
            ptr2 =ptr2.next
        ptr1 =ptr1.next

    #required count of triplets
    return count

# utility function to insert a new node at the
# beginning of a doubly linked list
def insert(head, data):
    # allocate node
    temp =Node()

    # put in the data
    temp.data =data
    temp.next =temp.prev =None

    if((head) == None):
        (head) =temp
    else:
        temp.next =head
        (head).prev =temp
        (head) =temp
    return head


# Driver code

# start with an empty doubly linked list
head =None

# insert values in sorted order
head =insert(head,9)
head =insert(head,8)
head =insert(head,6)
head =insert(head,5)
head =insert(head,4)
head =insert(head,2)
head =insert(head,1)

x = 17
print("Count =", countTriplets(head, x))

print(" ######################################## approach 2 #############################")
#Approach 2
# implementation to count triplets in a sorted doubly linked list
# whose sum is equal to a given value 'x'

# function to count triplets in a sorted doubly linked list
# who sum is equal to a given value 'x'
def countTriplets2(head, x):
    ptr2 =head
    count =0

    # unordered_map 'um' implemented as hash table
    um =dict()

    ptr =head
    # insert the <node data, node pointer> tuple in 'um'
    while ptr !=None:
        um[ptr.data] =ptr
        ptr =ptr.next

    # generate all possible pairs
    ptr1 =head

    while ptr1!=None:
        ptr2 =ptr1.next

        while ptr2!=None:
            # p_sum -sum of elements in the current pair
            p_sum =ptr1.data + ptr2.data
            # if 'x-p_sum' is present in 'um' and either of the two nodes
            # not equal to the 'um[x-p_sum]' node
            if((x-p_sum) in um) and um[x -p_sum] != ptr1 and um[x -p_sum] !=ptr2:
                # increment count
                count +=1
            ptr2 =ptr2.next
        ptr1 =ptr1.next

    #required count of triplets
    # division by 3 as each triplet is counted 3 times
    return (count // 3)



# Driver program to test above
if __name__=='__main__':
    # start with an empty doubly linked list
    head =None

    head =insert(head, 9)
    head =insert(head, 8)
    head =insert(head, 6)
    head =insert(head, 5)
    head =insert(head, 4)
    head =insert(head, 2)
    head =insert(head, 1)

    x =17

    print("Count ="+ str(countTriplets(head, x)))

print(" ######################################## approach 3 #############################")

# Function to count pairs whose sum
# equal to given 'value'
def countPairs(first, second, value):

	count = 0

	# The loop terminates when either of two pointers
	# become None, or they cross each other (second.next
	# == first), or they become same (first == second)
	while (first != None and second != None and
		first != second and second.next != first):

		# Pair found
		if ((first.data + second.data) == value):

			# Increment count
			count += 1

			# Move first in forward direction
			first = first.next

			# Move second in backward direction
			second = second.prev

		# If sum is greater than 'value'
		# move second in backward direction
		elif ((first.data + second.data) > value):
			second = second.prev

		# Else move first in forward direction
		else:
			first = first.next

	# Required count of pairs
	return count

# Function to count triplets in a sorted
# doubly linked list whose sum is equal
# to a given value 'x'
def countTriplets(head, x):

	# If list is empty
	if (head == None):
		return 0

	current, first, last = head, None, None
	count = 0

	# Get pointer to the last node of
	# the doubly linked list
	last = head

	while (last.next != None):
		last = last.next

	# Traversing the doubly linked list
	while current != None:

		# For each current node
		first = current.next

		# count pairs with sum(x - current.data) in
		# the range first to last and add it to the
		# 'count' of triplets
		count, current = count + countPairs(
			first, last, x - current.data), current.next

	# Required count of triplets
	return count



# Driver code
if __name__ == '__main__':

	# Start with an empty doubly linked list
	head = None

	# Insert values in sorted order
	head = insert(head, 9)
	head = insert(head, 8)
	head = insert(head, 6)
	head = insert(head, 5)
	head = insert(head, 4)
	head = insert(head, 2)
	head = insert(head, 1)

	x = 17

	print("Count = ", countTriplets(head, x))

# This code is contributed by mohit kumar 29


