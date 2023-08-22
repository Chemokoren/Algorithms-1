"""

Have the function ArrayJumping(arr) take the array of numbers stored in arr and first determine
the largest element in the array, and then determine whether or not you can reach that same element
within the array by moving left or right continuously according to whatever integer is in the 
current spot. If you can reach the same spot within the array, then your program should output the least
amount of jumps it took

For example: if the input is [1,3,5,6,1] you'll start at the spot where 6 is and if you jump 6 
spaces to the the right while looping around the array you end up at the last element where the
1 is. 
Then from here you jump 1 space to the left and you're back where you started, so your program
should output 2. 
If it's impossible to end up back at the largest element in the array, your program should output -1.
The largest element in the array will never equal the number of elements in the array. The largest element
will be unique.


Input:1,2,3,4,2
Output:3
Input:1,7,1,1,1,1
Output:2

"""
# Assume max is unique
# Max doesn't equal len(arr) >- output > 1
# positive integers only

def ArrayJumping(arr):

    ht ={}
    max_index =arr.index(max(arr))
    L = len(arr)

    for i in range(L):
        ht[i] =(left(L, i, arr[i]), right(L,i, arr[i]))

    if max_index in ht[max_index]:
        return 1

    travel_set =set(ht[max_index])

    for step in range(2, L+1):
        for val in tuple(travel_set):
            travel_set.add(ht[val][0])
            travel_set.add(ht[val[1]])
        if max_index  in travel_set:
            return step

    return -1

def left(length, index, number):
    left = number % length
    if left > index:
        left = length + index - left
    else:
        left = index - left
    return left

def right(length, index, number):
    right = number % length
    if right > length - index -1:
        right = right + index - length
    else:
        right = right + index
    return right
    



'''

my tests

'''

def array_jumping(arr):
    max_val =max(arr)
    i =arr.index(max_val)
    flag =True
    count = 0
    if(flag):
        i =(i+max_val)%len(arr)-1
        count +=1
        flag=False
    else:
        i = (i-arr[i])%len(arr)-1
        count +=1
        flag =True

    return count if arr[i] ==max_val else -1
 


print("Expected:2, Actual:", array_jumping([2, 3, 5, 6, 1]))
print("Expected:2, Actual:", array_jumping([1,7,1,1,1,1]))
print("Expected:3, Actual:", array_jumping([1,2,3,4,2]))

