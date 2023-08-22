"""

"""
class Solution:
    def moveZeroes(self, nums: int)->None:
        j = 0

        for num in nums:
            if(num != 0):
                nums[j] = num
                j += 1
                print("level:: ", nums)

        for x in range(j, len(nums)):
            nums[x] = 0

my_vals =[0, 1, 3, 0, 12]

sol = Solution()
sol.moveZeroes(my_vals)
print(my_vals)