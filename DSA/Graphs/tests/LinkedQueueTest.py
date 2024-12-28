import unittest
from LinkedQueue import LinkedQueue
from exceptions import Empty  # Assuming your `Empty` exception is in a module named `exceptions`

class TestLinkedQueue(unittest.TestCase):
    def setUp(self):
        """Set up a new LinkedQueue instance before each test."""
        self.queue = LinkedQueue()

    def test_enqueue_single_element(self):
        """Test enqueueing a single element."""
        self.queue.enqueue(10)
        self.assertEqual(len(self.queue), 1, "Queue size should be 1 after enqueueing one element.")
        self.assertEqual(self.queue.first(), 10, "First element should be the one just enqueued.")

    def test_enqueue_multiple_elements(self):
        """Test enqueueing multiple elements."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(len(self.queue), 3, "Queue size should reflect the number of enqueued elements.")
        self.assertEqual(self.queue.first(), 10, "First element should be the first one enqueued.")

    def test_dequeue_single_element(self):
        """Test dequeueing a single element."""
        self.queue.enqueue(10)
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, 10, "Dequeued element should match the first enqueued element.")
        self.assertTrue(self.queue.is_empty(), "Queue should be empty after dequeueing the only element.")

    def test_dequeue_multiple_elements(self):
        """Test dequeueing multiple elements."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.dequeue(), 10, "First dequeued element should be the first enqueued.")
        self.assertEqual(self.queue.dequeue(), 20, "Second dequeued element should match the second enqueued.")
        self.assertEqual(self.queue.dequeue(), 30, "Last dequeued element should match the last enqueued.")
        self.assertTrue(self.queue.is_empty(), "Queue should be empty after all elements are dequeued.")

    def test_dequeue_empty_queue(self):
        """Test dequeueing from an empty queue raises an exception."""
        with self.assertRaises(Empty, msg="Dequeueing an empty queue should raise an exception."):
            self.queue.dequeue()

    def test_first_empty_queue(self):
        """Test accessing the first element of an empty queue raises an exception."""
        with self.assertRaises(Empty, msg="Accessing first on an empty queue should raise an exception."):
            self.queue.first()

    def test_is_empty(self):
        """Test the is_empty method."""
        self.assertTrue(self.queue.is_empty(), "Newly created queue should be empty.")
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty(), "Queue should not be empty after enqueueing an element.")
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty(), "Queue should be empty after dequeueing all elements.")

    def test_size(self):
        """Test the size of the queue."""
        self.assertEqual(len(self.queue), 0, "Size of a newly created queue should be 0.")
        self.queue.enqueue(10)
        self.assertEqual(len(self.queue), 1, "Queue size should increase by 1 after each enqueue.")
        self.queue.enqueue(20)
        self.assertEqual(len(self.queue), 2, "Queue size should increase correctly with multiple enqueues.")
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 1, "Queue size should decrease by 1 after a dequeue.")
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 0, "Queue size should return to 0 after all elements are dequeued.")

    def test_order_is_maintained(self):
        """Test that the queue maintains the correct order (FIFO)."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.dequeue(), 10, "Order should be maintained: FIFO (First In, First Out).")
        self.assertEqual(self.queue.first(), 20, "The next element should be updated correctly.")
        self.assertEqual(self.queue.dequeue(), 20, "Second element should be dequeued correctly.")
        self.assertEqual(self.queue.first(), 30, "The next element should be updated after dequeue.")

    def test_display(self):
        """Test the display method output."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        # Capture console output for testing display
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.queue.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "10-->20-->30-->")

if __name__ == '__main__':
    unittest.main()