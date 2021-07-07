"""
program for Mean and median of an unsorted array

Given n size unsorted array, find it's mean and median.

Mean of an array = (sum of all elements) / (number of elements)

Median of a sorted array of size n is defined as the middle element when n is odd 
and average of middle two elements when n is even.
Since the array is not sorted here, we sort the array first, then apply above formula.

Input  : a[] = {1, 3, 4, 2, 6, 5, 8, 7}
Output : Mean = 4.5
         Median = 4.5
Sum of the elements is 1 + 3 + 4 + 2 + 6 + 
5 + 8 + 7 = 36
Mean = 36/8 = 4.5
Since number of elements are even, median
is average of 4th and 5th largest elements.
which means (4 + 5)/2 = 4.5

Input  : a[] = {4, 4, 4, 4, 4}
Output : Mean = 4
         Median = 4


Time Complexity to find mean = O(n) 
Time Complexity to find median = O(n Log n) as we need to sort the array first.

"""

# function for calculating mean

def findMean(a, n):
    sum = 0
    for i in range(0, n):
        sum += a[i]
    return float(sum/n)

# Function for calculating median
def findMedian(a, n):
    # First we sort the array
    sorted(a)

    # check for even case
    if n % 2 !=0:
        return float(a[int(n/2)])

    return float((a[int((n-1)/2)] + a[int(n/2)])/2.0)


a = [1, 3, 4, 2, 7, 5, 8, 6,9]
n = len(a)
 
# Function call
print("Mean =", findMean(a, n))
print("Median =", findMedian(a, n))