class Empty(Exception):
    """
    Custom exception intended to represent an empty state.

    This exception can be used in contexts where an operation is attempted
    on an empty collection, buffer, or similar structure. It serves as a way
    to indicate and handle such scenarios programmatically.
    """
    pass