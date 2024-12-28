from exceptions import Empty


class LinkedQueue:
    """A queue implementation using a singly linked list.

    This implementation provides O(1) time complexity for enqueue and dequeue operations.
    """

    class _Node:
        """A lightweight private class to represent a single node in the linked list."""
        __slots__ = '_element', '_next'  # Reduce memory overhead for instances.

        def __init__(self, element, next) -> None:
            """
            Initialize a node with an element and a reference to the next node.

            :param element: The data stored in the node.
            :param next: Reference to the next node in the list.
            """
            self._element = element
            self._next = next

    def __init__(self) -> None:
        """Initialize an empty queue."""
        self._head = None  # Points to the first node in the queue.
        self._tail = None  # Points to the last node in the queue.
        self._size = 0  # Tracks the number of elements in the queue.

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Check if the queue is empty.

        :return: True if the queue has no elements, otherwise False.
        """
        return self._size == 0

    def enqueue(self, e):
        """
        Add an element to the end of the queue.

        :param e: The element to add to the queue.
        """
        new_node = self._Node(e, None)  # Create a new node with the given element.

        if self.is_empty():
            self._head = new_node  # If the queue is empty, the new node is also the head.
        else:
            self._tail._next = new_node  # Link the new node to the end of the queue.
        self._tail = new_node  # Update the tail to the new node.
        self._size += 1  # Increment the size of the queue.

    def dequeue(self):
        """
        Remove and return the first element from the queue.

        :raises Empty: If the queue is empty.
        :return: The element at the front of the queue.
        """
        if self.is_empty():
            raise Empty('Queue is Empty')  # Cannot dequeue from an empty queue.
        value = self._head._element  # Store the element to return.
        self._head = self._head._next  # Move the head to the next node.
        self._size -= 1  # Decrement the size of the queue.
        if self.is_empty():
            self._tail = None  # If the queue is now empty, reset the tail.
        return value

    def first(self):
        """
        Return the first element of the queue without removing it.

        :raises Empty: If the queue is empty.
        :return: The element at the front of the queue.
        """
        if self.is_empty():
            raise Empty('Queue is Empty')  # No first element in an empty queue.
        return self._head._element

    def display(self):
        """Print the elements of the queue in order."""
        temp = self._head
        while temp:
            print(temp._element, end=" --> ")  # Print the element followed by an arrow.
            temp = temp._next
        print("")  # Indicate the end of the queue.


# Example usage of the LinkedQueue class
if __name__ == "__main__":
    q = LinkedQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.display()  # Expected output: 10 --> 20 --> None
    print('Length: ', len(q))  # Expected output: Length: 2
    print('Dequeue: ', q.dequeue())  # Expected output: Dequeue: 10
    q.display()  # Expected output: 20 --> None
    q.enqueue(30)
    q.enqueue(40)
    q.display()  # Expected output: 20 --> 30 --> 40 --> None
    print('First Element: ', q.first())  # Expected output: First Element: 20
    q.display()  # Expected output: 20 --> 30 --> 40 --> None
    print('Dequeue: ', q.dequeue())  # Expected output: Dequeue: 20
    q.display()  # Expected output: 30 --> 40 --> None
