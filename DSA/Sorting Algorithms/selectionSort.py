def selectionsort(A):
    """
    Sorts a list in-place using the selection sort algorithm.

    The function repeatedly selects the largest element from the unsorted portion of the list 
    and swaps it with the last element of that unsorted portion, effectively growing the 
    sorted portion of the list from the end.

    Args:
        A (list): The list of elements to be sorted. Assumes all elements are comparable.

    Example:
        >>> A = [84, 21, 96, 15, 47]
        >>> selectionsort(A)
        >>> print(A)
        [15, 21, 47, 84, 96]
    """
    # Iterate from the last element down to the second element.
    for i in range(len(A) - 1, 0, -1):
        # Initialize max_position to the first element in the unsorted portion.
        max_position = 0
        # Iterate through the unsorted portion to find the largest element.
        for j in range(1, i + 1):
            # Update max_position if a larger element is found.
            if A[j] > A[max_position]:
                max_position = j
        # Swap the largest element found with the last element of the unsorted portion.
        A[i], A[max_position] = A[max_position], A[i]

# Initialize an unsorted array.
A = [84, 21, 96, 15, 47]

# Print the original array.
print("Original Array: ", A)

# Call the selectionsort function to sort the array.
selectionsort(A)

# Print the sorted array.
print('Sorted Array: ', A)
