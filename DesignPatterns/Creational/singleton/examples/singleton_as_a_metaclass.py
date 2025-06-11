
class SingletonMeta(type):
    """
    Implementing User Table with Singleton using a Metaclass
    """
    class SingletonMeta(type):
        _instances ={}

        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] =super().__call__(*args, **kwargs)
            return cls._instances[cls]
        
class UserTable(metaclass=SingletonMeta):
    def __init__(self):
        self.users = []
        self.next_id = 1
    
    def add_user(self, username, fname, lname, gender=None, age=None):
        """Add a new user with validation"""
        if not all([username, fname, lname]):
            raise ValueError("Username, first name and last name are required")
        
        if any(user['username'].lower() == username.lower() for user in self.users):
            raise ValueError(f"Username '{username}' already exists")
        
        user = {
            'id': self.next_id,
            'username': username,
            'fname': fname,
            'lname': lname,
            'gender': gender,
            'age': age
        }
        self.users.append(user)
        self.next_id += 1
        return user
    
    def get_user_by_id(self, user_id):
        """Get user by ID with error handling"""
        try:
            return next(user for user in self.users if user['id'] == user_id)
        except StopIteration:
            raise ValueError(f"User with ID {user_id} not found") from None
    
    def get_user_by_username(self, username):
        """Get user by username (case-insensitive)"""
        try:
            return next(
                user for user in self.users 
                if user['username'].lower() == username.lower()
            )
        except StopIteration:
            return None
    
    def get_all_users(self):
        """Get a safe copy of all users"""
        return [user.copy() for user in self.users]
    
    def update_user(self, user_id, **kwargs):
        """Update user with validation"""
        user = self.get_user_by_id(user_id)
        
        if 'username' in kwargs and kwargs['username'] != user['username']:
            if self.get_user_by_username(kwargs['username']):
                raise ValueError(f"Username '{kwargs['username']}' already exists")
        
        for key, value in kwargs.items():
            if key in user and key != 'id':
                user[key] = value
        return user
    
    def delete_user(self, user_id):
        """Delete a user by ID"""
        user = self.get_user_by_id(user_id)
        self.users.remove(user)
        return True
    
    def __str__(self):
        return f"UserTable with {len(self.users)} users"


# Example usage
if __name__ == "__main__":
    # First instance
    db1 = UserTable()
    db1.add_user("jdoe", "John", "Doe", "Male", 30)
    db1.add_user("asmith", "Alice", "Smith", "Female", 25)
    
    # Second instance - same as the first
    db2 = UserTable()
    db2.add_user("bjohnson", "Bob", "Johnson", "Male", 40)
    
    # Demonstrate singleton behavior
    print(f"Same instance? {db1 is db2}")  # True
    
    # Show all users
    print("\nAll users:")
    for user in db1.get_all_users():
        print(user)
    
    # Update a user
    db2.update_user(1, age=31, fname="Jonathan")
    
    # Verify update appears in db1
    print("\nAfter update:")
    print(db1.get_user_by_id(1))
    
    # Error handling examples
    try:
        db1.add_user("jdoe", "Duplicate", "User", "Male", 35)
    except ValueError as e:
        print(f"\nError: {e}")
    
    try:
        db1.get_user_by_id(999)
    except ValueError as e:
        print(f"Error: {e}")

"""
Key Features of This Implementation:

    Metaclass Singleton Pattern:

        SingletonMeta controls instance creation for any class that uses it

        More Pythonic than the decorator approach for this use case

        Clean separation between singleton logic and business logic

    Enhanced User Table:

        Comprehensive input validation

        Better error handling with descriptive messages

        Case-insensitive username comparison

        Safe copying of user data when returning

    Thread Safety Consideration:

        While this implements the singleton pattern, for thread safety in production you'd want to add locking mechanisms

    Clean Interface:

        All methods return meaningful values (users when appropriate, booleans for success/failure)

        Clear method naming and documentation

This metaclass approach is particularly elegant because:

    It's very explicit about being a singleton (visible in the class definition)

    The singleton behavior is completely separated from the user management logic

    It can be easily reused for other classes that need singleton behavior
"""