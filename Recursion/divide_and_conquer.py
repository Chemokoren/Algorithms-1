"""
Divide & Conquer
- Divide problem into several smaller subproblems. Normally, the subproblems 
are similar to the original.
- Conquer the subproblems by solving them recursively
Base case: solve small enough problems by brute force
- Combine the solutions to get a solution to the subproblems And finally a solution 
to the original problem.
- Divide and Conquer algorithms are normally recursive 
"""

# binary search
def binary_search(nums, target):

    def bs(start, end, nums, target):

        while start <= end:
            mid = (start + end) // 2

            if target > nums[mid]:
                return bs(mid +1, end, nums, target)
            elif target < nums[mid]:
                return bs(start, mid -1, nums, target)
            elif target == nums[mid]:
                return nums[mid]
        return False
    return bs(0, len(nums)-1, nums, target)
    
print(binary_search([1,2,3,4,5,6,7], 7))