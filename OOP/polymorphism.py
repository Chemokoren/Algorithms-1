"""
Polymorphism

Polymorphism in OOP allows objects of different classes to be treated as objects of a
common superclass.

It enables a single interface to represent different underlying data types.

Polymorphism can be achieved through:
    Method Overriding: Subclasses provide specific implementations of methods defined in
    the parent class.
    Method Overloading (not natively supported in Python, but can be simulated using
    default or variable arguments).
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    """
    Abstract base class for employees.
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        """
        Abstract method to calculate salary.
        Must be implemented by subclasses.
        """
        pass

    def __str__(self):
        return f"Employee: {self.name}"

class FullTimeEmployee(Employee):
    """
    Full-time employee with a fixed monthly salary.
    """

    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    """
    Part-time employee with hourly wages.
    """

    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

class Contractor(Employee):
    """
    Contractor with a fixed rate per project.
    """

    def __init__(self, name, project_fee):
        super().__init__(name)
        self.project_fee = project_fee

    def calculate_salary(self):
        return self.project_fee

# Polymorphism in action
def print_salary(employee):
    """
    Demonstrates polymorphism by calling calculate_salary on different employee types.
    """
    print(f"{employee}: Salary: ${employee.calculate_salary():.2f}")

if __name__ == "__main__":
    # Creating instances of various employee types
    emp1 = FullTimeEmployee("Alice", 5000)
    emp2 = PartTimeEmployee("Bob", 100, 20)
    emp3 = Contractor("Charlie", 3000)

    # Using polymorphism
    employees = [emp1, emp2, emp3]

    for emp in employees:
        print_salary(emp)
