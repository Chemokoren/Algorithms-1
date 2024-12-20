# test_exceptions.py

import unittest
from exceptions import Empty

class TestExceptions(unittest.TestCase):

    def test_empty_exception_inheritance(self):
        """Test if Empty exception is a subclass of Exception."""
        assert issubclass(Empty, Exception)


    def test_empty_exception_instance(self):
        """Test instantiating Empty exception."""
        exception_instance = Empty("Queue is empty")
        assert isinstance(exception_instance, Empty)
        assert str(exception_instance) == "Queue is empty"


    def test_empty_exception_raises(self):
        """Test if Empty exception can be raised and caught correctly."""
        with self.assertRaisesRegex(Empty, "Queue is empty"):
            raise Empty("Queue is empty")

if __name__ == "__main__":
    unittest.main()