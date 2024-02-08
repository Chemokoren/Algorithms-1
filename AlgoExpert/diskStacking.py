"""
The time and space complexity of the diskStacking function is as follows:

Time Complexity:

    The function consists of two nested loops: one iterating over the disks and another iterating over the range of disks.
    Inside the nested loops, there are constant-time operations for comparisons and updates.
    Therefore, the overall time complexity is O(n^2), where n is the number of disks.

Space Complexity:

    The function uses additional space to store the heights and sequences lists, both of which have a 
    length equal to the number of disks.
    Therefore, the space complexity is O(n), where n is the number of disks.

Overall, the function has a quadratic time complexity and linear space complexity with respect to the number of disks.


"""
# O(n ^ 2) time | O(n) space
def diskStacking(disks):
    """
    Given a list of disks represented as [width, depth, height], returns the maximum height
    achievable by stacking the disks while adhering to the constraints that a disk can only
    be stacked on top of a larger disk.

    Args:
        disks (List[List[int]]): List of disks, where each disk is represented by its dimensions [width, depth, height].

    Returns:
        List[List[int]]: A list of disks representing the maximum height achievable by stacking the disks.

    Time Complexity: O(n^2) where n is the number of disks.
    Space Complexity: O(n) for the heights and sequences lists.
    """
    # Sort the disks by height in ascending order
    disks.sort(key=lambda disk: disk[2])
    
    # Initialize arrays to store the heights and sequences
    heights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]
    
    # Index of the maximum height achieved
    maxHeightIdx = 0
    
    # Loop through each disk
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        # Compare the current disk with each other disk
        for j in range(0, i):
            otherDisk = disks[j]
            # Check if the dimensions of the current disk are valid for stacking on top of the other disk
            if areValidDimensions(otherDisk, currentDisk):
                # Update the height if stacking the current disk on top of the other disk results in a higher stack
                if heights[i] <= currentDisk[2] + heights[j]:
                    heights[i] = currentDisk[2] + heights[j]
                    sequences[i] = j
            # Update the index of the maximum height achieved
            if heights[i] >= heights[maxHeightIdx]:
                maxHeightIdx = i
    # Build and return the sequence of disks that achieves the maximum height
    return buildSequence(disks, sequences, maxHeightIdx)

def areValidDimensions(o, c):
    """
    Checks if the dimensions of the other disk (o) are smaller than the current disk (c).

    Args:
        o (List[int]): Dimensions of the other disk [width, depth, height].
        c (List[int]): Dimensions of the current disk [width, depth, height].

    Returns:
        bool: True if the dimensions are valid, False otherwise.
    """
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

"""
Overall, these two lines of code iteratively traverse through the sequence of disks, starting from
the last disk and moving backward. For each disk, it appends it to the sequence list and updates the 
currentIdx to the index of the previous disk in the sequence, as determined by the sequences list. 
This process continues until it reaches a disk with no previous disk (i.e., currentIdx becomes None),
indicating the end of the sequence.
"""
def buildSequence(array, sequences, currentIdx):
    """
    Builds the sequence of disks that achieves the maximum height.

    Args:
        array (List[List[int]]): List of disks.
        sequences (List[int]): List of sequence indices.
        currentIdx (int): Index of the current disk in the sequence.

    Returns:
        List[List[int]]: A list of disks representing the sequence.
    """
    # The sequences list maintains the indices of the disks forming the sequence. 
    # Each element in the sequences list represents the index of the previous disk in the sequence.
    sequence = []
    # Check if the currentIdx is within the valid range
    while currentIdx is not None and currentIdx < len(array):
        # array[currentIdx]- The element represents a disk, which is a list of 
        # integers [width, depth, height].
        sequence.append(array[currentIdx])
        # This updates the currentIdx variable to the value stored in the sequences list at the 
        # index currentIdx.
        currentIdx = sequences[currentIdx]
    # If the currentIdx is out of range, return an empty sequence
    if currentIdx is None:
        return list(reversed(sequence))
    else:
        # Handle the case where currentIdx is out of range
        return []



import unittest

class TestDiskStacking(unittest.TestCase):

    def test_given_disks(self):
        my_disks =[[2,2,1],[2,1,2],[3,2,3],[2,3,4],[4,4,5],[2,2,8]]
        self.assertEqual(diskStacking(my_disks), [[2, 1, 2], [3, 2, 3], [4, 4, 5]])

    def test_disk_stacking(self):
        """
        Test case to check the correctness of the disk stacking algorithm.
        """
        # Test case with a simple set of disks
        disks1 = [[2, 2, 1], [2, 3, 2], [3, 4, 3]]
        expected_result1 = [[2, 3, 2], [3, 4, 3]]
        self.assertEqual(diskStacking(disks1), expected_result1)

        # Test case with another set of disks
        disks2 = [[3, 3, 2], [2, 2, 1], [1, 1, 1]]
        expected_result2 = [[1, 1, 1], [3, 3, 2]]
        self.assertEqual(diskStacking(disks2), expected_result2)

        # # Test case with duplicate disks
        disks3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected_result3 = [[1, 1, 1]]
        self.assertEqual(diskStacking(disks3), expected_result3)

        # Test case with empty list of disks
        disks4 = []
        expected_result4 = []
        self.assertEqual(diskStacking(disks4), expected_result4)

    def test_are_valid_dimensions(self):
        """
        Test case to check the validity of the areValidDimensions function.
        """
        # Test case with valid dimensions
        other_disk1 = [2, 2, 2]
        current_disk1 = [3, 3, 3]
        self.assertTrue(areValidDimensions(other_disk1, current_disk1))

        # Test case with invalid dimensions
        other_disk2 = [3, 3, 3]
        current_disk2 = [2, 2, 2]
        self.assertFalse(areValidDimensions(other_disk2, current_disk2))

        # Test case with equal dimensions
        other_disk3 = [3, 3, 3]
        current_disk3 = [3, 3, 3]
        self.assertFalse(areValidDimensions(other_disk3, current_disk3))

    def test_build_sequence(self):
        """
        Test case to check the correctness of the buildSequence function.
        """
        # Test case with a sequence of disks
        array = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        sequences = [None, 0, 1]
        current_idx = 2
        expected_result = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        self.assertEqual(buildSequence(array, sequences, current_idx), expected_result)

if __name__ == '__main__':
    unittest.main()
