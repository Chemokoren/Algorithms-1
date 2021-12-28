"""
Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
input: nums = [3,2,1,5,6,4], k =2
Output: 5

Example 2:
input: nums = [3,2,3,1,2,4,5,5,6], k =4
Output: 4

Constraints:
1 <= k <= nums.length <=10^4
-10^4 < nums[i] <= 10^4

"""


class Solution:

    # def findKthLargest1(self, nums, k):
    #     nums.sort()
    #     return nums
        # return nums[len(nums)-k]

    def findKthLargest(self, nums, k):
        k = len(nums) - k

        def quickSelect(l,r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] =nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k: return quickSelect(l, p-1)
            if p < k: return quickSelect(p+1, r)
            else: return nums[p]

nums =[3,2,3,1,2,4,5,5,6]
k = 4
sol = Solution()
print(sol.findKthLargest("using option 1:", sol.findKthLargest(nums, k)))
# sol.findKthLargest("using quick select", sol.findKthLargest(nums, k))
