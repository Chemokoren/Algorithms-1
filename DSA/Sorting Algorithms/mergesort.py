def mergesort(A):
    """
    Perform a merge sort on the given list.

    Merge sort is a divide-and-conquer algorithm that recursively divides 
    the input list into smaller sub-lists, sorts them, and then merges
    them to produce a sorted list.

    Parameters:
    A (list): The list of elements to be sorted.

    Returns:
    None: The input list A is sorted in place.

    Example:
    >>> A = [84, 21, 96, 15, 47]
    >>> mergesort(A)
    >>> print(A)
    [15, 21, 47, 84, 96]

    Time Complexity:
    - Best, Average, and Worst Case: O(n log n), where n is the length of the list.

    Space Complexity:
    - O(n) due to auxiliary space used during the merge process.
    """
    # Base case: A list with 0 or 1 element is already sorted.
    if len(A) > 1:
        # Find the midpoint to divide the list into two halves.
        mid = len(A) // 2
        left = A[:mid]   # Left sublist
        right = A[mid:]  # Right sublist

        # Recursively sort the left and right sub-lists.
        mergesort(left)
        mergesort(right)

        # Initialize pointers for merging: i (left), j (right), k (main list).
        i = 0  # Pointer for the left sublist
        j = 0  # Pointer for the right sublist
        k = 0  # Pointer for the main list

        # Merge the two sorted sublists back into the main list.
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]  # Add the smaller element from the left sublist
                i += 1
            else:
                A[k] = right[j]  # Add the smaller element from the right sublist
                j += 1
            k += 1  # Move to the next position in the main list

        # Add any remaining elements from the left sublist.
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        # Add any remaining elements from the right sublist.
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


# Example usage
A = [84, 21, 96, 15, 47]
print('Original Array: ', A)
mergesort(A)
print('Sorted Array :', A)


"""
Explanation of the Code

    Base Case:
        If the length of the list is 1 or less, it is already sorted, and the function returns without
        further action.

    Divide:
        The list is split into two halves (left and right) using slicing.

    Conquer:
        mergesort is called recursively on the left and right halves to sort them.

    Combine:
        Two sorted halves are merged back into the original list:
            - The smallest element between the current pointers of the two halves is added to the main list.
            - Remaining elements from either half are added after one half is exhausted.

    Pointers:
        i, j, and k keep track of the current positions in the left sublist, right sublist, and main list respectively.

    In-Place Sorting:
        The input list is modified directly, so no additional list is returned.
"""
