class ContinuousMedianHandler:
    """
    A class to handle continuous median calculations for a stream of numbers.

    Attributes:
        lowers (Heap): A max-heap to store the lower half of the numbers.
        greaters (Heap): A min-heap to store the upper half of the numbers.
        median (float): The current median value.
    """

    def __init__(self, data):
        """
        Initializes the ContinuousMedianHandler instance with the given data.

        Args:
            data (List[int]): The initial list of numbers.

        Time Complexity: O(n * log(n)) where n is the number of elements in data.
        Space Complexity: O(n) for storing elements in heaps.
        """
        self.lowers = Heap(MAX_HEAP_FUNC, [])
        self.greaters = Heap(MIN_HEAP_FUNC, [])
        self.median = None
        for value in data:
            self.insert(value)

    def insert(self, number):
        """
        Inserts a number into the ContinuousMedianHandler and updates the median.

        Args:
            number (int): The number to be inserted.

        Time Complexity: O(log(n)) where n is the total number of elements in lowers and greaters.
        """
        if not self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):
        """
        Rebalances the heaps to ensure that the size difference is at most 1.
        """
        if self.lowers.length - self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greaters.remove())

    def updateMedian(self):
        """
        Updates the median based on the current state of the heaps.
        """
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()

    def getMedian(self):
        """
        Returns the current median value.

        Returns:
            float: The median value.

        Time Complexity: O(1)
        """
        return self.median


class Heap:
    """
    A class representing a heap data structure.

    Attributes:
        heap (List): The underlying array representing the heap.
        comparisonFunc (Callable): A function used for comparison in the heap.
        length (int): The length of the heap.

    Methods:
        buildHeap: Builds the heap from the given array.
        siftDown: Moves an element down in the heap to maintain heap property.
        siftUp: Moves an element up in the heap to maintain heap property.
        peek: Returns the root element of the heap.
        remove: Removes and returns the root element of the heap.
        insert: Inserts a new element into the heap.
        swap: Swaps two elements in the heap array.
    """

    def __init__(self, comparisonFunc, array):
        """
        Initialize the Heap instance.

        Args:
            comparisonFunc (Callable): A function used for comparison in the heap.
            array (List): The initial array to build the heap from.
        """
        self.heap = self.buildHeap(array)
        self.comparisonFunc = comparisonFunc
        self.length = len(self.heap)

    def buildHeap(self, array):
        """
        Build a heap from the given array.

        Args:
            array (List): The array to build the heap from.

        Returns:
            List: The heap array.
        """
        firstParentIdx = (len(array) - 1) // 2
        for currentIdx in reversed(range(firstParentIdx)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        """
        Move an element down in the heap to maintain heap property.

        Args:
            currentIdx (int): The index of the element to sift down.
            endIdx (int): The index of the last element in the heap.
            heap (List): The heap array.
        """
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1:
                if self.comparisonFunc(heap[childTwoIdx], heap[childOneIdx]):
                    idxToSwap = childTwoIdx
                else:
                    idxToSwap = childOneIdx
            else:
                idxToSwap = childOneIdx
            if self.comparisonFunc(heap[idxToSwap], heap[currentIdx]):
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        """
        Move an element up in the heap to maintain heap property.

        Args:
            currentIdx (int): The index of the element to sift up.
            heap (List): The heap array.
        """
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0:
            if self.comparisonFunc(heap[currentIdx], heap[parentIdx]):
                self.swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx - 1) // 2
            else:
                return

    def peek(self):
        """
        Return the root element of the heap.

        Returns:
            Any: The root element of the heap.
        """
        return self.heap[0]

    def remove(self):
        """
        Remove and return the root element of the heap.

        Returns:
            Any: The root element of the heap.
        """
        valueToRemove = self.heap.pop(0)
        self.length -= 1
        self.siftDown(0, self.length - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        """
        Insert a new element into the heap.

        Args:
            value (Any): The value to insert into the heap.
        """
        self.heap.append(value)
        self.length += 1
        self.siftUp(self.length - 1, self.heap)

    def swap(self, i, j, array):
        """
        Swap two elements in the heap array.

        Args:
            i (int): The index of the first element.
            j (int): The index of the second element.
            array (List): The heap array.
        """
        array[i], array[j] = array[j], array[i]


def MAX_HEAP_FUNC(a, b):
    """
    Comparison function for creating a max heap.

    Args:
        a (Any): The first element.
        b (Any): The second element.

    Returns:
        bool: True if a is greater than b, False otherwise.
    """
    return a > b


def MIN_HEAP_FUNC(a, b):
    """
    Comparison function for creating a min heap.

    Args:
        a (Any): The first element.
        b (Any): The second element.

    Returns:
        bool: True if a is less than b, False otherwise.
    """
    return a < b




my_list =[5, 10, 100, 200, 6, 13, 14]

# # Create an instance of the class
median_handler = ContinuousMedianHandler(my_list)

# # Call getMedian() on the instance
print(median_handler.getMedian())


"""
    A small set of numbers with both positive and negative values.
    An empty set of numbers.
    A single number.
    A set of duplicate numbers.
    Large numbers.

This should ensure that the algorithm is robust and can handle unforeseen scenarios.
"""
import unittest

class TestContinuousMedianHandler(unittest.TestCase):
    def test_continuous_median_handler(self):
        # Test case with a small set of numbers
        data = [5, 10, 100, 200, 6, 13, 14]
        median_handler = ContinuousMedianHandler(data)
        self.assertEqual(median_handler.getMedian(), 13)

        # Test case with an empty set of numbers
        data = []
        median_handler = ContinuousMedianHandler(data)
        self.assertIsNone(median_handler.getMedian())

        # Test case with a single number
        data = [7]
        median_handler = ContinuousMedianHandler(data)
        self.assertEqual(median_handler.getMedian(), 7)

        # Test case with duplicate numbers
        data = [5, 5, 5, 5, 5]
        median_handler = ContinuousMedianHandler(data)
        self.assertEqual(median_handler.getMedian(), 5)

        # Test case with negative numbers
        data = [-10, -5, -3, -1, -20]
        median_handler = ContinuousMedianHandler(data)
        self.assertEqual(median_handler.getMedian(), -5)

        # Test case with large numbers
        data = [10**9, 10**10, 10**11, 10**12, 10**13]
        median_handler = ContinuousMedianHandler(data)
        self.assertEqual(median_handler.getMedian(), 10**11)

if __name__ == "__main__":
    unittest.main()
