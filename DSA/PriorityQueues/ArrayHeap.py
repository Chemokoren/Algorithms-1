from exceptions import Empty

class ArrayHeap:
    def __init__(self) -> None:
        self._maxsize = 10
        self._data =[-1] * self._maxsize
        self._currentsize = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def maxh(self):
        if self._currentsize == 0:
            raise Empty('Heap is empty')
        return self._data[1]

    def insert(self, e):
        """
        Insert an element into the binary max-heap and maintain the heap property.

        This method performs the following steps:
        1. Checks if the heap has space to add a new element.
        2. Inserts the new element at the next available position.
        3. Percolates the new element up to its correct position to restore the heap property.

        Args:
            e: The element to be inserted into the heap.

        Raises:
            Empty: If the heap is full and cannot accommodate more elements.
        """
        # Step 1: Check if the heap is full
        if self._currentsize == self._maxsize:
            raise Empty('No Space')  # Raise an exception if the heap has no space

        # Step 2: Increment the current size of the heap
        self._currentsize += 1  # Update the size to include the new element
        i = self._currentsize  # Start at the new position (last position in the heap)

        # Step 3: Percolate the element up to maintain the heap property
        # While not at the root and the element is greater than its parent
        while i != 1 and e > self._data[i // 2]:
            self._data[i] = self._data[i // 2]  # Move the parent down
            i = i // 2  # Move up to the parent's position

        # Step 4: Place the new element in its correct position
        self._data[i] = e  # The correct position for the new element


    def deletemax(self):
        """
        Remove and return the maximum element (root) from the binary max-heap.

        This method performs the following steps:
        1. Check if the heap is empty; raise an exception if it is.
        2. Store the root element (maximum value) to return later.
        3. Replace the root with the last element in the heap.
        4. Decrement the size of the heap.
        5. Restore the heap property by percolating down the replaced element.

        Returns:
            The maximum element (root) of the heap.

        Raises:
            Empty: If the heap is empty when the method is called.
        """
        # Step 1: Check if the heap is empty
        if self._currentsize == 0:
            raise Empty('Heap is Empty')  # Raise an exception if no elements exist in the heap

        # Step 2: Store the root element (maximum value) for return
        x = self._data[1]  # The maximum element is at the root (index 1 in a 1-based index heap)

        # Step 3: Replace the root with the last element in the heap
        y = self._data[self._currentsize]  # Last element in the heap
        self._currentsize -= 1  # Decrease the size of the heap by 1

        # Step 4: Start the percolation process from the root
        i = 1  # Current index (start at root)
        ci = 2  # Child index (left child of root)

        # Step 5: Percolate down to restore the heap property
        while ci <= self._currentsize:  # Loop as long as there is at least one child
            # Check if the right child exists and is greater than the left child
            if ci < self._currentsize and self._data[ci] < self._data[ci + 1]:
                ci += 1  # Move to the right child

            # If the current element (y) is larger than the greater child, stop
            if y >= self._data[ci]:
                break

            # Move the larger child up to the current position
            self._data[i] = self._data[ci]

            # Update indices to move down the heap
            i = ci  # Move current index to child index
            ci = ci * 2  # Calculate new child index (left child of current index)

        # Place the element (y) at its correct position
        self._data[i] = y

        # Return the maximum element
        return x

h = ArrayHeap()
h.insert(25)
h.insert(14)
h.insert(2)
h.insert(20)
h.insert(10)
h.insert(12)
print(h._data)
h.deletemax()
print(h._data)


"""
Explanation: insert
Key Variables:

    e: The new element to be added to the heap.
    self._currentsize: Tracks the number of elements currently in the heap.
    i: Represents the position of the new element during the percolation process.

Logic Summary:

    The method ensures the heap is not full before attempting to insert the new element.
    After placing the element at the next available position, it "bubbles up" the element to its proper position by repeatedly swapping it with its parent if it's larger.
    This guarantees that the max-heap property (parent is always greater than or equal to its children) is maintained.
    
    
Explanation: deletemax

    Clear Variable Explanations:
        x: Stores the maximum value to be returned.
        y: The last element in the heap, which is moved to restore the heap property.
        i: Tracks the current position during percolation.
        ci: Tracks the index of the larger child during percolation.


"""
