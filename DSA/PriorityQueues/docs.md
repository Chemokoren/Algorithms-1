# Queues
- Queues collection of objects follows FIFO e.g. Customers waiting for service
- FIFO policy  does no suite many real applications e.g. Air Traffic control
- Though FIFO policy is reasonable, some situations require objects to be prioritized
- This is achieved through Priority Queues
### Priority Queues
- Priority Queues is a Collection of prioritized Objects or Elements 
- Allows element insertion
- Removal of element is based on priority
- A key is associated when element is inserted in the priority queue
- Element with minimum key will be next element to be removed
- 
### Heaps
- heap is an efficient realization of Priority Queue
- Heap is a Binary Tree
- Relational Property:
  - In a heap the value in each node is greater than or equal to  those in its children (Max Heap)
  - In a heap the value in each node is less than or equal to  those in its children (Min Heap)
- Structural Property
  - Heap is a complete binary tree
- Max Heap and Min Heap

# Heap ADT
- Heap ADT stores prioritized objects
- Members:
  - MaxSize
  - CurrentSize
  - HeapList
- Operations
  - insert(Object) : insert element
  - deleteMax(): remove & return element
  - max(): return root element
  - len(): returns number of elements
  - isEmpty(): whether stack is empty or not
# Code Walkthrough
"""
This function implements the insert operation for a binary max-heap data structure. Here's a detailed breakdown:

def insert(self, e):

        if self._currentsize == self._maxsize:
            raise Empty('No Space')

        self._currentsize +=1
        i = self._currentsize
        while i!=1 and e >self._data[i//2]:
            self._data[i] = self._data[i//2]
            i = i//2
        self._data[i] = e
"""
## Function Purpose:

The insert method adds an element e into a binary max-heap while maintaining the heap property:
"The value of each node is greater than or equal to the values of its children."

## Code Explanation:

    ### 1. Check for Space in the Heap:
    """
    if self._currentsize == self._maxsize:
    raise Empty('No Space')

    """
The method ensures that the heap has space for the new element.
If the heap is full (current size equals maximum size), an Empty exception is raised.

    ### 2. Increment the Current Size:
    self._currentsize += 1
    i = self._currentsize

The current size of the heap (_currentsize) is incremented to account for the new element being added.
i is initialized to the index where the new element will be placed.

    ### 3. Shift Elements Up (Heapify-Up):
    
    while i != 1 and e > self._data[i // 2]:
        self._data[i] = self._data[i // 2]
        i = i // 2
Purpose: To maintain the max-heap property:

    If e (the new element) is greater than its parent (self._data[i // 2]), it should move up the tree.

Steps:

    The loop continues as long as i != 1 (not at the root) and e is greater than its parent.
    The parent is moved down to the current position (self._data[i]).
    Update i to the parent's index (i // 2), effectively moving e up the tree.

    ### 4. Insert the New Element in the Correct Position:
    self._data[i] = e
When the loop finishes, i points to the correct position for the new element e.
e is placed there.

Example Walkthrough:
Initial State:

    _data: [None, 40, 30, 20] (using 1-based indexing; None is a placeholder at index 0).
    _currentsize: 3
    _maxsize: 5

Insert 50:

    Space Check: There's space, since _currentsize < _maxsize.
    Increment Size: _currentsize = 4, i = 4.
    Heapify-Up:
        e = 50 > self._data[4 // 2] = 20: Move 20 down.
        e = 50 > self._data[2 // 2] = 40: Move 40 down.
    Final Position:
        Insert 50 at index 1.

Final State:

    _data: [None, 50, 40, 20, 30]

Key Points:

    Heapify-Up ensures that the max-heap property is maintained after insertion.
    Time Complexity: O(logn), where n is the number of elements in the heap (height of the heap).
    Space Complexity: O(1), as the operation is done in-place.

# deletemax: explain the following code

The deletemax function implements the delete operation for a binary max-heap, specifically for removing 
the maximum element (the root) while maintaining the heap property.

## Function Purpose:

The method removes and returns the maximum element of a binary max-heap. The max-heap property 
ensures the root (the first element) is the maximum value.

    def deletemax(self):
        if self._currentsize == 0:
            raise Empty('Heap is Empty')
        x = self._data[1]
        y = self._data[self._currentsize]
        self._currentsize -= 1
        i = 1
        ci =2
        while ci <= self._currentsize:
            # checking which child is greater
            if ci < self._currentsize and self._data[ci] < self._data[ci+1]:
                ci += 1
                # checking if the last element is greater than its child
                if y >= self._data[ci]:
                    break
                self._data[i] = self._data[ci]
                i = ci
                ci = ci * 2
            self._data[i] =y

Code Explanation:

    Check if the Heap is Empty:

if self._currentsize == 0:
    raise Empty('Heap is Empty')

    If _currentsize is 0, the heap is empty, and an Empty exception is raised.

Save the Maximum Element:

x = self._data[1]

    The root of the heap (self._data[1]) is the maximum value in the heap. This value is saved in x to return later.

Replace the Root with the Last Element:

y = self._data[self._currentsize]
self._currentsize -= 1

    The last element in the heap (self._data[self._currentsize]) is stored in y.
    The heap size is reduced by 1 (_currentsize -= 1), effectively removing the last element from the heap.

Initialize Position Pointers:

i = 1
ci = 2

    i: Index of the current node being adjusted (starting at the root).
    ci: Index of the left child of the current node (2 * i).

Heapify-Down (Reheapify):

while ci <= self._currentsize:

    The loop ensures we stay within the valid range of the heap.

    Step 1: Select the Larger Child:

if ci < self._currentsize and self._data[ci] < self._data[ci+1]:
    ci += 1

    If the right child exists (ci + 1 <= _currentsize) and is larger than the left child, update ci to the index of the right child (ci + 1).

Step 2: Compare Parent with Larger Child:

if y >= self._data[ci]:
    break

    If y (the replacement value) is larger than or equal to the larger child, the heap property is satisfied, and the loop breaks.

Step 3: Move the Larger Child Up:

    self._data[i] = self._data[ci]
    i = ci
    ci = ci * 2

        Move the larger child into the parent's position (self._data[i] = self._data[ci]).
        Update i to the child's index (ci), and set ci to the index of the left child (2 * i).

Insert the Replacement Value:

self._data[i] = y

    Once the correct position for y is found, insert it into the heap.

Return the Maximum Element:

    return x

        Return the saved maximum element (x).

Example Walkthrough:
Initial State:

    _data: [None, 50, 40, 30, 20] (max-heap; 1-based indexing).
    _currentsize: 4.

Delete Max:

    Check if Empty: The heap is not empty.
    Save Maximum: x = 50 (the root).
    Replace Root: Replace 50 with 20 (the last element); _currentsize = 3.
        _data: [None, 20, 40, 30].
    Heapify-Down:
        Compare 20 with its children (40 and 30):
            Larger child is 40 (at index 2).
            Move 40 up: _data[1] = 40.
        Compare 20 with its new children (None):
            Insert 20 at index 2.

Final State:

    _data: [None, 40, 20, 30].
    Returned Value: 50.

Key Points:

    Heapify-Down ensures the heap property is maintained after removing the root.
    Time Complexity: O(logn), where nn is the number of elements in the heap (height of the heap).
    Space Complexity: O(1), as the operation is done in-place.