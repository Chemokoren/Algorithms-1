'''
naive recursive solution
upper Bound: O((n*(2n)!/(n!(n+1)!))) time

'''
def numberOfBinaryTreeTopologies(n):
    if n == 0:
        return 1
    numberOfTrees =0
    for leftTreeSize in range(n):
        rightTreeSize =n-1-leftTreeSize
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
        numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize)
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
    return numberOfTrees


'''
cached recursive solution
O(n^2) time | O(n) space
'''
def numberOfBinaryTreeTopologies1(n, cache ={0: 1}):
    if n in cache:
        return cache[n]
    numberOfTrees =0

    for leftTreeSize in range(n):
        rightTreeSize =n-1-leftTreeSize
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize, cache)
        numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize, cache)
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
    cache[n] =numberOfTrees
    return numberOfTrees

'''
iterative solution
O(n^2) time | O(n) space

'''
def numberOfBinaryTreeTopologies2(n):
    cache =[1]
    for m in range(1, n+1):
        numberOfTrees =0
        for leftTreeSize in range(m):
            rightTreesize =m -1 -leftTreeSize
            numberOfLeftTrees =cache[leftTreeSize]
            numberOfRightTrees =cache[rightTreesize]
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees
        cache.append(numberOfTrees)
    return cache[n]

if __name__=='__main__':
    print(numberOfBinaryTreeTopologies(3))
