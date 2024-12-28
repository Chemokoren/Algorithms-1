def quicksort_recursive(A):
    """
    Sorts a list using the recursive implementation of the QuickSort algorithm.

    Parameters:
    A (list): The list of elements to be sorted.

    Returns:
    list: A new sorted list in ascending order.

    Example:
    >>> A = [84, 21, 96, 15, 47]
    >>> quicksort_recursive(A)
    [15, 21, 47, 84, 96]
    """
    # Initialize the range for the entire list
    low, high = 0, len(A) - 1

    def rec_quick_sort(A, low, high):
        """
        Recursively applies QuickSort to partitions of the list.

        Parameters:
        A (list): The list to be sorted.
        low (int): The starting index of the partition.
        high (int): The ending index of the partition.

        Returns:
        list: The sorted list (in-place).
        """
        if low < high:
            # Partition the list and get the pivot index
            p = partition(A, low, high)
            # Recursively sort the left and right partitions
            rec_quick_sort(A, low, p - 1)
            rec_quick_sort(A, p + 1, high)
        return A

    # Start the recursive QuickSort
    return rec_quick_sort(A, low, high)


def quicksort(A, low, high):
    """
    Sorts a list using an in-place implementation of the QuickSort algorithm.

    Parameters:
    A (list): The list of elements to be sorted.
    low (int): The starting index of the list.
    high (int): The ending index of the list.

    Example:
    >>> A = [84, 21, 96, 15, 47]
    >>> quicksort(A, 0, len(A) - 1)
    >>> A
    [15, 21, 47, 84, 96]
    """
    if low < high:
        # Partition the list and get the pivot index
        p = partition(A, low, high)
        # Recursively sort the left and right partitions
        quicksort(A, low, p - 1)
        quicksort(A, p + 1, high)


def partition(A, low, high):
    """
    Partitions a list around a pivot element, placing all elements less than
    or equal to the pivot to its left and all greater elements to its right.

    Parameters:
    A (list): The list to be partitioned.
    low (int): The starting index of the partition.
    high (int): The ending index of the partition, where the pivot resides.

    Returns:
    int: The final index of the pivot element after partitioning.

    Example:
    >>> A = [84, 21, 96, 15, 47]
    >>> pivot_index = partition(A, 0, len(A) - 1)
    >>> A
    [15, 21, 47, 84, 96]  # Pivot element is at the correct position.
    """
    # Initialize the pointer for elements smaller than the pivot
    i = low - 1
    # Select the pivot as the last element in the partition
    pivot = A[high]

    # Iterate through the partition
    for j in range(low, high):
        if A[j] <= pivot:
            # Increment the pointer and swap elements
            i += 1
            A[i], A[j] = A[j], A[i]

    # Place the pivot element in its correct position - when j reaches the pivot
    # the new i A[i] = A[i + 1]
    A[i + 1], A[high] = A[high], A[i + 1]

    # Return the index of the pivot
    return i + 1


# Example usage and testing
A = [84, 21, 96, 15, 47]
print('Expected: [15, 21, 47, 84, 96], Actual:', quicksort_recursive(A))
print(f'Original: {A}')  # `quicksort_recursive` sorts the list in place.
quicksort(A, 0, len(A) - 1)
print(f'After Sorting: {A}')
