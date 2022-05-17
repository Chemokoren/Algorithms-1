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