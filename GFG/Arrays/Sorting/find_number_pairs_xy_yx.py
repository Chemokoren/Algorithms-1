"""
Find number of pairs(x, y) in an array such that x^y > y^x

Given two arrays X[] and Y[] of positive integers, find a number of pairs such that x^y > y^x 
where x is an element from X[] and y is an element from Y[].


    Input: X[] = {2, 1, 6}, Y = {1, 5} 
    Output: 3 
    Explanation: There are total 3 pairs where pow(x, y) is greater than pow(y, x) Pairs 
    are (2, 1), (2, 5) and (6, 1)

    Input: X[] = {10, 19, 18}, Y[] = {11, 15, 9} 
    Output: 2 
    Explanation: There are total 2 pairs where pow(x, y) is greater than pow(y, x) Pairs are
     (10, 11) and (10, 15)

Efficient solution

- The problem can be solved in O(nLogn + mLogn) time. The trick here is if y > x then 
x^y > y^x with some exceptions.

Steps based on this trick
- Sort array Y[]
- For every x in X[], find the index of the smallest number greater than x(also called ceil of x)
in Y[] using binary search, or we can use the inbuilt function upper_bound() in algorithm library
- All the nunbers after idx satisfy the relation so just add(n-idx) to the count.

Base Cases and Exceptions
Following are exceptions for x from X[] and y from Y[]   

    If x = 0, then the count of pairs for this x is 0.
    If x = 1, then the count of pairs for this x is equal to count of 0s in Y[].
    If x>1, then we also need to add count of 0s and count of 1s to the answer.
    x smaller than y means x^y is greater than y^x.
        x = 2, y = 3 or 4
        x = 3, y = 2

Note that the case where x = 4 and y = 2 is not there

Following diagram shows all exceptions in tabular form. The value 1 indicates that the 
corresponding (x, y) form a valid pair.

In the following implementation, we pre-process the Y array and count 0, 1, 2, 3 and 4 in it, 
so that we can handle all exceptions in constant time. The array NoOfY[] is used to store the
counts.

Time Complexity: O(nLogn + mLogn), where m and n are the sizes of arrays X[] and Y[] respectively. 
The sort step takes O(nLogn) time. Then every element of X[] is searched in Y[] using binary
search. This step takes O(mLogn) time.

Auxiliary Space: O(1)

"""
import bisect


# function to return count of pairs with x as one element of the pair.
# It mainly looks for all values in Y where  x ^ Y[i] > Y[i] ^ x
def count(x, Y, n, NoOfY):
    # if x is 0, then there cannot be any value in Y such that
    # x ^ Y[i] > Y[i]^x
    if x == 0:
        return 0
    
    # if x is 1, then the number of pairs is equal to number of zeroes in Y
    if x ==1:
        return NoOfY[0]

    # Find number of elements in Y[] with values greater than x, bisect.bisect_right 
    # gets address of first greater element in Y[0..n-1]
    idx = bisect.bisect_right(Y, x)
    ans = n - idx

    # If we have reached here, then x must be greater than 1, increase number of pairs 
    # for y=0 and y =1
    ans += NoOfY[0] + NoOfY[1]

    # Decrease number of pairs for x = 2 and (y=4 or y =3)
    if x == 2:
        ans -= NoOfY[3] + NoOfY[4]
    
    # Increase number of pairs for x = 3 and y = 2
    if x == 3:
        ans += NoOfY[2]
    return ans

# Function to return count of pairs (x, y) such that x belongs to x,
# y belongs to Y and x^y > y^x
def count_pairs(X, Y):

    m =len(X)
    n =len(Y)

    # To store counts of 0, 1, 2, 3 and 4 in array Y
    NoOfY =[0] * 5
    for i in range(n):
        if Y[i] < 5:
            NoOfY[Y[i]] += 1

    # sort Y so that we can do binary search in it
    Y.sort()
    total_pairs = 0 # initialize result

    # Take every element of X and count pairs with it
    for x in X:
        total_pairs += count(x, Y, n, NoOfY)
    return total_pairs


print("Total pairs = ", count_pairs([2, 1, 6], [1, 5]))




'''
my tests
'''
# Time Complexity: O(M*N) where M and N are sizes of given arrays. 
def my_tests(arr1, arr2):
    res =[]
    count = 0
    for i in range(len(arr1)):

        for j in range(len(arr2)):

            if pow(arr1[i], arr2[j]) > pow(arr2[j],arr1[i]):
                res.append([arr1[i],arr2[j]])
                count +=1

    return count,res

print("Expected: 3 Actual:", my_tests([2, 1, 6], [1, 5]))
print("Expected: 2 Actual:", my_tests([10, 19, 18], [11, 15, 9]))
