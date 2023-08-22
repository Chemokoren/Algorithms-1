"""

Sort elements by frequency

print the elements of an array in the decreasing frequency. If 2 numbers have same 
frequency then print the one which came first.

    Input:  arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
    Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}

    Input: arr[] = {2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8}
    Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999}

METHOD 1(Use Sorting)
- Use sorting algoritm to sort the elements O(nlogn)
- Iterate the sorted array and construct a 2D array of elements and count O(n).
- Sort the 2D array according to count O(nlogn)

 Input 2 5 2 8 5 6 8 8
  After sorting we get
  2 2 5 5 6 8 8 8
  Now construct the 2D array as
  2, 2
  5, 2
  6, 1
  8, 3
  Sort by count
  8, 3
  2, 2
  5, 2
  6, 1

  How to maintain the order of elements if the frequency is the same?

  The above approach doesn't make sure the order of elements if the frequency is the same.
  To handle this, we should use indexes in step 3, if two counts are the same then we 
  should first process(or print) the element with a lower index. In step 1, we should
  store the indexes instead of elements.


Input   2  5  2  8  5  6  8  8
After sorting we get
Element 2 2 5 5 6 8 8 8
Index   0 2 1 4 5 3 6 7
Now construct the 2D array as
Index, Count
0,      2
1,      2
5,      1
3,      3
Sort by count (consider indexes in case of tie)
3, 3
0, 2
1, 2
5, 1
Print the elements using indexes in the above 2D array.



"""

# program that sorts elements by frequency. If two elements have same count, then put
# the elements that appears first

class ele:
    def __init__(self) -> None:
        self.count = 0
        self.index = 0
        self.val = 0

def mycomp(a):
    return a.val

# used for sorting by frequency. And if frequency is same, then by appearance

def mycomp2(a):
    # using negative value for a.index since the sorting should be in descending order
    return (a.count, -a.index)

def sortByFrequency(arr):
    n = len(arr)

    element =[None for _ in range(n)]
    for i in range(n):
        element[i] = ele()

        # Fill Indexes
        element[i].index = i

        # Initialize counts as 0
        element[i].count = 0

        # Fill values in structure elements
        element[i].val =arr[i]

    # sort the structure elements according to value, we used stable sort so relative 
    # order  is maintained.
    element.sort(key=mycomp)

    # initialize count of first element as 1
    element[0].count =1

    # count occurrences of remaining elements
    for i in range(1, n):

        if(element[i].val == element[i-1].val):
            element[i].count += element[i-1].count + 1

            # Set count of previous elements as -1, we are doing this because we'll again
            # sort on the basis of counts(if counts are equal than on the basis of index)
            element[i-1].count =-1

            # Retain the first index(Remember first index is always present in the first 
            # duplicate we used stable sort.)
            element[i].index = element[i-1].index

        # Else if previous element is not equal to current so set the count to 1
        else:
            element[i].count =1

    # Now we have counts and first index for each element so now sort on the basis of 
    # count and in case of ties use index to sort
    element.sort(key=mycomp2)

    index = 0
    for i in range(n-1, -1, -1):
        if(element[i].count != -1):
            for j in range(element[i].count):
                arr[index] =element[i].val
                index += 1
                
    return arr

print("Expected:[8, 8, 8, 2, 2, 5, 5, 6], actual:", sortByFrequency([2, 5, 2, 8, 5, 6, 8, 8]))
print("Expected:[8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999], actual:", sortByFrequency([2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]))


"""
METHOD 2: Use Hashing and Sorting

Using a hashing mechanism, we can store the elements(also the first index) and their
counts in a hash. Finally, sort the hash elements according to their counts.

This can also be solved by Using two maps, one for array element as an index and after
this second map whose keys are frequency and value are array elements.
"""

from collections import defaultdict

# sort by frequency
def sortByFreq(arr):
    n =len(arr)

    d =defaultdict(lambda:0)
    for i in range(n):
        d[arr[i]] +=1
    
    # sorting the array 'arr' where key is the function based on which the array is sorted
    # while sorting we want to give first priority to Frequency then to value of item
    arr.sort(key=lambda x:(-d[x], x))

    return (arr)


print("Expected:[8, 8, 8, 2, 2, 5, 5, 6], actual:", sortByFreq([2, 5, 2, 8, 5, 6, 8, 8]))
print("Expected:[8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999], actual:", sortByFreq([2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]))



"""
METHOD 3: Use BST and sorting

- Insert elements in BST one by one and if an element is already present then increment
the count of the node. The node of the Binary Search Tree in this approach is as follows

"""
class Tree:
    element = None

    # to handle ties
    first_index = None
    count = None

BST = Tree()

"""
    Store the first indexes and corresponding counts of BST in a 2D array.
    Sort the 2D array according to counts (and use indexes in case of tie).

Time Complexity: O(nlogn) if a Self Balancing Binary Search Tree is used. 

 https://youtu.be/NBXf9vCksuM


 METHOD 4: (Heap-Based Solution)

    ALGORITHM:

        Take the arr and use unordered_map to have VALUE : FREQUENCY Table
        Then make a HEAP such that high frequency remains at TOP and when frequency is
        same, just keep in ascending order (Smaller at TOP)
        Then After full insertion into Heap.
        Pop one by one and copy it into the Array.

Time Complexity:

O(d*log(d)) (Dominating factor O(n+ 2*d*log(d)))

Reason:  O(n) (unordered map insertion- as 1 insertion takes O(1)) + O(d*log(d)) 
(Heap insertion – as one insertion is log N complexity) + O(d*log(d)) (Heap Deletion – as 
one pop takes Log N complexity) 

Here d = No. of Distinct Elements, n = Total no. of elements (size of input array). 
(Always d<=n  depends on array)

Extra Space Complexity:

O(d)  => As heap and map is created. 

"""


'''

comparator works in prority_queue only if they are a class which has
operator() overloaded in it

'''
class Compare:
    
    # pair<int, int> a, pair<int, int> b)
    def operator(a, b):
        # b is at top and a is at bottom - have that in mind
        if(a.first == b.first): #when freq same 
            return a.second > b.second # smaller val stays at top
        return a.first < b.first # higher freq stays at top
		

# vector<int> &arr
def solve(arr):
    
    N = len(arr)
    
    #unordered_map<int ,int> mpp; // val, freq
    mpp ={}
    for a in arr:
        mpp[a] +=1
        
    # max heap - as max wise freq elements is what needed
    # # priority_queue<ppi,vector<ppi>, Compare> maxH;
    # 
    for m in mpp:
        maxH.push({m.second, m.first}) # freq, val
        
    # now the max freq is at TOP of MAX heap
    
    i=0 # to maintain index to copy
    
    while(maxH.size()>0):
        val = maxH.top().second # val
        freq = maxH.top().first # freq
        
        freq -=1
        while(freq):
            #freq - those many times make a copy
            arr[i] = val
            i +=1
            
        maxH.pop(); # heapify happens and next top freq ele goes up

    return arr
	
	

solve([ 2, 5, 2, 8, 5, 6, 8, 8 ])














print("\n my tests\n")
'''
my tests
''' 

def my_tests(arr):
    new_set =set(arr)
    dic={}
    final_arr=[]
    for i in new_set:
        dic[i] =arr.count(i)

    new_val= {k:v for k,v in sorted(dic.items(),key=lambda item:item[1],reverse=True)}

    for i,v in new_val.items():
        if v ==1:
            final_arr.append(i)
        else:
            for val in str(i)*v:
                final_arr.append(int(val))
    

    return final_arr
    

print("Expected:[8, 8, 8, 2, 2, 5, 5, 6], actual:", my_tests([2, 5, 2, 8, 5, 6, 8, 8]))
print("Expected:[8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999], actual:", my_tests([2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]))