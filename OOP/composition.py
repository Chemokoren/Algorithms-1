"""
Composition in OOP

Composition in Object-Oriented Programming (OOP) is a design principle where one class
contains an instance of another class as a part of its attributes.
It allows objects to be built using other objects, creating a "has-a" relationship instead
of the "is-a" relationship seen in inheritance.

Key Characteristics of Composition

    Reusability: Promotes code reuse by combining smaller, well-defined classes.
    Decoupling: Provides flexibility by avoiding rigid inheritance hierarchies.
    Encapsulation: Keeps the internal details of composed objects hidden, exposing
    only necessary functionality.

"""
class Address:
    """
    Represents an address with details like street, city, and postal code.
    """
    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"

class Contact:
    """
    Represents a set of contacts.
    """
    def __init__(self, phone,mobile, email):
        self.phone = phone
        self.mobile = mobile
        self.email = email

    def __str__(self):
        return f"{self.phone}, {self.mobile}, {self.email}"


class Employee:
    """
    Represents an employee with a name and address.
    Demonstrates composition by including an Address object.
    """
    def __init__(self, name, address, contacts):
        self.name = name
        self.address = address  # Composition: Employee "has an" Address
        self.contacts = contacts  # Composition: Employee "has an" Contacts

    def __str__(self):
        return f"Employee: {self.name}, Address: {self.address}, Contacts: {self.contacts}"


# Example usage
if __name__ == "__main__":
    # Create an Address object
    emp_address = Address("123 Main St", "Springfield", "98765")

    # Create a Contacts Object
    contact = Contact("254713058775", "0710737392", "testineek@gmail.com")

    # Create an Employee object with the Address object
    employee = Employee("John Doe", emp_address, contact)

    # Display the employee details
    print(employee)  # Output: Employee: John Doe, Address: 123 Main St, Springfield, 98765
    print(employee.contacts.mobile)
