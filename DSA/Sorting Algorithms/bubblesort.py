def bubblesort(A):
    """
    Perform Bubble Sort on a given list.

    Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order. The
    process is repeated for each element until the list is sorted.

    Parameters:
    A (list): The list of elements to be sorted. Assumes all elements are comparable.

    Returns:
    None: The input list is sorted in place.

    Time Complexity:
    - Best Case: O(n) when the list is already sorted.
    - Worst Case: O(n^2) for a list sorted in reverse order.

    Example:
    --------
    Input: [84, 21, 96, 15, 47]
    Output: [15, 21, 47, 84, 96]
    """
    # Outer loop: Starts from the last element, decreasing to the second element.
    # This ensures the largest unsorted element "bubbles up" to its correct position.
    for i in range(len(A) - 1, 0, -1):
        # Inner loop: Compare and swap adjacent elements.
        for j in range(i):
            # If the current element is greater than the next, swap them.
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

# Example usage of the bubble sort function.
A = [84, 21, 96, 15, 47]
print("Original Array: ", A)  # Print the original unsorted array.
bubblesort(A)  # Call the bubble sort function to sort the array.
print("Sorted Array: ", A)  # Print the sorted array.

"""
Explanation of the Code:

    Outer Loop:
        Starts from the last index and moves backward.
        Ensures that after each pass, the largest unsorted element is moved to its correct position.

    Inner Loop:
        Compares adjacent elements and swaps them if they are out of order.

    Swap:
        The swapping mechanism (A[j], A[j+1] = A[j+1], A[j]) exchanges elements in Pythonic syntax, ensuring no temporary variable is needed.

    In-Place Sorting:
        The list A is sorted directly without creating a new list, optimizing memory usage.

    Example Input and Output:
        The array [84, 21, 96, 15, 47] is sorted into [15, 21, 47, 84, 96].

This implementation provides an intuitive and straightforward demonstration of the Bubble Sort algorithm.
"""
