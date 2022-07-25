"""
Sort an array in wave form

Given an unsorted array of integers, sort the array into a wave like array. An array 
'arr[0..n-1]' is sorted in wave form if arr[0]>=arr[1]<=arr[2]>=arr[3]<=arr[4]>=...

Well, you have seen waves right? How do they look? If you will form a graph of them it 
would be some in som up-down fashion.

That is what you have to do here, you  are supposed to arrange numbers in such a way 
that if we will form a graph, it will be in an up-down fashion rather than a straight 
line.

Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
 Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
                 {20, 5, 10, 2, 80, 6, 100, 3} OR
                 any other array that is in wave form
                 
                 here you can see {10, 5, 6, 2, 20, 3, 100, 80} first element is larger 
                 than the second and the same thing is repeated again and again. large 
                 element - small element-large element -small element
                 and so on .
                 it can be small element-larger element - small element-large element 
                 -small element too.
                 all you need to maintain is the up-down fashion which represents a wave.
                  there can be multiple answers.
                 

 Input:  arr[] = {20, 10, 8, 6, 4, 2}
 Output: arr[] = {20, 8, 10, 4, 6, 2} OR
                 {10, 8, 20, 2, 6, 4} OR
                 any other array that is in wave form

 Input:  arr[] = {2, 4, 6, 8, 10, 20}
 Output: arr[] = {4, 2, 8, 6, 20, 10} OR
                 any other array that is in wave form

 Input:  arr[] = {3, 6, 5, 10, 7, 20}
 Output: arr[] = {6, 3, 10, 5, 20, 7} OR
                 any other array that is in wave form

A simple solution is to uses sorting. First sort the input array, the swap all 
adjacent elements.
- For example, let the input array be [3,6,5,10,7,20].
- After sorting, we get [3,5,6,7,10,20]
- After swapping adjacent elements, we get [5,3,7,6,20,10]

Time Complexity: O(nlogn)

Auxiliary Space: O(1)

The time complexity of the above solution is O(nLogn) if an O(nLogn) sorting algorithm 
like Merge Sort, Heap Sort, etc are used.

"""

def sort_in_wave(arr):
    n = len(arr)
    arr.sort()

    # swap adjacent elements
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] =arr[i+1], arr[i]
        print(i, arr[i], arr[i+1])
    return arr


print("Expected: [2 1 10 5 49 23 90], Actual:", sort_in_wave([10, 90, 49, 2, 1, 5, 23]))


"""
Approach 2

This can be done in O(n) time by doing a single traversal of the given array. The idea is
based on the fact that if we make sure that all even positioned (at index 0, 2, 4, ..) 
elements are greater than their adjacent odd elements, we don’t need to worry about oddly
positioned elements. 

The following are simple steps. 
1) Traverse all even positioned elements of the input array, and do the following. 
….a) If the current element is smaller than the previous odd element, swap previous and 
current. 
….b) If the current element is smaller than the next odd element, swap next and current.

Time Complexity: O(n)

Auxiliary Space: O(1)

"""

def sort_in_wave_two(arr):
    n = len(arr)

    # Traverse all even elements
    for i in range(0, n, 2):

        # If current even element is smaller than previous
        if(i > 0 and arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]

        # if current even element is smaller than next
        if (i < n-1 and arr[i] < arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]

    return arr
print("Expected: [90 10 49 1 5 2 23], Actual:", sort_in_wave_two([10, 90, 49, 2, 1, 5, 23]))







print("\n my tests \n")
'''
my tests
'''
def my_tests(arr):
    arr.sort()
    final_arr=[]

    start =0
    end = len(arr)-1

    while start <= end:
        final_arr.append(arr[start])
        start +=1

        # handles the case of an odd array to avoid duplicates
        if start <= end:
            final_arr.append(arr[end])
            end -=1
    return final_arr

print(my_tests([3, 6, 5, 10, 7, 20]))
print(my_tests([2, 4, 6, 8, 10, 20]))
print(my_tests([10, 90, 49, 2, 1, 5, 23]))

def sort_arr_wave_form(arr):

    for i in range(0, len(arr)-1, 2):
        if i%2 ==0 and arr[i] < arr[i+1]:
            arr[i],arr[i+1] =arr[i+1], arr[i]

    return arr

print("Expected: [90 10 49 1 5 2 23], Actual:", sort_arr_wave_form([10, 90, 49, 2, 1, 5, 23]))
