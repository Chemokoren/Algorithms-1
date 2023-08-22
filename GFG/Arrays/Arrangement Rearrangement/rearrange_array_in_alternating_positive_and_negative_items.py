"""

Rearrange array in alternating positive & negative items with O(1) extra space | Set 1

Given an array of positive and negative numbers, arrange them in alternate fashion such that every 
positive number is followed by negative and vice-versa maintaining the order of appearance.

Number of positive and negative numbers need not be equal. If there are more positive  numbers they 
appear at the end of the array. If there are more negative numbers, they too appear in the end of 
the array.

Input: arr[] = {1,2,3,-4,-1,4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input: arr[] ={-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output: arr[] ={-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}


"""

def rearrange_arr(arr1):
    i =0
    positive_arr=[]
    negative_arr=[]

    while i < len(arr1):
        if arr1[i] < 0:
            negative_arr.append(arr1[i])
        else:
            positive_arr.append(arr1[i])
        i =i+ 1
    
    p =0
    n =0
    positive = True

    final_arr=[]
    while p<len(positive_arr) and n <len(negative_arr):
        if(not positive):
            final_arr.append(negative_arr[n])
            n =n+ 1
            positive =True
        else:
            final_arr.append(positive_arr[p])
            p =p+ 1
            positive =False

    while p < len(positive_arr):
        final_arr.append(positive_arr[p])
        p =p+ 1

    while n < len(negative_arr):
        final_arr.append(negative_arr[n])
        n =n+ 1
    return final_arr



arr =[1,2,3,-4,-1,4]  
arr1=[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]      
print("expected:[-4, 1, -1, 2, 3, 4], actual:",rearrange_arr(arr))
print("expected:[-5, 5, -2, 2, -8, 4, 7, 1, 8, 0], actual:", rearrange_arr(arr1))

"""
Naive approach

- The above problem can be easily solved if O(n) extra space is allowed. It becomes interesting due to the
limitations that O(1) extra space and order of appearances.
The idea is to process array from left to right. While processing, find the first out of place element in the
remaining unprocessed array. An element is out of place if it is negative and at odd index(0 based index), or
it is positive and at even index(0 based index). Once we find an out of place element, we find the first 
element after it with oppositive sign. We right rotate the subarray between these two elements(including 
these two).

Time Complexity : O(N^2)

Space Complexity : O(1)

"""

# rotates the array to right by once from index 'outOfPlace to cur'
def rightRotate(arr,n, outOfPlace, cur):
    temp =arr[cur]
    for i in range(cur, outOfPlace, -1):
        arr[i] = arr[i-1]
    arr[outOfPlace] = temp
    return arr

def rearrangeNaive(arr, n):
    outOfPlace = -1
    for index in range(n):
        if(outOfPlace >= 0):
            # if element at outOfPlace place in negative and if element at index is positive we can
            # rotate the array to right or if element at outOfPlace place in positive and if element at
            # index is negative we can rotate the array to right
            
            if((arr[index] >= 0 and arr[outOfPlace] < 0) or (arr[index] < 0 and arr[outOfPlace] >= 0)):
                arr =rightRotate(arr, n, outOfPlace, index)
                if(index - outOfPlace > 2):
                    outOfPlace += 2
                else:
                    outOfPlace =-1

        if(outOfPlace == -1):
            # conditions for A[index] to be in out of place
            if((arr[index] >= 0 and index %2 == 0) or (arr[index] < 0 and index % 2 ==1)):
                outOfPlace = index
    return arr

print(" rearrange naive")
arr =[1,2,3,-4,-1,4]  
arr1=[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]      
print("expected:[-4, 1, -1, 2, 3, 4], actual:",rearrangeNaive(arr, len(arr)))
print("expected:[-5, 5, -2, 2, -8, 4, 7, 1, 8, 0], actual:", rearrangeNaive(arr1,len(arr1)))


"""
Examples: 

Input :
arr[] = {-2, 3, 4, -1}
Output :
arr[] = {-2, 3, -1, 4} OR {-1, 3, -2, 4} OR ..

Input :
arr[] = {-2, 3, 1}
Output :
arr[] = {-2, 3, 1} OR {-2, 1, 3} 

Input : 
arr[] = {-5, 3, 4, 5, -6, -2, 8, 9, -1, -4}
Output :
arr[] = {-5, 3, -2, 5, -6, 4, -4, 9, -1, 8} 
        OR ..

Approach:
1.First, sort the array in non-increasing order. Then we will count the number of positive and negative integers
2.Then swap the one negative and one positive number in the odd positions till we reach our condition.
3. This will rearrange the array elements because we are sorting the array and accessing the element from left 
to right according to our need.

Time Complexity: O(N*logN)

Space Complexity: O(1)

"""
# function which works in the condition when number of negative numbers are lesser or equal than positive numbers
def fill1(a, neg, pos):
    
    if(neg % 2 == 1):

        for i in range(1, neg, 2):
            c = a[i]
            d = a[i + neg]
            temp = c
            a[i] = d
            a[i + neg] = temp

    else:
        for i in range(1, neg +1, 2):
            c = a[i]
            d = a[i + neg -1]
            temp =c
            a[i] = d
            a[i+neg -1] = temp

# Function which works in the condition
# when number of negative numbers are 
# greater than positive numbers
def fill2(a, neg, pos):
    if(pos % 2== 1):
        for i in range(1, pos, 2):
            c = a[i]
            d = a[i + pos]
            temp = c 
            a[i] = d
            a[i + pos] = temp

    else:
        for i in range(1, pos + 1, 2):
            c =a[i]
            d =[i + pos -1]
            temp =c 
            a[i] =d
            a[i + pos -1] = temp

# Reverse the array
def reverse(a, n):
    
    for i in range(n / 2):
        t = a[i]
        a[i] = a[n - i - 1]
        a[n - i - 1] =t

# print the array
def printt(a, n):
    for i in range(n):
        print(a[i], end =" ")

    print()

if __name__=="__main__":
    arr =[2,3,-4,-1,6,-9]
    n =len(arr)
    print("Given array is")
    printt(arr,n)

    neg = 0
    pos = 0
    for i in range(0, n):
        if(arr[i]<0):
            neg += 1
        else:
            pos +=1

    # sort the array
    arr.sort()
    if(neg <= pos):
        fill1(arr, neg, pos)
    else:

        # Reverse the array in this condition
        reverse(arr, n)
        fill2(arr, neg, pos)
    print(" Rearranged array is ")
    printt(arr, n)
    

"""
Efficient approach:

- If we are allowed to change order of appearance, we can solve this problem in O(n) time and O(1) space.
- The idea is to process the array and shift all negative values to the end in O(n) time. After all negative
values are shifted to the end, we can easily rearrange array in alternating positive & negative items. We basically 
swap next positive element at even position from next negative element in this step.

Time Complexity : O(N)

Space Complexity : O(1)

"""
# program to rearrange array in alternating positive & negative items with O(1) extra space
# Function to rearrange positive and negative integers in alternate fashion
# The following solution does not maintain the original order of elements

def rearrange(arr, n):
    i = 0
    j = n-1

    #shift al negative values to the end
    while(i < j):

        while(i <=n-1 and arr[i] > 0):
            i +=1
        while(j >= 0 and arr[j] < 0):
            j -=1

        if(i < j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        
    # i has index of leftmost negative element
    if(i == 0 or i ==n):
        return 0

    # start with first positive element at index 0

    # Rearrange array in alternating positive & negative items
    k = 0
    while( k< n and i < n):

        # swap next positive element at even position from next negative element
        temp = arr[k]
        arr[k] = arr[i]
        arr[i] = temp 
        i = i +1
        k = k +2

    
# Utility function to print an array
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print("\n")


print("# main code for efficient approach")
arr =[2,3,-4,-1,6,-9]
n = len(arr)

print("Given array is")
printArray(arr, n)
 
rearrange(arr, n)
 
print("Rearranged array is")
printArray(arr, n)