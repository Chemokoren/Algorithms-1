from exceptions import Empty

class MinHeap:
    """
    A class that implements a binary min-heap using an array for storage.

    This heap supports operations like:
    - Adding an element while maintaining the heap property.
    - Retrieving the smallest element.
    - Removing the smallest element.
    """

    def __init__(self):
        """
        Initializes an empty heap with a fixed maximum capacity.
        """
        self._capacity = 10  # Maximum number of elements the heap can hold.
        self._elements = [-1] * self._capacity  # Array to store heap elements; initialized with placeholders.
        self._size = 0  # Tracks the current number of elements in the heap.

    def __len__(self):
        """
        Returns the number of elements currently in the heap.
        """
        return self._size

    def is_empty(self):
        """
        Checks if the heap has no elements.

        Returns:
            bool: True if the heap is empty, False otherwise.
        """
        return self._size == 0

    def get_min(self):
        """
        Retrieves the smallest element (root) of the heap.

        Returns:
            int: The smallest element in the heap.

        Raises:
            Empty: If the heap is empty.
        """
        if self._size == 0:
            raise Empty("The heap is empty.")  # Error if the heap has no elements.
        return self._elements[1]  # Root element is always at index 1.

    def add(self, value):
        """
        Adds a new element to the heap, maintaining the heap property.

        Args:
            value (int): The value to be added.

        Raises:
            Empty: If the heap is at full capacity.
        """
        if self._size == self._capacity:
            raise Empty("Heap is at full capacity.")  # Error if the heap is full.

        self._size += 1  # Increment the size of the heap.
        position = self._size  # Start at the last position.

        # Bubble up: Place the new element in the correct position by comparing with its parent.
        while position > 1 and value < self._elements[position // 2]:
            self._elements[position] = self._elements[position // 2]  # Move the parent down.
            position //= 2  # Move up to the parent's position.

        self._elements[position] = value  # Place the new element in its correct position.

    def remove_min(self):
        """
        Removes and returns the smallest element (root) from the heap.

        Returns:
            int: The smallest element removed from the heap.

        Raises:
            Empty: If the heap is empty.
        """
        if self._size == 0:
            raise Empty("The heap is empty.")  # Error if there are no elements to remove.

        min_value = self._elements[1]  # The root element (smallest value).
        last_value = self._elements[self._size]  # Last element in the heap.
        self._size -= 1  # Reduce the size of the heap.

        position = 1  # Start from the root.
        child_position = 2  # Left child of the root.

        # Bubble down: Place the last element in the correct position by comparing with its children.
        while child_position <= self._size:
            # Find the smaller of the two children.
            if child_position < self._size and self._elements[child_position] > self._elements[child_position + 1]:
                child_position += 1
            # If the last element is smaller than or equal to the smaller child, stop.
            if last_value <= self._elements[child_position]:
                break
            self._elements[position] = self._elements[child_position]  # Move the smaller child up.
            position = child_position  # Move down to the child's position.
            child_position *= 2  # Move to the next level.

        self._elements[position] = last_value  # Place the last element in its correct position.
        return min_value  # Return the smallest element.

# Example usage of the MinHeap.
heap = MinHeap()

# Add elements to the heap.
heap.add(25)
heap.add(14)
heap.add(2)
heap.add(20)
heap.add(10)
heap.add(12)

# Print and remove elements in sorted order.
while not heap.is_empty():
    print(heap.remove_min(), end=', ')
