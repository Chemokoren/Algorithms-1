# o(n^2) time | o(1) space
my_list =[3, 5, -4, 8, 11, 1, -1, 6, 4]
sum =10
def sumTwoNumbers(array, targetSum):

    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] + array[j] ==targetSum:
                print([array[i], array[j]])
    return []

# O(n) time | O(n) space  =hashtables
def sumTwoNumbers1(array, targetSum):
    nums ={}
    for num in array:
        potentialMatch =targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] =True
    return []

# O(nlog(n)) | O(1) space
def sumTwoNumbers2(array, targetSum):
    array.sort()
    left =0
    right =len(array) -1
    while left < right:
        currentSum =array[left] + array[right]
        if currentSum ==targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


print(sumTwoNumbers2(my_list,sum))
