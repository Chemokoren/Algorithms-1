"""
Count elements which divide all numbers in range L-R

Given N numbers and Q queries, each query consists of L and R. Task is to write a program
which prints the count of numbers which divides all  numbers in the given range(L-R).


Input : a = {3, 4, 2, 2, 4, 6} 
        Q = 2
        L = 1 R = 4  
        L = 2 R = 6
    
Output :  0
          2 

Explanation : The range 1-4 has {3, 4, 2, 2} 
which does not have any number that divides all the 
numbers in this range. 
The range 2-6 has {4, 2, 2, 4, 6} which has  2 numbers {2, 2} which divides 
all numbers in the given range. 

Input: a = {1, 2, 3, 5} 
       Q = 2 
       L = 1 R = 4 
       L = 2 R = 4 
Output: 1 
        0   

Naive Approach

- Iterate from L-R for every query and check if the given element at index-i divides all
the numbers in the range. We keep a count for all the elements which divides all the 
numbers. The complexity of every query at worst case will be O(n^2).

"""
# program to count elements which divides all numbers in range L-R

# function to count element: Time complexity O(n^2) worst case
from dataclasses import dataclass


def answerQuery(a, l, r):

    # answer for query
    count = 0

    # 0 based index
    l = l -1

    # Iterate for all elements
    for i in range(l, r, 1):
        element =a[i]
        divisors = 0

        # check if the element divides all numbers in range
        for j in range(l, r, 1):
            # no of elements
            if(a[j] % a[i] == 0):
                divisors += 1
            else:
                break

        # if all elements are divisible by a[i]
        if(divisors == (r -l)):
            count += 1
    # answer for every query
    return count

# print("expected: 1, actual, ", answerQuery([1, 2, 3, 5], 1, 4))
# print("expected: 0, actual, ", answerQuery([1, 2, 3, 5], 2, 4))
# print("expected: 0 , actual:", answerQuery([3, 4, 2, 2, 4, 6],1,4))
# print("expected: 2 , actual:", answerQuery([3, 4, 2, 2, 4, 6],2,6))


"""
Efficient approach

Use segment Trees to solve this problem. If an element divides all the numbers in a given
range, then the element is the minimum number in that range and it is the gcd of all 
elements in the given range L-R. So the count of the number of minimums in range L-R, 
given that minimum is equal to the gcd of that range will be our answer to every query.
The problem boils down to finding GCD, MINIMUM and countMINIMUM for every range using 
Segment trees. On every node of the tree, three values are stored.
On querying for a given range, if the gcd and minimum of the given range are equal,
countMINIMUM is returned as the answer. If they are unequal, 0 is returned as the answer.

Time Complexity: Time Complexity for tree construction is O(n logn) since tree 
construction takes O(n) and finding out gcd takes O(log n). The time taken for every 
query in worst case will be O(log n * log n) since the inbuilt function __gcd 
takes O(log n)

"""
from typing import List
# CPP program to Count elements which divides all numbers in
# range L-R efficient approach

#define N 100005
N = 100005

# predefines the tree with nodes storing gcd, min and count
@dataclass
class node:
	gcd: int
	min: int
	cnt: int


tree =[5] * N

# function to construct the tree
def buildtree(low:int, high:int,pos:int, a:List[int]):
	# base condition
	if (low == high):
		# initially always gcd and min are same at leaf node
		tree[pos].min = tree[pos].gcd = a[low]
		tree[pos].cnt = 1
		return

	mid = (low + high) >> 1
	
	# left-subtree
	buildtree(low, mid, 2 * pos + 1, a)

	# right-subtree
	buildtree(mid + 1, high, 2 * pos + 2, a)

	# finds gcd of left and right subtree
	tree[pos].gcd = _gcd(tree[2 * pos + 1].gcd,	tree[2 * pos + 2].gcd)

	# left subtree has the minimum element
	if (tree[2 * pos + 1].min < tree[2 * pos + 2].min):
		tree[pos].min = tree[2 * pos + 1].min
		tree[pos].cnt = tree[2 * pos + 1].cnt
	
	# right subtree has the minimum element
	elif (tree[2 * pos + 1].min > tree[2 * pos + 2].min):
		tree[pos].min = tree[2 * pos + 2].min
		tree[pos].cnt = tree[2 * pos + 2].cnt
	
	# both subtree has the same minimum element
	else:
		tree[pos].min = tree[2 * pos + 1].min
		tree[pos].cnt = tree[2 * pos + 1].cnt +	tree[2 * pos + 2].cnt;


# function that answers every query
def query(s:int,e:int,low:int,high:int,pos:int)->node:
    
    dummy: node
    
    # out of range
    if (e < low or s > high):
        dummy.gcd = dummy.min = dummy.cnt = 0
        return dummy

    # in range    
    if (s >= low and e <= high):
        dummy: node
        dummy.gcd = tree[pos].gcd
        dummy.min = tree[pos].min
        
        if(dummy.gcd != dummy.min):
            dummy.cnt = 0
        else:
            dummy.cnt = tree[pos].cnt
        return dummy
    
    mid = (s + e) >> 1
    
    # left-subtree
    ans1 = query(s, mid, low, high, 2 * pos + 1) # of type node
    
    # right-subtree
    ans2 = query(mid + 1, e, low,high, 2 * pos + 2) # node
    
    ans:node
    
    # when both left subtree and right subtree is in range
    if (ans1.gcd and ans2.gcd):
        
        # merge two trees
        ans.gcd = __gcd(ans1.gcd, ans2.gcd)
        ans.min = min(ans1.min, ans2.min)
        
        # when gcd is not equal to min
        
        if (ans.gcd != ans.min):
            ans.cnt = 0
        else:
            # add count when min is same of both subtree
            if (ans1.min == ans2.min): 
                ans.cnt = ans2.cnt + ans1.cnt;
                
            # store the minimal's count
            else:
                if (ans1.min < ans2.min):
                    ans.cnt = ans1.cnt
                else:
                    ans.cnt = ans2.cnt
        return ans
        
    # only left subtree is in range
    elif (ans1.gcd):
        return ans1
    #only right subtree is in range
    elif (ans2.gcd):
        return ans2;


# function to answer query in range l-r
def answerQuery(a:List[int], n:int, l:int, r:int):
	#  calls the function which returns a node this function returns the
	# count which will be the answer
	return query(0, n - 1, l - 1, r - 1, 0).cnt


if __name__=='__main__':
    a = [ 3, 4, 2, 2, 4, 6 ]
    n = len(a) / len(a[0])
    
    buildtree(0, n - 1, 0, a)
    l = 1
    r = 4
    
    #  answers 1-st query
    print(answerQuery(a, n, l, r))
    
    l = 2
    r = 6
    
    # answers 2nd query
    print(answerQuery(a, n, l, r))
  


'''
my tests
'''
def my_tests(arr,Q):
    l,r =Q
    l =l-1
    arr =arr[l:r]
    count =0
    divisors =0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] % arr[j] ==0:
                divisors +=1
        if divisors ==(r-l)+1:
            count +=1
        divisors =0
        

    return count

print("expected: 1, actual, ", my_tests([1, 2, 3, 5], [1, 4]))
print("expected: 0, actual, ", my_tests([1, 2, 3, 5], [2, 4]))
print("expected: 0 , actual:", my_tests([3, 4, 2, 2, 4, 6],[1,4]))
print("expected: 2 , actual:", my_tests([3, 4, 2, 2, 4, 6],[2,6]))