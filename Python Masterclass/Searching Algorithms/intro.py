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

Big O of Binary Search
- Worst and Average Case - O(log n) 
- Best Case O(1)


Naive String Search
-Suppose you want to cont the number of times a smaller string appears in a longer string
- A straightforward approach involves checking pairs of characters individually.

Pseudocode
- Loop over the longer string
- Loop over the shorter string
- If the characters don't match break out of the inner loop
- If the characters do match, keep going
- If you complete the inner loop and find a match, increment the count of matches
- Return the count
"""

def naiveSearch(long_str, search_val):
    match_count =0
    for i in range(len(long_str)):
        for j in range(len(search_val)):
            print(long_str[i+j],search_val[j])
            if long_str[i+j]!=search_val[j]:
                print("BREAK")
                break
            if j ==len(search_val)-1:
                match_count +=1
    return match_count

print("expected is 2: actual is", naiveSearch("harold said haha in hamburg", "r"))

