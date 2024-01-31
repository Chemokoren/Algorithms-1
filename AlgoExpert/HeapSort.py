"""
A conceptual overview of the HeapSort algorithm

The provided algorithm implements heap sort, a comparison-based sorting algorithm that leverages the heap data structure to achieve efficient sorting. Here's a conceptual overview of how the algorithm works:

    Building a Max Heap:
        The first step of the heap sort algorithm is to build a max heap from the input array.
        It involves rearranging the elements of the array so that they satisfy the heap property: for every node i, the value of the parent node is greater than or equal to the values of its children.
        The buildMaxHeap function iterates through the input array, starting from the last parent node and moving up to the root, and performs the sift-down operation to ensure that each subtree rooted at a parent node satisfies the heap property.

    Sorting the Heap:
        Once the max heap is constructed, the algorithm proceeds to sort the elements in ascending order.
        The sorting phase involves repeatedly extracting the maximum element from the heap (which is always the root node) and placing it at the end of the array.
        After each extraction, the heap property is restored by performing the sift-down operation on the remaining elements to maintain the heap structure.
        This process continues until all elements have been extracted and placed in their correct positions in the array.

    Sift-Down Operation:
        The siftDown function is responsible for maintaining the heap property during both the heap construction and sorting phases.
        Given a current node index, the siftDown function compares the values of the current node with its children and swaps it with the larger child if necessary.
        This process continues recursively until the current node is greater than or equal to its children, ensuring that the subtree rooted at the current node satisfies the heap property.

    Swapping Elements:
        The swap function is a utility function used to exchange the positions of two elements in the array.

    Time Complexity:
        In every scenario, Heap sort exhibits a complexity of O(n log n) in terms of time, where n represents the number of elements within the input array.
        This complexity arises from the repeated extraction of the maximum element from the heap, which takes O(log n) time. Further, the total number of such extractions scales with the size of the input array.

    Space Complexity:
        The space complexity of heap sort is O(1) since the algorithm operates in place. Meaning, it does not need additional memory proportional to the input size.

Key Points:

    Heap sort is an efficient and stable sorting algorithm with a consistent time complexity of O(n log n).
    Unlike other sorting algorithms like quicksort and mergesort, heap sort is not affected by the input distribution and always performs well.
    However, heap sort has a more significant constant factor compared to quicksort and mergesort, making it less preferred for smaller input sizes.

"""

def heap_sort(array):
    """
    Sorts the given array in ascending order using the heap sort algorithm.

    Args:
        array (list): The input list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    build_max_heap(array)
    # Iterate through the heap from the end to the beginning
    for endIdx in reversed(range(1, len(array))):
        # Swap the root (maximum element) with the last element
        swap(0, endIdx, array)
        # Restore the heap property for the remaining elements
        sift_down(0, endIdx - 1, array)
    return array

def build_max_heap(array):
    """
    Builds a max heap from the given array.

    Args:
        array (list): The input list of integers.
    """
    # Determine the index of the first parent node
    firstParentIdx = (len(array) - 1) // 2
    # Starting from the last parent node, sift down each node to ensure the heap property
    for currentIdx in reversed(range(firstParentIdx + 1)):
        sift_down(currentIdx, len(array) - 1, array)

def sift_down(currentIdx, endIdx, heap):
    """
    Performs the sift-down operation on the heap to maintain the heap property.

    Args:
        currentIdx (int): The index of the current node to sift down.
        endIdx (int): The index of the last element in the heap.
        heap (list): The input list representing the heap.
    """
    # Calculate the index of the first child node
    childOneIdx = currentIdx * 2 + 1
    # Continue sifting down while there is at least one child node
    while childOneIdx <= endIdx:
        # Calculate the index of the second child node (if exists)
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        # Determine the index of the child node to swap with
        idxToSwap = childTwoIdx if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx] else childOneIdx
        # If the value of the node to swap with is greater than the current node, perform the swap
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx, idxToSwap, heap)
            # Update the current index and the index of the first child node
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return

def swap(i, j, array):
    """
    Swaps the elements at the specified indices in the given array.

    Args:
        i (int): The index of the first element to swap.
        j (int): The index of the second element to swap.
        array (list): The input list of integers.
    """
    array[i], array[j] = array[j], array[i]

import unittest

class TestHeapSort(unittest.TestCase):
    """
    Test class for the heap sort algorithm.
    """

    def test_heap_sort(self):
        """
        Test the heap_sort function with a typical input array.
        """
        # Test case with a randomly shuffled array
        self.assertEqual(heap_sort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

    def test_empty_list(self):
        """
        Test the heap_sort function with an empty input array.
        """
        # Test case with an empty input array
        self.assertEqual(heap_sort([]), [])

    def test_sorted_list(self):
        """
        Test the heap_sort function with a sorted input array.
        """
        # Test case with an already sorted input array
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """
        Test the heap_sort function with a reverse-sorted input array.
        """
        # Test case with a reverse-sorted input array
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        """
        Test the heap_sort function with an input array containing duplicate elements.
        """
        # Test case with an input array containing duplicate elements
        self.assertEqual(heap_sort([5, 2, 3, 5, 2, 1]), [1, 2, 2, 3, 5, 5])

if __name__ == "__main__":
    unittest.main()
