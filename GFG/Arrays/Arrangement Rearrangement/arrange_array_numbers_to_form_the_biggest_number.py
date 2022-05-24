"""
Arrange given numbers to form the biggest number | Set 1

Given an array of numbers, arrange them in a way that yields the largest value. 
For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 
gives the largest value. And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, 
then the arrangement 998764543431 gives the largest value.

A simple solution that comes to our mind is to sort all numbers in descending order,
but simply sorting doesn’t work. For example, 548 is greater than 60, but in output 60
comes before 548. As a second example, 98 is greater than 9, but 9 comes before 98 in output.

So how do we go about it? The idea is to use any comparison based sorting algorithm. 
In the used sorting algorithm, instead of using the default comparison, 
write a comparison function myCompare() and use it to sort numbers. 

Given two numbers X and Y, how should myCompare() decide which number to put first 
– we compare two numbers XY (Y appended at the end of X) and YX (X appended at the end of Y).
If XY is larger, then X should come before Y in output, else Y should come before. 
For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542. 
Since 60542 is greater than 54260, we put Y first.

Following is the implementation of the above approach. 
To keep the code simple, numbers are considered as strings, the vector is used instead of
a normal array. 

Time Complexity:  O(nlogn) ,sorting is considered to have running time complexity of O(nlogn) and the for loop runs in O(n) time.
Auxiliary Space: O(1).
"""

# program to get hte maximum possible integer from given array of integers
# custom comparator to sort according to the ab, ba, as mentioned in description

def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return ((int(ba) >
             int(ab)) -
            (int(ba) <
             int(ab)))


def myCompare(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K




if __name__ =='__main__':
    a = [54, 546, 548, 60]
    sorted_array =sorted(a, key=myCompare(comparator))
    number ="".join([str(i) for i in sorted_array])
    print(number)


print("\n Another approach:(using itertools) \n")

"""
Another approach:(using itertools) 

Using the inbuilt library of the Python, itertools library can be used to perform this task.

Time Complexity:  O(n!)
Auxiliary Space: O(1).

"""


from itertools import permutations
def largest(l):
    lst =[]
    for i in permutations(l,len(l)):
        # provides all permulations of the list values, store them in list to find max
        lst.append("".join(map(str,i)))
    return max(lst)

print(largest([54, 546, 548, 60])) #Output 6054854654


'''
In the first case, we allowed strings input but in case strings are restricted then also we can solve 
the problem using long long int to find biggest arrangement. The only limitation is that we cannot store
numbers greater than 10^18. In case it exceeds that, this solution won't work.
'''

# given an array of numbers, program to arrange the numbers to form the largest number
# A comparison function which is used by sort in printLargest()

from functools import cmp_to_key

def myCompare(X, Y):
    # assign X to XY since XY starts with X first
    # assign Y to YX since YX starts with Y first
    XY, YX, revX, revY = X,Y,0,0

    # reverse X and assign to revX
    while(X):
        revX = revX * 10 + X % 10
        X = (X//10)

    # reverse Y and assign to revY
    while(Y):
        revY = revY *10 + Y % 10
        Y =(Y//10)

    # first append Y at the end of X
    while(revY):
        XY = XY *10 + revY % 10
        revY =(revY // 10)
    # then append X at the end of Y
    while(revX):
        YX = YX * 10 + revX%10
        revX =(revX // 10)

    # Now see which of the two formed numbers is greater
    return YX - XY

# The main function that prints the arrangement with the largest value. The function accepts a vector
# of strings
def printLargest(arr):
    # sort the numbers using library sort function. The function uses our comparison function
    # myCompare() to compare two strings
    arr.sort(key=cmp_to_key(myCompare))
    for i in range(len(arr)):
        print(arr[i], end="")

    
arr =[]
arr.append(54)
arr.append(546)
arr.append(548)
arr.append(60)
print("expected:6054854654, \nactual:")
printLargest(arr)