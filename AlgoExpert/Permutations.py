# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def getPermutations(array):
    permutations =[]
    permutationsHelper(array,[], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray =array[:i] +array[i + 1:]
            newPermutation = currentPermutation +[array[i]]
            permutationsHelper(newArray, newPermutation,permutations)

# second approach
# O(n * n!) time | O(n*n!) space
def getPermutations2(array):
    permutations =[]
    permutationsHelper(0,array, permutations)
    return permutations

def permutationsHelper2(i, array, permutations):
    if i == len(array) -1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationsHelper(i+1, array, permutations)
            swap(array, i, j)
def swap(array, i, j):
    array[i],array[j] = array[j], array[i]
