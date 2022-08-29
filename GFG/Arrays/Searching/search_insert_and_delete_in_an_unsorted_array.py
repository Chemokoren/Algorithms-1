"""
How to search, insert, and delete in an unsorted array

Search operation:
- In an unsorted array, the search operation can be performed by linear traversal from the first
element to the last element

"""
# Time Complexity: O(N) | Auxiliary Space: O(1)
def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

print(search([12, 34, 10, 6, 40 ], 40))

"""
Insert at the end
In an unsorted array, the insert operation is faster compared to a sorted array because we 
on't have to care about position at which the element is placed.
"""
# Time Complexity: O(1) | Auxiliary Space: O(1)
def insert_at_end(arr, key):
    arr.append(key)
    return arr

print(insert_at_end([12, 34, 10, 6, 40 ], 80))

"""
Insert at any position

Insert operation in an array at any position can be performed by shifting elements to the right,
which are on the right side of the required position.

"""
def insert_any(arr, pos, val):
    start =0

    # while start <pos:
    #     start +=1

    # new_idx = start +1

    # temp =arr[start]
    # arr[start] =val
    # start +=1

    # while start< len(arr)-1:
    #     arr[start] =temp
    #     start +=1
    #     temp =arr[start]
    arr.insert(pos,val)
    return arr

print(insert_any([12, 34, 10, 6, 40 ],2, 80))

"""
Delete Operation

In the delete operation, the element to be deleted is searched using linear search, and then the
delete operation is performed followed by shifting the elements.

"""
# Time Complexity: O(N)  | Auxiliary Space: O(1)
def delete_arr_val(arr,val):
    arr.remove(val)
    return arr

print("Expected: [12,10, 6, 40 ], Actual:", delete_arr_val([12, 34, 10, 6, 40 ], 34))


