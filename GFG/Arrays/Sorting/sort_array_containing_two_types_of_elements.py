"""
Sort an array containing two types of elements

Given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right 
side of the array. Traverse array only once.

Examples: 

Input :  arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output : arr[] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 

Input :  arr[] = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1] 
Output : arr[] = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1] 

Step 1: Here we can take two pointers type0(for element 0) starting from beginning
(index = 0)and type1(for element 1) starting from end index
Step 2: We intend to put  to the right side of the array. Once we have done this then 0
will definetely move towards the left side of array. To achieve this we do the following:
We compare elements index typ0
1) if this is 1 then this should be moved to right side so we need to swap this with
index type1 once swapped we are sure that element at index type1 is '1' so we need to
decrement index type1
2) else it will be 0 then we need to simple increment index type0

"""
# program to sort an array with two types of values in one traversal.

# method for segregating 0 and 1 given input array
def segegregate_0_and_1(arr):
    n =len(arr)

    start = 0
    end = n-1

    while (start < end):
        if(arr[start] == 1):
            arr[start], arr[end] = arr[end], arr[start]
            end -=1
        else:
            start +=1
        
    return arr

print("Expected: [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], Actual:", segegregate_0_and_1([1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1] ))
print("Expected: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], Actual:", segegregate_0_and_1([0, 1, 0, 1, 0, 0, 1, 1, 1, 0]))













print("\n my tests \n")

'''
my tests
'''

def my_tests(arr):
    start = 0
    end =len(arr)-1

    while start < end:
        if arr[start] ==0:
            start +=1

        if start < end:
            if arr[end] ==1:
                end -=1

        arr[start], arr[end] = arr[end],arr[start]
    return arr

print("Expected: [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], Actual:", my_tests([1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1] ))
print("Expected: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], Actual:", my_tests([0, 1, 0, 1, 0, 0, 1, 1, 1, 0]))