"""
Objectives
- Describe what a searching algorithm is
- implement linear search on arrays
- Implement binary search on sorted arrays
- Implement a naive string searching algorithm
- Implement the KMP string searching algorithm

Linear Search
-This function accepts an array and a value
- Loop through the array and check if the current array element is equal to the value
- if it is, return the index at which the element is found
- if the value is never found, return -1

Big O of linear search
- best case O(1)
- average case O(n)
- Worst case O(n)

Binary Search
- Binary search is a much faster form of search
- Rather than eliminating one element at a time, you can eliminate half of the remaining elements at a time
- Binary search only works on sorted arrays!
- it uses divide and conquer

Binary Search Pseudocode
- This function accepts a sorted array and a value
- Create a left pointer at the start of the array, and a right pointer at the end of the array
- While the left pointer comes before the right pointer:
    - Create a pointer in the middle
    - If you find the value you want, return the index
    - If the value is too small, move the left pointer up
    - If the value is too large, move the right pointer down
- If you never find the value, return -1
"""