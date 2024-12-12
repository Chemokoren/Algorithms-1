"""
Dependency Injection

Dependency Injection (DI) is a design pattern where an object receives its dependencies
from an external source, rather than creating them itself.
It promotes loose coupling by separating the creation of dependencies from their usage,
allowing greater flexibility and easier testing.

Dependency Injection in OOP

Dependency Injection (DI) is a design pattern where an object receives its dependencies from an external source, rather than creating them itself. It promotes loose coupling by separating the creation of dependencies from their usage, allowing greater flexibility and easier testing.
Key Concepts of Dependency Injection

    Dependency: A class or object required by another class to function (e.g., a database, service, or helper object).
    Injection: Supplying the dependency from the outside, rather than creating it inside the dependent class.
    Types of Dependency Injection:
        Constructor Injection: Dependencies are provided via the constructor.
        Setter Injection: Dependencies are set via public methods.
        Interface Injection: The dependency is injected through an interface the dependent class implements.

"""
class TaxCalculator:
    """
    A dependency class that calculates tax on a salary.
    """
    def calculate_tax(self, gross_salary):
        # A simple tax calculation (e.g., 20% of gross salary)
        return gross_salary * 0.2


class Employee:
    """
    Employee class depends on a TaxCalculator to compute net salary.
    Demonstrates dependency injection.
    """
    def __init__(self, name, gross_salary, tax_calculator):
        self.name = name
        self.gross_salary = gross_salary
        self.tax_calculator = tax_calculator  # Dependency injected via constructor

    def calculate_net_salary(self):
        # Use the injected TaxCalculator to compute the tax
        tax = self.tax_calculator.calculate_tax(self.gross_salary)
        return self.gross_salary - tax

    def __str__(self):
        return (
            f"Employee: {self.name}, "
            f"Gross Salary: ${self.gross_salary:.2f}, "
            f"Net Salary: ${self.calculate_net_salary():.2f}"
        )


# Example usage
if __name__ == "__main__":
    # Create a TaxCalculator instance (the dependency)
    tax_calculator = TaxCalculator()

    # Inject the dependency into the Employee class
    employee = Employee("John Doe", 5000, tax_calculator)

    # Display the employee's details
    print(employee)

