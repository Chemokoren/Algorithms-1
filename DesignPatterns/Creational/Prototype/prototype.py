"""
Prototype -A partially or fully initialized object that you copy(clone) and make use of.

How do you copy an object so that it does not refer to the original object?
"""
import copy

class Address:
    
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country
        
    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'
    
class Person:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def __str__(self) -> str:
        return f'{self.name} lives at {self.address}'
    
address = Address('123 London Road', 'London','UK')
john = Person('John',address)
print(john)
# jane = Person('Jane', address)
jane =copy.deepcopy(john)
print("---")
jane.address.street_address='123B Manchester Road'
print(john)
print(jane)
    
