class UserTableSingleton:

    """
    User Table with Singleton Pattern

    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance =super(UserTableSingleton, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.users =[]
        self.next_id =1

    def add_user(self, username, fname, lname, gender, age):
        """Add a new user to the table"""
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
            if user['username'] == username:
                return user
        return None
    
    def get_all_users(self):
        """Get all users"""
        return self.users.copy()
    
    def update_user(self, user_id, **kwargs):
        """Update user information"""
        user = self.get_user_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                if key in user and key != 'id':  # Prevent ID modification
                    user[key] = value
            return True
        return False
    
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
    user_table1 = UserTableSingleton()
    
    # Add some users
    user_table1.add_user("jdoe", "John", "Doe", "Male", 30)
    user_table1.add_user("asmith", "Alice", "Smith", "Female", 25)
    
    # Create second instance - it will be the same as the first one
    user_table2 = UserTableSingleton()
    
    # Add another user through the second instance
    user_table2.add_user("bjohnson", "Bob", "Johnson", "Male", 40)
    
    # Verify both instances point to the same data
    print("Users from instance 1:")
    for user in user_table1.get_all_users():
        print(user)
    
    print("\nUsers from instance 2:")
    for user in user_table2.get_all_users():
        print(user)
    
    # Verify singleton behavior
    print(f"\nAre both instances the same? {user_table1 is user_table2}")

"""
Key Features:

    Singleton Implementation:

        The __new__ method ensures only one instance exists

        The _instance class variable holds the single instance

    User Management:

        Stores users with username, first name, last name, gender, and age

        Auto-increments ID for each new user

        Provides CRUD operations (Create, Read, Update, Delete)

    Thread Safety Note:

        This basic implementation isn't thread-safe. For production use with multiple threads, you should add locking mechanisms.

    Usage:

        Any number of UserTableSingleton() calls will return the same instance

        All operations are performed on the same underlying data store
"""