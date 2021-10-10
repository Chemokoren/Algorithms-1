"""
Permutations

"""

def swap(array, i, j):
    array[i],array[j] = array[j],array[i]
# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def getPermutations(array):
    permutations =[]
    permutationsHelper(array,[],permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i]+array[i+1:] # O(n)
            newPermutation =currentPermutation + [array[i]] # O(n)
            permutationsHelper(newArray, newPermutation, permutations)

# approach 2
def getPermutationsTwo(array):
    permutations =[]
    permutationsHelperTwo(0,array, permutations)
    return permutations

def permutationsHelperTwo(i, array, permutations):
    if i == len(array) -1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationsHelperTwo(i+1, array, permutations)
            swap(array, i, j)

my_array =[1,2,3]
print(getPermutationsTwo(my_array))