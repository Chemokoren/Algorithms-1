# O(n*2^n) time | O(n*2^n) space
def powerset(array):
    subsets =[[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset =subsets[i]
            subsets.append(currentSubset +[ele])
    return subsets

# O(n*2^n) time | O(n*2^n) space
def powerset1(array, idx =None):
    if idx is None:
        idx =len(array) -1
    elif idx < 0:
        return [[]]
    ele =array[idx]
    subsets =powerset1(array, idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets
