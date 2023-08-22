"""
Ceiling in a sorted array

Given a sorted array and a value x, the ceiling of x is the smallest element in an array greater
than or equal to x, and the floor is the greatest element smaller than or equal to x. Assume that
the array is sorted in non-decreasing order. Write efficient functions to find the floor and 
ceiling of x.


Examples : 

For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
For x = 0:    floor doesn't exist in array,  ceil  = 1
For x = 1:    floor  = 1,  ceil  = 1
For x = 5:    floor  = 2,  ceil  = 8
For x = 20:   floor  = 19,  ceil doesn't exist in array

In the below methods, we have implemented only ceiling search functions. Floor earch can be 
implemented in the same way.

Method 1: Linear Search
Algorithm to search ceiling of x:
1. if x is smaller than or equal to the first element in the array then return 0(index of first
element)
2. Else linearly search for an index i such that x lies between arr[i] and arr[i+1]
3. If we do not find an index in step 2, then return -1

"""
# function to get index of ceiling of x in arr[low..high]
# Time Complexity: O(n), Auxiliary Space: O(1)
def ceil_search(arr, x):
    low =0
    high = len(arr)-1
    # if x is smaller than or equal to first element, then return the first element
    if x <= arr[low]:
        return low

    # otherwise, linearly search for ceil value
    i = low
    for i in range(high):
        if arr[i] == x:
            return i
        # if x lies between arr[i] and arr[i+1] including arr[i+1], then return arr[i+1]
        if arr[i] < x and arr[i+1] >=x:
            return i +1
    # if we reach here then x is greater than the last element of the arrya, return -1 in this case
    return -1

print("Expected: ", ceil_search([1, 2, 8, 10, 10, 12, 19], 20))


"""
Method 2: Binary Search

Instead of using linear search, binary search is used here to find out the index. Binary search
reduces the time complexity to O(Logn)

Time Complexity: O(log(n)), Auxiliary Space: O(1)
"""

# function to get index of ceiling of x in arr[low ... high]
def ceil_search(arr, low, high, x):

    # if x is smaller than or equal to the first element, then return the first element
    if x <= arr[low]:
        return low
    # if x is greater than the last element, then return -1
    if x > arr[high]:
        return -1

    # get the index of middle element of arr[low..high]
    mid =(low + high) / 2 # low +(high - low) / 2

    # if x is same as middle element, then return mid
    if arr[mid] == x:
        return mid

    # if x is greater than arr[mid], then either arr[mid+1]
    # is ceiling of x or ceiling lies in arr[mid+1 ... high]
    elif arr[mid] < x:
        if mid + 1 <= high and x <= arr[mid+1]:
            return mid + 1
        else:
            return ceil_search(arr, mid +1, high, x)

    # if x is smaller than arr[mid], then either arr[mid]
    # is ceiling of x or ceiling lies in arr[low ... mid-1]
    else:
        if mid -1 >= low and x > arr[mid]:
            return mid
        else:
            return ceil_search(arr, low, mid -1, x)

    
print("AA Expected", ceil_search([1, 2, 8, 10, 10, 12, 19], 0, len([1, 2, 8, 10, 10, 12, 19])-1, 20))

"""
Another approach

- Like the previous method, binary search is at play. However, the code logic is different,
instead of lots of if else check, we will simply return.
- Lets understand through the steps below:


Step 1 : { low->1, 2, 8, 10<-mid, 10, 12, 19<-high};

if( x < mid) yes set high = mid -1;

Step 2 : { low ->1, 2 <-mid, 8 <-high, 10, 10, 12, 19};

if( x < mid) no set low = mid + 1;

Step 3 : {1, 2, 8<-high,low,mid,  10, 10, 12, 19};

if( x == mid ) yes return mid  
if(x < mid ) no low = mid + 1

Step 4  : {1, 2, 8<-high,mid, 10<-low, 10, 12, 19};

check while(low =<  high)


Time Complexity: O(log(n)), where n is the length of the given array, Auxiliary Space: O(1)

"""

def ceil_search_updated(arr, low, high, x):

    # base condition if length of arr == 0 then return -1
    if(x == 0):
        return -1
    """

    this while loop function will run until condition does not break
    Once the condition breaks, loop will return start and ans is low which will be next smallest
    greater than target which is ceiling

    """
    while (low <= high):
        mid = low + (high - low) / 2
        mid = int(mid)
        if(arr[mid] == x):
            return mid
        elif(x < arr[mid]):
            high = mid -1
        else:
            low = mid + 1
    return low

""" step 1 : { low = 1, 2, 8, 10= mid, 10, 12, 19= high};
                if( x < mid) yes set high = mid -1;
      step 2 : { low = 1, 2 = mid, 8 = high, 10, 10, 12, 19};
                if( x < mid) no set low = mid + 1;
      step 3 : {1, 2, 8 = high,low,low,  10, 10, 12, 19};
                 if( x == mid ) yes return mid
                 if(x < mid ) no low = mid + 1
      step 4  : {1, 2, 8 = high,mid, 10 = low, 10, 12, 19};
                check while(low < = high)
                 condition break and return low which will next greater of target 
"""
 
arr = [1, 2, 8, 10, 10, 12, 19]
n = len(arr)
x = 8
print("UP Expected", ceil_search_updated(arr, 0, n - 1, x))




print("\n my tests \n")
def my_tests(arr, key):

    ceil_val =-float("inf")
    floor_val =float("inf")
    idx =check_idx(arr, key)
    
    if len(arr)-1 == idx:
        ceil_val =-1
    else:
        if arr[idx] >= key:
            ceil_val =arr[idx]
        elif arr[idx+1] >= key:
            ceil_val =arr[idx+1] 
            
    if  key < arr[0]:
            floor_val =-1
    else:
        if arr[idx] <= key:
            floor_val =arr[idx]
        elif arr[idx-1] <= key:
                floor_val =arr[idx-1] 
        

    return floor_val,ceil_val


def check_idx(arr, key):

    for i in range(len(arr)):
        if arr[i] ==key:
            return i
        elif arr[i] < key and arr[i+1] > key:
                return i
        elif key > arr[len(arr)-1]:
                return len(arr)-1
        elif key < arr[0]:
                return 0
print("Expected: [-1,1], Actual:", my_tests([1, 2, 8, 10, 10, 12, 19], 0))
print("Expected: [1,1], Actual:", my_tests([1, 2, 8, 10, 10, 12, 19], 1))
print("Expected: [2,8], Actual:", my_tests([1, 2, 8, 10, 10, 12, 19], 5))
print("Expected: [19,-1], Actual:", my_tests([1, 2, 8, 10, 10, 12, 19], 20))

def binary_search(arr, key):
    start =0
    end =len(arr)-1

    while start <= end:
        mid = (start+end)// 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start =mid+1
        else:
            end = mid-1
    return -1


print("Eggg", binary_search([1, 2, 8, 10, 10, 12, 19], 34))