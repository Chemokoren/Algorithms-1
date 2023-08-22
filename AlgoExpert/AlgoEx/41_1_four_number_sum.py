"""
four number sum
worst case (time) :O(n^3) for the case where: -4,-3,-2,-1,0,1,2,3,4

assignment: three number sum

"""

# O(n^2)  time | O(n^2) space
def fourNumberSum(array, targetSum):
    allPairSums ={}
    quadruplets =[]
    for i in range(1, len(array) -1):
        for j in range(i+1, len(array)):
            currentSum =array[i] + array[j]
            difference = targetSum - currentSum

            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair+[array[i], array[j]])

        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] =[[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets

my_array =[7,6,4,-1,1,2]
target_val =16

print(fourNumberSum(my_array, target_val))