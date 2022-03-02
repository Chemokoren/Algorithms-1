"""
Count of Smaller Numbers after Self | Number of Swaps to Sort | Algorithm Swap

You are given an integer array nums and you have to return a new counts array. The counts
array has the property where counts[i] is the number of smaller elements to the right of
nums[i].

Input:

    [5,2,6,1]

Output:

    [2,1,1,0]

Explanation:

For the number 5, there are 2 numbers smaller than it after it. (2 and 1)

For the number 2, there is 1 number smaller than it after it. (1)

For the number 6, there is also 1 number smaller than it after it. (1)

For the number 1, there are no numbers smaller than it after it.

Hence, we have [2, 1, 1, 0].

Number of swaps to sort

Another way to phrase the question is:

If we sort the array by finding the smallest pair i, j where i < j and a[i] > a[j] how 
many swaps are needed?

To answer that question we just have to sum up the numbers in the above output
array: 2 + 1 + 1 = 5 swaps.

Solution

Explanation
Intuition

The brute force way to solve this question is really easy and intuitive, we simply go 
through the list of elements. For each of the element, we go through the elements after 
it and count how many numbers are smaller than it. This would result in a O(N^2) runtime.
However, this approach is not the optimal solution.

Observe that if we need to reduce our solution's complexity, we will need to count 
multiple numbers' smaller count in one go. This can only be done using some kind of sorted 
order.

But sorting destroys the origin order of the array, what can we do about that?

Recall from introduction of divide and conquer questions, the common approach of tackling 
a divide and conquer question is dividing the data given into two components, assuming 
each components is solved and then try to merge the result.

What if we divide the numbers into two components by index and then sort them separate?

Since we divided the original array by index, after the two components are both sorted, 
all the elements in the left components still have smaller index than any element in the 
right components in the original array.

We can utilize this fact when we combine the two arrays together.

Thus, to solve this problem, we first split the data given into two components, the left 
and the right components. And then we assume that both components' sub-problem are already
solved -- that is we know the count of number smaller than itself for each number for both
components. Now all we need to know is for each number in the left component, how many 
elements are smaller than it in the right component.


This will allow us to know for each number in the left components, how many elements is 
smaller than it in the right component.

Thus, we have successfully solved the problem.

So, what is the run time of our improved solution? We split the problem into two components
each recursion and go through each of the components, and each recursion takes O(N) time 
for the merge process. Thus we have

T(N) = 2T(N/2) + O(N)

This recurrence will yield a total run time of O(N log N).

Implementation

"""
from typing import List

def count_smaller(nums: List[int]) -> List[int]:
    smaller_arr =[0] * len(nums)

    def merge_sort(nums):
        if len(nums) <= 1:
            return nums
        mid  =len(nums) // 2
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])

        return merge(left,right)
    def merge(left, right):
        result =[]
        l, r = 0,0

        while l < len(left) or r < len(right):
            if r >= len(right) or (l < len(left) and left[l][1] <= right[r][1]):
                result.append(left[l])
                smaller_arr[left[l][0]] +=r
                l += 1
            else:
                result.append(right[r])
                r += 1
        return result

    merge_sort(list(enumerate(nums)))
    return smaller_arr

if __name__=='__main__':
    nums =[int(x) for x in input().split()]
    res = count_smaller(nums)
    print(' '.join(map(str, res)))

"""
If the problem asks for number of swaps, we can simple keep a counter each time we swap 
and don't have to keep the array.

"""

from typing import List

def number_of_swaps_to_sort(nums: List[int])->int:

    counts = 0
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])
        return merge(left, right)
    
    def merge(left, right):
        nonlocal counts
        result = []
        l, r = 0, 0

        while l < len(left) or r < len(right):
            if r >= len(right) or (l < len(left) and left[l][1] <= right[r][1]):
                result.append(left[l])
                counts += r
                l += 1
            else:
                result.append(right[r])
                r += 1
        return result
    merge_sort(list(enumerate(nums)))
    return counts

if __name__ =='__main__':
    nums =[int(x) for x in input().split()]
    res = number_of_swaps_to_sort(nums)
    print(res)