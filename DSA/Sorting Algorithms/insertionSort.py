def insertionsort(A):
    """
    Perform Insertion Sort on a given array.

    Insertion Sort is a comparison-based sorting algorithm that builds the sorted array one element at a time.
    It repeatedly takes the next unsorted element and places it in its correct position
    within the sorted portion.

    Parameters:
    A (list): The list of elements to be sorted. Can include integers, floats, or any comparable elements.

    Time Complexity:
        - Best case: O(n) when the input array is already sorted.
        - Worst case: O(n^2) when the input array is sorted in reverse order.

    Space Complexity:
        - O(1) as it sorts in place.

    Example:
        Original Array: [84, 21, 96, 15, 47]
        Sorted Array: [15, 21, 47, 84, 96]
    """
    # Iterate through the array starting from the second element
    for i in range(1, len(A)):
        # Store the current element to be positioned
        value = A[i]
        # Initialize the position to the current index
        position = i

        # Shift elements of the sorted portion (to the left of `i`) to the right
        # if they are greater than the current element
        while position > 0 and A[position - 1] > value:
            # Move the larger element one position to the right
            A[position] = A[position - 1]
            # Move the position pointer one step back
            position = position - 1

        # Place the current element in its correct position
        A[position] = value


# Example usage:
A = [84, 21, 96, 15, 47]
print('Original Array: ', A)
# Call the insertion sort function to sort the array
insertionsort(A)
print('Sorted Array: ', A)

"""
Explanation of the Code

    Outer Loop:
        Starts from the second element (index 1) since a single-element subarray (index 0) is already 
        sorted by definition.
        Each iteration considers one more element from the unsorted portion and incorporates it into the
        sorted portion.

    Value and Position Initialization:
        value: The element currently being positioned in the sorted portion.        
        # Place the current element in its correct position
        A[position] = value
        position: Tracks where value should be placed in the sorted portion.

    Inner While Loop:
        Compares the current element (value) with the elements in the sorted portion (to its left).
        Moves larger elements one position to the right to make space for value.

    Placement:
        Once the correct position for value is found, it is inserted into the sorted portion.

Example Walkthrough
Input: [84, 21, 96, 15, 47]

    Iteration 1 (i = 1):
        value = 21, position = 1.
        Compare 21 < 84. Shift 84 right.
        Place 21 at index 0. Result: [21, 84, 96, 15, 47].
    Iteration 2 (i = 2):
        value = 96, position = 2.
        No shifts needed. Result: [21, 84, 96, 15, 47].
    Iteration 3 (i = 3):
        value = 15, position = 3.
        Compare 15 < 96, 15 < 84, 15 < 21. Shift all three right.
        Place 15 at index 0. Result: [15, 21, 84, 96, 47].
    Iteration 4 (i = 4):
        value = 47, position = 4.
        Compare 47 < 96, 47 < 84. Shift both right.
        Place 47 at index 2. Result: [15, 21, 47, 84, 96].

Output: [15, 21, 47, 84, 96]

"""