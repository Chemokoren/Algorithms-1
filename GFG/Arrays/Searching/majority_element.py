"""
Majority Element

Find the majority element in the array. A majority element in an array A[] of size n is an element
that appears more than n/2 times and hence there is at most one such element.

    Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
    Output : 4
    Explanation: The frequency of 4 is 5 which is greater than the half of the size of the 
    array size. 

    Input : {3, 3, 4, 2, 4, 4, 2, 4}
    Output : No Majority Element
    Explanation: There is no element whose frequency is greater than the half of the size of
    the array size.

Naive Approach: 

    The basic solution is to have two loops and keep track of the maximum count for all different
     elements. If the maximum count becomes greater than n/2 then break the loops and return the 
     element having the maximum count. If the maximum count doesn’t become more than n/2 then the 
     majority element doesn’t exist.

Illustration:

    arr[] = {3, 4, 3, 2, 4, 4, 4, 4}, n = 8

    For i = 0:

        count = 0
        Loop over the array, whenever an element is equal to arr[i] (is 3), increment count
        count of arr[i] is 2, which is less than n/2, hence it can’t be majority element.

    For i = 1:

        count = 0
        Loop over the array, whenever an element is equal to arr[i] (is 4), increment count
        count of arr[i] is 5, which is greater than n/2 (i.e 4), hence it will be majority element.

    Hence, 4 is the majority element.

Follow the steps below to solve the given problem:

    Create a variable to store the max count, count = 0
    Traverse through the array from start to end.
    For every element in the array run another loop to find the count of similar elements in the
     given array.
    If the count is greater than the max count update the max count and store the index in another
     variable.
    If the maximum count is greater than half the size of the array, print the element. Else print
     there is no majority element.

Time Complexity: O(n*n), A nested loop is needed where both the loops traverse the array 
from start to end.
Auxiliary Space: O(1), No extra space is required.
"""
def find_majority(arr):

    n = len(arr)
    max_count = 0
    index = -1 # sentinels

    for i in range(n):

        count = 0
        for j in range(n):
            if(arr[i] == arr[j]):
                count +=1
        
        # update max_count if count of current element is greater
        if(count > max_count):
            max_count = count
            index = i
    # if max_count is greater than n/2
    # return the corresponding element
    if(max_count > n // 2):
        print(arr[index])
    else:
        print("No Majority Element")

    
 
find_majority([1, 1, 2, 1, 3, 5, 1])



""""
Majority Element using Binary Search Tree

Insert elements in BST one by one and if an element is already present then increment the count of
the node. At any stage, if the count of a node becomes more than n/2 then return.

Illustration:

Follow the steps below to solve the given problem:

    Create a binary search tree, if the same element is entered in the binary search tree the
    frequency of the node is increased.
    traverse the array and insert the element in the binary search tree.
    If the maximum frequency of any node is greater than half the size of the array, 
    then perform an inorder traversal and find the node with a frequency greater than half
    Else print No majority Element.

Time Complexity: If a Binary Search Tree is used then time complexity will be O(n²). 
If a self-balancing-binary-search tree is used then it will be O(nlogn)
Auxiliary Space: O(n), As extra space is needed to store the array in the tree.

"""

# class for creating node
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.count = 1 # count of times data is inserted


# class for binary search tree - it initializes tree with None root
# insert function inserts node as per BST rule and also checks for majority element. If no 
# majority is found yet, it returns None
class BST():
    def __init__(self) -> None:
        self.root = None

    def insert(self, data, n):
        out = None
        if(self.root == None):
            self.root = Node(data)
        else:
            out = self.insert_node(self.root, data, n)
        return out
    
    def insert_node(self, current_node, key, n):
        if(current_node.data == key):
            current_node.count +=1
            if(current_node.count > n //2):
                return current_node.data
            else:
                return None
        elif (current_node.data < key):
            if(current_node.right):
                self.insert_node(current_node.right, key, n)
            else:
                current_node.right =Node(key)

        elif(current_node.data > key):
            if(current_node.left):
                self.insert_node(current_node.left, key, n)
            else:
                current_node.left = Node(key)
        
arr = [3, 2, 3]
n = len(arr)
 
# declaring None tree
tree = BST()
flag = 0
for i in range(n):
    out = tree.insert(arr[i], n)
    if (out != None):
        print(arr[i])
        flag = 1
        break
if (flag == 0):
    print("No Majority Element")


"""
Majority Element Using Moore’s Voting Algorithm:

    This is a two-step process:

        The first step gives the element that may be the majority element in the array. 
        If there is a majority element in an array, then this step will definitely return majority
        element, otherwise, it will return candidate for majority element.
        Check if the element obtained from the above step is the majority element. This step is 
        necessary as there might be no majority element. 


Illustration:

    arr[] = {3, 4, 3, 2, 4, 4, 4, 4}, n = 8

    maj_index = 0, count = 1

    At i = 1: arr[maj_index] != arr[i]

        count = count – 1 = 1 – 1 = 0
        now count == 0 then:
            maj_index = i = 1
            count = count + 1 = 0 + 1 = 1

    At i = 2: arr[maj_index] != arr[i]

        count = count – 1 = 1 – 1 = 0
        now count == 0 then:
            maj_index = i = 2
            count = count + 1 = 0 + 1 = 1

    At i = 3: arr[maj_index] != arr[i]

        count = count – 1 = 1 – 1 = 0
        now count == 0 then:
            maj_index = i = 3
            count = count + 1 = 0 + 1 = 1

    At i = 4: arr[maj_index] != arr[i]

        count = count – 1 = 1 – 1 = 0
        now count == 0 then:
            maj_index = i = 4
            count = count + 1 = 0 + 1 = 1

    At i = 5: arr[maj_index] == arr[i]

        count = count + 1 = 1 + 1 = 2

    At i = 6: arr[maj_index] == arr[i]

        count = count + 1 = 2 + 1 = 3

    At i = 7: arr[maj_index] == arr[i]

        count = count + 1 = 3 + 1 = 4

    Therefore, the arr[maj_index] may be the possible candidate for majority element.

    Now, Again traverse the array and check whether arr[maj_index] is the majority element or not.

    arr[maj_index] is 4

    4 occurs 5 times in the array therefore 4 is our majority element.

Follow the steps below to solve the given problem:

    Loop through each element and maintains a count of the majority element, and a majority index,
    maj_index
    If the next element is the same then increment the count if the next element is not the same 
    then decrement the count.
    if the count reaches 0 then change the maj_index to the current element and set the count 
    again to 1.
    Now again traverse through the array and find the count of the majority element found.
    If the count is greater than half the size of the array, print the element
    Else print that there is no majority element

Time Complexity: O(n), As two traversal of the array, is needed, so the time complexity is linear.
Auxiliary Space: O(1), As no extra space is required.

"""

# finding majority element in an array
def find_candidate(A):
    maj_index = 0
    count = 1
    for i in range(len(A)):
        if A[maj_index] == A[i]:
            count +=1
        else:
            count -=1
        if count == 0:
            maj_index = i
            count =1
    return A[maj_index]

def is_majority(A, cand):
    count = 0
    for i in range(len(A)):
        if A[i] == cand:
            count +=1
    if count > len(A) /2:
        return True
    else: 
        return False

def print_majority_two(A):
    # Find the candidate for Majority
    cand = find_candidate(A)
 
    # Print the candidate if it is Majority
    if is_majority(A, cand) == True:
        print(cand)
    else:
        print("No Majority Element")


print_majority_two([1, 3, 3, 1, 2])

"""
Majority Element Using Sorting:

    The idea is to sort the array. Sorting makes similar elements in the array adjacent, 
    so traverse the array and update the count until the present element is similar to the 
    previous one. If the frequency is more than half the size of the array, print the majority
    element.

Illustration:

    arr[] = {3, 4, 3, 2, 4, 4, 4, 4}, n = 8

    Array after sorting => arr[] = {2, 3, 3, 4, 4, 4, 4, 4}, count = 1

    At i = 1:

        arr[i] != arr[i – 1] => arr[1] != arr[0]
        count is not greater than n/2, therefore reinitialise count with, count = 1

    At i = 2:

        arr[i] == arr[i – 1] => arr[2] == arr[1] = 3
        count = count + 1 = 1 + 1 = 2

    At i = 3

        arr[i] != arr[i – 1] => arr[3] != arr[2]
        count is not greater than n/2, therefore reinitialise count with, count = 1

    At i = 4

        arr[i] == arr[i – 1] => arr[4] == arr[3] = 4
        count = count + 1 = 1 + 1 = 2

    At i = 5

        arr[i] == arr[i – 1] => arr[5] == arr[4] = 4
        count = count + 1 = 2 + 1 = 3

    At i = 6

        arr[i] == arr[i – 1] => arr[6] == arr[5] = 4
        count = count + 1 = 3 + 1 = 4

    At i = 7

        arr[i] == arr[i – 1] => arr[7] == arr[6] = 4
        count = count + 1 = 4 + 1 = 5
        Therefore, the count of 4 is now greater than n/2.

    Hence, 4 is the majority element.

Follow the steps below to solve the given problem:

    Sort the array and create a variable count and previous, prev = INT_MIN.
    Traverse the element from start to end.
    If the current element is equal to the previous element increase the count.
    Else set the count to 1.
    If the count is greater than half the size of the array, print the element as the majority element and break.
    If no majority element is found, print “No majority element”

Time Complexity: O(nlogn), Sorting requires O(n log n) time complexity.
Auxiliary Space: O(1), As no extra space is required.

"""

# function for finding majority element in an array , return -1 if no majority element
def majority_element(arr):
    n = len(arr)

    # sort the array in O(nlogn)
    arr.sort()
    count, max_ele, temp, f =1, -1, arr[0], 0
    for i in range(1, n):
        # increases the count if the same element occurs otherwise it starts counting new element
        if (temp ==arr[i]):
            count +=1
        else:
            count = 1
            temp = arr[i]
        # sets maximum count and stores maximum occurred element so far if maximum cont becomes 
        # greater than n/2 it breaks out setting the flag
        if(max_ele < count):
            max_ele = count
            ele = arr[i]

            if(max_ele > (n//2)):
                f = 1
                break
    # returns maximum occurred element if there is no such element, returns -1
    if f == 1:
        return ele
    else: return -1

print("Expected:, Actual:", majority_element([1, 1, 2, 1, 3, 5, 1]))








print(" \n my tests \n ")
'''

my tests

'''

def my_tests(arr):
    dic ={}
    for i in range(len(arr)):
        dic[arr[i]] = dic.get(arr[i], 0) +1
    n = (len(arr)-1) /2

    for i, v in dic.items():
        if v > n:
            return i
        else:
            return -1

print("Expected:4, Actual:", my_tests([3, 3, 4, 2, 4, 4, 2, 4, 4]))
print("Expected:-1, Actual:", my_tests([3, 3, 4, 2, 4, 4, 2, 4]))
