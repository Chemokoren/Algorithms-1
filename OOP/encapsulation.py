"""
Encapsulation is the bundling of data (attributes) and methods (functions) that operate on
the data into a single unit (class).
It also involves restricting direct access to some attributes and methods to ensure
better control and prevent accidental modification.
This is typically achieved using access modifiers:

Public Attributes: Accessible from anywhere.
Protected Attributes (_attribute): Indicated by a single underscore;
        meant to be accessed only within the class or its subclasses.
Private Attributes (__attribute): Indicated by double underscores;
        not directly accessible outside the class.

Benefits of Encapsulation

    Data Hiding: Prevents direct access to sensitive or implementation-specific data.
    Control: Enables validation and error checking before changing the state of an object.
    Modularity: Encapsulated components are easier to maintain and debug.
    Flexibility: Internal implementation can change without affecting external code.

"""
from abc import ABC, abstractmethod

class Employee(ABC):
    """
    Abstract base class for employees with encapsulated attributes.
    """

    def __init__(self, name, base_salary):
        self.__name = name           # Private attribute
        self._base_salary = base_salary  # Protected attribute

    @abstractmethod
    def calculate_salary(self):
        """
        Abstract method to calculate salary.
        Must be implemented by subclasses.
        """
        pass

    # Public getter for the name
    def get_name(self):
        return self.__name

    # Public setter for the name
    def set_name(self, name):
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            raise ValueError("Invalid name")

    # Protected method for internal use
    def _get_base_salary(self):
        return self._base_salary

class FullTimeEmployee(Employee):
    """
    Full-time employee with a fixed monthly salary.
    """

    def calculate_salary(self):
        return self._get_base_salary()

class PartTimeEmployee(Employee):
    """
    Part-time employee with hourly wages.
    """

    def __init__(self, name, base_salary, hours_worked, hourly_rate):
        super().__init__(name, base_salary)
        self.__hours_worked = hours_worked  # Private attribute
        self.__hourly_rate = hourly_rate    # Private attribute

    def calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate

    # Public getter for hours worked
    def get_hours_worked(self):
        return self.__hours_worked

    # Public setter for hours worked
    def set_hours_worked(self, hours):
        if hours >= 0:
            self.__hours_worked = hours
        else:
            raise ValueError("Hours worked cannot be negative")

    # Public getter for hourly rate
    def get_hourly_rate(self):
        return self.__hourly_rate

    # Public setter for hourly rate
    def set_hourly_rate(self, rate):
        if rate > 0:
            self.__hourly_rate = rate
        else:
            raise ValueError("Hourly rate must be positive")

# Example usage
if __name__ == "__main__":
    emp1 = FullTimeEmployee("Alice", 5000)
    emp2 = PartTimeEmployee("Bob", 0, 100, 20)

    # Accessing public methods
    print(emp1.get_name())  # Output: Alice
    emp1.set_name("Alice Smith")
    print(emp1.get_name())  # Output: Alice Smith

    print(f"{emp2.get_name()} Salary: ${emp2.calculate_salary():.2f}")

    # Encapsulation in action
    emp2.set_hours_worked(120)
    emp2.set_hourly_rate(25)
    print(f"{emp2.get_name()} Updated Salary: ${emp2.calculate_salary():.2f}")
