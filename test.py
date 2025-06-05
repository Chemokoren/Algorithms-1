from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(list(set(nums)))
        final = []
        i = 0
        j = 1
        k = len(nums) - 1
        while j < len(nums) - 1 and k > j:
            temp = nums[i] + nums[j] + nums[k]
            if (temp == 0):
                print(f"aa::{nums}")
                final.append([nums[i], nums[j], nums[k]])
            elif temp > 0:
                k -= 1
            else:
                j += 1

        return final

sol = Solution()
print("Expected:: [[-1,-1,2],[-1,0,1]], Actual::", sol.threeSum([-1,0,1,2,-1,-4]))