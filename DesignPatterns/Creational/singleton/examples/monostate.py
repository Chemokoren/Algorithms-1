class UserTableMonostate:
    __shared_state = {
        'users': [],
        'next_id': 1
    }
    
    def __init__(self):
        self.__dict__ = self.__shared_state
    
    def add_user(self, username, fname, lname, gender=None, age=None):
        """Add a new user with validation"""
        if not all([username, fname, lname]):
            raise ValueError("Username, first name and last name are required")
        
        if any(user['username'].lower() == username.lower() 
               for user in self.users):
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
        return f"UserTableMonostate with {len(self.users)} users"


# Example usage
if __name__ == "__main__":
    # First instance
    db1 = UserTableMonostate()
    db1.add_user("jdoe", "John", "Doe", "Male", 30)
    db1.add_user("asmith", "Alice", "Smith", "Female", 25)
    
    # Second instance - different object but same state
    db2 = UserTableMonostate()
    print(f"Same instance? {db1 is db2}")  # False
    print(f"Same state? {db1.users is db2.users}")  # True
    
    # Add user through second instance
    db2.add_user("bjohnson", "Bob", "Johnson", "Male", 40)
    
    # Show all users from first instance
    print("\nAll users from db1:")
    for user in db1.get_all_users():
        print(user)
    
    # Update through second instance
    db2.update_user(1, age=31, fname="Jonathan")
    
    # Verify update appears in db1
    print("\nAfter update through db2:")
    print(db1.get_user_by_id(1))
    
    # Demonstrate independent instances with shared state
    db3 = UserTableMonostate()
    print(f"\nNew instance user count: {len(db3.users)}")
    
    # Reset demonstration (affects all instances)
    db1.users.clear()
    db1.next_id = 1
    print(f"\nAfter reset through db1, db2 count: {len(db2.users)}")

"""
Notes
-----

Implementing User Table with Monostate Pattern in Python

The Monostate pattern (also known as the Borg pattern) is an alternative to Singleton that allows multiple instances but shares the same state. 

Key Differences from Singleton:

    Multiple Instances, Shared State:

        Each UserTableMonostate() call creates a new instance

        All instances share the same __shared_state dictionary

        __dict__ assignment makes instance attributes point to the shared state

    Behavioral Differences:

        is comparison returns False (different objects)

        == comparison would need to be implemented separately

        All instances automatically reflect state changes from any instance

    Advantages:

        More flexible than Singleton (can create multiple instances)

        Still maintains single shared state

        Can be subclassed more naturally than Singleton

    Disadvantages:

        Slightly more memory usage (multiple instance objects)

        Less explicit than Singleton pattern

        Shared state is less obvious to users of the class

This pattern is particularly useful when:

    You want the benefits of shared state but need multiple instances

    You need to subclass the shared-state class

    You want to maintain instance identity while sharing data

"""