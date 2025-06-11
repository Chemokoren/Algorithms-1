def singleton(cls):

    instances ={}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] =cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class UserTable:

    def __init__(self):
        self.users =[]
        self.next_id =1

    def add_user(self, username, fname, lname, gender, age):
        """Add a new user to the table"""
        if not username or not fname or not lname:
            raise ValueError("Username, first name, and last name are required")
        
        if self.get_user_by_username(username):
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
        """Get user by ID"""
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None
    
    def get_user_by_username(self, username):
        """Get user by username"""
        for user in self.users:
            if user['username'].lower() == username.lower():
                return user
        return None
    
    def get_all_users(self):
        """Get all users"""
        return self.users.copy()
    
    def update_user(self, user_id, **kwargs):
        """Update user information"""
        user = self.get_user_by_id(user_id)
        if not user:
            return False
            
        if 'username' in kwargs and kwargs['username'] != user['username']:
            if self.get_user_by_username(kwargs['username']):
                raise ValueError(f"Username '{kwargs['username']}' already exists")
        
        for key, value in kwargs.items():
            if key in user and key != 'id':  # Prevent ID modification
                user[key] = value
        return True
    
    def delete_user(self, user_id):
        """Delete a user"""
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False


# Example usage
if __name__ == "__main__":
    # Create first instance
    user_table1 = UserTable()
    
    # Add some users
    user_table1.add_user("jdoe", "John", "Doe", "Male", 30)
    user_table1.add_user("asmith", "Alice", "Smith", "Female", 25)
    
    # Create second instance - it will be the same as the first one
    user_table2 = UserTable()
    
    # Add another user through the second instance
    user_table2.add_user("bjohnson", "Bob", "Johnson", "Male", 40)
    
    # Update a user
    user_table1.update_user(1, age=31, fname="Jonathan")
    
    # Verify both instances point to the same data
    print("Users from instance 1:")
    for user in user_table1.get_all_users():
        print(user)
    
    print("\nUsers from instance 2:")
    for user in user_table2.get_all_users():
        print(user)
    
    # Verify singleton behavior
    print(f"\nAre both instances the same? {user_table1 is user_table2}")
    
    # Try to add duplicate username (should raise error)
    try:
        user_table1.add_user("jdoe", "Another", "Doe", "Male", 35)
    except ValueError as e:
        print(f"\nError caught: {e}")

"""

Key Differences from the Previous Implementation:

    Singleton as Decorator:

        The @singleton decorator handles the singleton logic separately from the class

        The decorator maintains a dictionary of instances (one per decorated class)

    Improved Validation:

        Added checks for required fields

        Added duplicate username prevention

        Case-insensitive username comparison

    Cleaner Class Implementation:

        The UserTable class focuses solely on user management

        Singleton behavior is added through decoration

    Same Singleton Guarantee:

        Any call to UserTable() returns the same instance

        All operations affect the same underlying data store

This approach provides better separation of concerns - the singleton functionality is completely decoupled from the user table functionality,
making the code more modular and easier to maintain.

"""