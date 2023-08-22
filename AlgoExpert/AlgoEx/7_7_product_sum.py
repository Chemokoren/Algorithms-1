"""
Product Sum - classic recursion question

Find product sum of the special array (consists of numbers or integers and or 
other special arrays)
Product sum - is the sum of all the elements in the array, but when you get to another 
special array like [7,-1] you sum up the numbers of that special array but you multiply
that sum by the depth of that special array.

depth 1 = [5,2,[7,-1],3,[6,[-13,8],4]]
depth 2 = [7,-1], [6,[-13,8],4]
depth 3 = [-13,8]
"""


# O(n) time - is the list of all elements in the array, including those in the subarrays
#  O(d) space where d is the depth of the subarrays
def productSum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier+1)
        else:
            sum += element
    return sum * multiplier


my_array =[5,2,[7,-1],3,[6,[-13,8],4]]
print(productSum(my_array,1))

