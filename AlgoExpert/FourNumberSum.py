# def fourNumberSum(array, targetSum):
#     global current_val, first_val, second_val, third_val, fourth_val
#     for i in range(len(array) - 1):
#         for j in range(i + 1, len(array) - 1):
#             first_val = array[i]
#             second_val = array[j]
#         for k in range(i + 2, len(array) - 1):
#             third_val = array[k]
#             current_val += third_val
#         for m in range(i + 3, len(array) - 1):
#             fourth_val = array[m]
#             current_val += fourth_val
#         if (current_val) == targetSum:
#             print([first_val, second_val, third_val, fourth_val])
#     return []
def fourNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array) - 1):
                for m in range(k + 1, len(array) - 1):
                    if (array[i]+array[j]+array[k]+array[m]) == targetSum:
                        print([array[i],array[j],array[k],array[m]])
    return []

def fourNumberSum1(array,targetSum):
    array.sort()
    left =0
    left1 =1
    right =len(array)-1
    right1 =len(array)-2
    while left <right and left1 < right1:
        currentSum =array[left]+array[left1]+array[right]+array[right1]
        if currentSum == targetSum:
            return [array[left],array[left1],array[right],array[right1]]
        if currentSum < targetSum:
            left +=1
            left1 +=1
        if currentSum > targetSum:
            right +=1
            right1 +=1
    return []

# O(n ^ 2 ) time | O(n ^ 2) space
def fourNumberSum2(array, targetSum):
    allPairSums ={}
    quadruplets =[]
    for i in range(1, len(array) - 1):
        for j in range(i +1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0,i):
            currentSum =array[i] +array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] =[[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k],array[i]])
    return quadruplets


# my_array = [7, 6, 4, -1, 1, 2]
my_array = [7, 6, 4, -1, 1, 2]
sum = 16
print(fourNumberSum2(my_array, sum))

# [1, 2, 7, 6], [7, 6, 4, -1]
