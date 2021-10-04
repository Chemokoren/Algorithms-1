# approach 1

# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    for i in range(len(array) -1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]

            if firstNum +secondNum ==targetSum:
                return [firstNum, secondNum]
    return []

# approach 2
#O(n) time | O(n) space

def twoNumberSumTwo(array, targetSum):
    nums ={}
    for num in array:
        potentialMatch = targetSum-num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


# approach 3
# O(nlog(n)) time | O(1) space
def twoNumberSumThree(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        potentialSum = array[left] +array[right]

        if(potentialSum == targetSum):
            return [array[left], array[right]]
        elif potentialSum < targetSum:
            left += 1
        elif potentialSum > targetSum:
            right -= 1
    return []



my_array =[3, 5, -4, 8, 11, 1, -1, 6]
my_target = 10

print(twoNumberSumThree(my_array, my_target))