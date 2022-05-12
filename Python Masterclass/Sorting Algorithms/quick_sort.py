"""
Quick Sort
- Like merge sort, it exploits the fact that arrays of 0 or 1 element are always sorted
- Works by selecting one element(called the "pivot") and finding the index where the pivot should end up in 
the  sorted array
- Once the pivot is positioned appropriately, quick sort can be applied on either side of the pivot

Pivot Helper
-In order to implement merge sort, it's useful to first implement a function responsible for arranging
elements in an array on either side of a pivot
- Given an array, this helper function should designate an element as the pivot
- It should then rearrange elements in the array so that all values less than the pivot are moved to the 
left of the pivot, and all values greater than the pivot are moved to the right of the pivot.
- The order of elements on either side of the pivot doesn't matter
-The helper should do this in place, that is, it should not create a new array
- When complete, the helper should return the index of the pivot

Picking a pivot
- The runtime of quick sort depends in part on how one selects the pivot
- Ideally, the pivot should be chosen so that it's roughly the median value in the data set you're sorting
- For simplicity, we'll always choose the pivot to be the first element(we'll talk about consequences of this
later)

Pivot Pseudocode
- It will help to accept three arguments: an array, a start index, and an end index(these can default to 0 
and the array length minus 1, respectively)

- Grab the pivot from the start of the array
- Store the current pivot index in a variable(this will keep track of where the pivot should end up)
- Loop through the array from the start until the end
    - If the pivot is greater than the current element, increment the pivot index variable and then swap the
    current element with the element at the pivot index
- Swap the starting element(i.e. the pivot ) with the pivot index
- Return the pivot index
"""
