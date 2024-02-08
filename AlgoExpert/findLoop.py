"""
Solution Approach
    The find_loop function takes the head node of a linked list as input and returns the starting 
    node of a loop in the linked list, if it exists.
    It uses Floyd's Tortoise and Hare algorithm to detect the loop in the linked list. Two pointers, 
    first and second, are initialized to traverse the linked list at different speeds until they meet 
    at a common node within the loop.
    After detecting the loop, one pointer (first) is reset to the head of the linked list, and both 
    pointers are moved one step at a time until they meet again at the starting node of the loop.
    The function returns the starting node of the loop or None if no loop is found.
    The TestFindLoop class contains unit tests to verify the correctness of the findLoop function for 
    various scenarios, including cases with no loop, loops starting from different nodes in the linked 
    list, and loops starting from the first node.

"""
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# O(n) time | O(1) space
def find_loop(head):
    """
    Find the starting node of a loop in a linked list, if it exists.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        ListNode: The starting node of the loop. Returns None if no loop is found.
    """
    # Initialize two pointers: first and second
    first = head.next
    second = head.next.next
    
    # Move first and second pointers until they meet at a common node within the loop
    while first != second:
        if not second or not second.next:
            return None  # No loop found
        first = first.next
        second = second.next.next
    
    # Reset first pointer to the head and move both pointers one step at a time until they meet
    first = head
    while first != second:
        first = first.next
        second = second.next
    
    # Return the node where the pointers meet, which is the starting node of the loop
    return first

import unittest
class TestFindLoop(unittest.TestCase):
    def test_no_loop(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        self.assertIsNone(find_loop(head))

    def test_loop_starting_from_second_node(self):
        head = ListNode(1)
        node2 = ListNode(2)
        head.next = node2
        node3 = ListNode(3)
        node2.next = node3
        node4 = ListNode(4)
        node3.next = node4
        node5 = ListNode(5)
        node4.next = node5
        node6 = ListNode(6)
        node5.next = node6
        node6.next = node2  # Create a loop
        self.assertEqual(find_loop(head), node2)

    def test_loop_starting_from_last_node(self):
        head = ListNode(1)
        node2 = ListNode(2)
        head.next = node2
        node3 = ListNode(3)
        node2.next = node3
        node4 = ListNode(4)
        node3.next = node4
        node5 = ListNode(5)
        node4.next = node5
        node6 = ListNode(6)
        node5.next = node6
        node6.next = node5  # Create a loop
        self.assertEqual(find_loop(head), node5)

    def test_loop_starting_from_first_node(self):
        head = ListNode(1)
        node2 = ListNode(2)
        head.next = node2
        node3 = ListNode(3)
        node2.next = node3
        node4 = ListNode(4)
        node3.next = node4
        node5 = ListNode(5)
        node4.next = node5
        node6 = ListNode(6)
        node5.next = node6
        node6.next = head  # Create a loop
        self.assertEqual(find_loop(head), head)

if __name__ == "__main__":
    unittest.main()