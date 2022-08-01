from typing import List
import heapq

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

# nums =[3,2,3,1,2,4,5,5,6]
# k = 4
# sol = Solution()
# print(sol.findKthLargest("using option 1:", sol.findKthLargest(nums, k)))
# sol.findKthLargest("using quick select", sol.findKthLargest(nums, k))


"""
You are given an array of strings, nums, and an integer k. Each string in nums represents an integer
without leading zeros.
Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is
the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

Example 1:
Input: nums = ["3","6","7","10"], k =4
Output: "3"
Explanation: The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
             The 4th largest integer in nums is "3"

Example 2:
Input: nums =["2","21","12","1"], k=3
Output: "2"
Explanation:
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3rd largest integer in nums is "2".


"""

class Solution:
    def kthLargestNumber(self, nums: List[str],k:int)->str:
        maxHeap =[-int(n) for n in  nums]
        y = heapq.heapify(maxHeap)

        while k > 1:
            heapq.heappop(maxHeap)
            k -=1
        return str(-maxHeap[0])

nums,k  = ["3","6","7","10"], 4
nums,k =["2","21","12","1"], 3
soln = Solution()
print(soln.kthLargestNumber(nums, k))

'''
my tests

'''
def findKthLargest1(nums, k):
    nums.sort()
    return nums[len(nums)-k]


print("Expected:5, Actual:",findKthLargest1([3,2,1,5,6,4],2))
print("Expected:4, Actual:",findKthLargest1([3,2,3,1,2,4,5,5,6],4))


def find_kth_largest(nums,k):
    nums.sort(reverse=True)
    return nums.index(k-1)
print("Index Expected:5, Actual:",find_kth_largest([3,2,1,5,6,4],2))
print("Index Expected:4, Actual:",find_kth_largest([3,2,3,1,2,4,5,5,6],4))