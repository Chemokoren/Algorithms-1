"""
Given an array A[] and a number x, check for pair in A[] with sum as x(aka Two Sum)

Write a program that, given an array A[] of n numbers and another number x, determines whether or 
not there exists two elements in A[] whose sum is exactly x.

Input: arr[] ={0, -1, 2, -3, 1}
x =-2
Output: Pair with a given num -2 is(-3, 1)
valid pair exists

Input: arr[] = {1, -2, 1, 0, 5}
       x = 0
Output: No valid pair exists for 0

Method 1: Sorting and Two-Pointers technique.

Approach: A tricky approach to solve this problem can be to use the two-pointer technique. 
But for using two pointer technique, the array must be sorted. Once the array is sorted the two 
pointers can be taken which mark the beginning and end of the array respectively. If the sum is
greater than the sum of those two elements, shift the right pointer to decrease the value of the 
required sum and if the sum is lesser than the required value, shift the left pointer to increase 
the value of the required sum. Let’s understand this using an example.

    Let an array be {1, 4, 45, 6, 10, -8} and sum to find be 16
    After sorting the array 
    A = {-8, 1, 4, 6, 10, 45}
    Now, increment ‘l’ when the sum of the pair is less than the required sum and decrement ‘r’ when the sum of the pair is more than the required sum. 
    This is because when the sum is less than the required sum then to get the number which could increase the sum of pair, start moving from left to right(also sort the array) thus “l++” and vice versa.
    Initialize l = 0, r = 5 
    A[l] + A[r] ( -8 + 45) > 16 => decrement r. Now r = 4 
    A[l] + A[r] ( -8 + 10) increment l. Now l = 1 
    A[l] + A[r] ( 1 + 10) increment l. Now l = 2 
    A[l] + A[r] ( 4 + 10) increment l. Now l = 3 
    A[l] + A[r] ( 6 + 10) == 16 => Found candidates (return 1)

Note: If there is more than one pair having the given sum then this algorithm reports only one. 
Can be easily extended for this though.

Algorithm: 

    hasArrayTwoCandidates (A[], ar_size, sum)
    Sort the array in non-decreasing order.
    Initialize two index variables to find the candidate 
    elements in the sorted array. 
        Initialize first to the leftmost index: l = 0
        Initialize second the rightmost index: r = ar_size-1
    Loop while l < r. 
        If (A[l] + A[r] == sum) then return 1
        Else if( A[l] + A[r] < sum ) then l++
        Else r–
    No candidates in the whole array – return 0

    Time Complexity: Depends on what sorting algorithm we use. 
        If Merge Sort or Heap Sort is used then (-)(nlogn) in the worst case.
        If Quick Sort is used then O(n^2) in the worst case.
    Auxiliary Space: This too depends on sorting algorithm. The auxiliary space is O(n) for merge 
    sort and O(1) for Heap Sort.

"""

def array_has_two_elememts(arr, x):
    arr.sort()
    i = 0
    j = len(arr)-1
    res =[]

    while i <j:
        if(arr[i] + arr[j]) < x:
            i +=1
        elif(arr[i] + arr[j])>x:
            j -=1
        elif(arr[i] + arr[j])== x:
            res.append((arr[i], arr[j]))
            return res

print("Trial Expected, Actual", array_has_two_elememts([1, -2, 1, 0, 5], 0))
print("Trial Expected, Actual", array_has_two_elememts([0, -1, 2, -3, 1], -2))

"""
Method 2: Hashing

-This problem can be solved efficiently by using the technique of hashing. Use a hash_map to 
check for the current array value x(let), if there exists a value target_sum-x which on adding 
to the former gives target_sum. This can be done in constant time. 

arr[] = {0, -1, 2, -3, 1} 
sum = -2 
Now start traversing: 
Step 1: For ‘0’ there is no valid number ‘-2’ so store ‘0’ in hash_map. 
Step 2: For ‘-1’ there is no valid number ‘-1’ so store ‘-1’ in hash_map. 
Step 3: For ‘2’ there is no valid number ‘-4’ so store ‘2’ in hash_map. 
Step 4: For ‘-3’ there is no valid number ‘1’ so store ‘-3’ in hash_map. 
Step 5: For ‘1’ there is a valid number ‘-3’ so answer is 1, -3 

Algorithm
- Initialize an empty hash table s.
- Do the following for each element A[i] in A[]
    - if s[x-A[i]] is set then print the pair(A[i], x-A[i])
    - insert A[i] into s.

unordered_set_s
for(i=0 to end)
    if(s.find(target_sum - arr[i]) == s.end)
        insert(arr[i] into s)
    else 
        print arr[i], target-arr[i]

    Time Complexity: O(n). 
    As the whole array is needed to be traversed only once.
    Auxiliary Space: O(n). 
    A hash map has been used to store array elements.

Note: The solution will work even if the range of numbers includes negative numbers + if the pair
is formed by numbers recurring twice in array eg: array = [3,4,3]; pair = (3,3); target sum = 6.

"""
def print_pairs(arr,target_sum):
    arr_size =len(arr)
    dic ={}

    for i in range(0, arr_size):
        temp = target_sum -arr[i]
        if temp in dic:
            return ((temp, arr[i]))
        dic[arr[i]] =i


print("pairs::::", print_pairs([1, 4, 45, 6, 10, 8], 16))
print("pairs::::, Actual", print_pairs([1, -2, 1, 0, 5], 0))


"""
Method 3: Using remainders of the elements less than x

Approach
- The idea is to count the elements with remainders when divided by x, i.e 0 to x-1, each 
remainder seperately.  Suppose we have x as 6, then the numbers which are less than 6 and have 
remainders which add up to 6 gives sum as 6 when needed. For example, we have elements, 2,4 in the
array and 2%6 =2 and 4%6=4, and these remainders add up to give 6. Like that we have to check for
pairs with remainders (1,5), (2,4), (3,3). If we have one or more elements with remainder 1 and one
or more elements with remainder 5, then surely we get a sum as 6. Here we do not consider(0,6) as
the elements for the resultant pair should be less than 6. When it comes to(3,3) we have to check 
if we have two elements with remainder 3, then we can say that "there exists a pair sum whoe sum
is x".
Algorithm:

1. Create an array with size x. 

2. Initialize all rem elements to zero.

3. Traverse the given array

    Do the following if arr[i] is less than x:
        r=arr[i]%x which is done to get the remainder.
        rem[r]=rem[r]+1 i.e. increasing the count of elements that have remainder r when divided with x.

4. Now, traverse the rem array from 1 to x/2.   

    If(rem[i]> 0 and rem[x-i]>0) then print “YES” and come out of the loop. This means that we have a pair that results in x upon doing.

5. Now when we reach at x/2 in the above loop   

    If x is even, for getting a pair we should have two elements with remainder x/2.
        If rem[x/2]>1 then print “YES” else print “NO”
    If it is not satisfied that is x is odd, it will have a separate pair with x-x/2.
        If rem[x/2]>1 and rem[x-x/2]>1 , then print “Yes” else, print”No”;

Time Complexity: O(n+x)
Auxiliary Space: O(x)

"""
# code to tell if there exists a pair in array whose sume results in x
def print_pairs_three(a, x):

    n = len(a)

    rem =[]

    for i in range(x):
        # Initializing the rem values with 0's
        rem.append(0)

    for i in range(n):
        if (a[i] < x):
            # perform the remainder operation only if the element is x, as numbers greater than x
            # can't be used to get a sum x.Updating the count of remainders.
            rem[a[i] % x] +=1

    # Traversing the remainder list from start to middle to find pairs
    for i in range(1, x//2):
        if(rem[i] > 0 and rem[x-i]>0):
            # The elements with remainders i and x-i will result in a sum of x. Once we get two
            # elements which add up to x, we print x and break
            # print("Yes")
            return "Yes"
            break
    # Once we reach the middle of remainder array, we have to do operations based on x
    if(i >= x // 2):
        if(x % 2 == 0):
            if (rem[x // 2] > 1):
                # if x is even and we have more than 1 elements with remainder x/2, then we will
                # have two distinct elements which add up to x. if we dont have more than 1 
                # element, print "NO"
                # print("Yes")
                return "Yes"
            else:
                return "No"
                # print("No")
        else:
            # when x is odd we continue the same process which we did in previous loop
            if(rem[x // 2] > 0 and rem[x - x // 2] > 0):
                # print("Yes")
                return "Yes"
            else:
                return "No"
                # print("No")


print("Three Expected:, Actual:", print_pairs_three([ 1, 4, 45, 6, 10, 8 ], 16))
# print("Three Expected, Actual:", print_pairs_three([1, -2, 1, 0, 5], 0))

"""
Similarly, the indices of a pair that add up to a given sum can also be calculated by an 
unordered map. The only change here is that we also have to store indices of elements as values 
for each element as key.

Time Complexity: O(n)
Auxiliary Space: O(n)
"""
def find_sum(arr,target):
        n = len(arr)
        mp ={}
        result =[0] *2

        for i  in range(n):
            findElement = target-arr[i]
            if(findElement in mp):
                result[0] = mp[findElement]
                result[1] = i
                break
            else:
                mp[arr[i]] = i
        return result

ans = find_sum([1,5,4,3,7,9,2],7)
print("aaa:", ans)
# print(f"{min(ans[0], ans[1])} {max(ans[0], ans[1])}")

print("\n my tests \n")
'''

my tests

'''
# Time complexity: O(n^2) | Space complexity: O(1)
def my_tests(arr1, x):
    res =[]
    for i in range(len(arr1)):
        for j in range(i+1, len(arr1)):
            if (arr1[i] +arr1[j]) == x:
                res.append((arr1[i],arr1[j]))
                return True, res
    return False

print("Expected, Actual", my_tests([0, -1, 2, -3, 1], -2))

def my_tests_two(arr, x):
    dic ={}

    for i in range(len(arr)):
        val =x-arr[i]
        if val in dic:
            return True, (val, arr[i])
        dic[arr[i]] =arr[i]

# print("Expected, Actual", my_tests_two([0, -1, 2, -3, 1], -2))
print("Expected, Actual:", my_tests_two([1, -2, 1, 0, 5], 0))