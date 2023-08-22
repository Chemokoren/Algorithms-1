"""

"""
import copy

class Address:
    
    def __init__(self, street_address, city, suite):
        self.city = city
        self.street_address = street_address
        self.suite = suite
        
    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'
    
class Employee:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def __str__(self) -> str:
        return f'{self.name} workes at {self.address}'
    
class EmployeeFactory:
    main_office_employee = Employee('', Address('123 East Dr', 'London', 0))
    aux_office_employee = Employee('', Address('123B East Dr', 'London', 0))
    
    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result
    
    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name,suite
            )
    
    @staticmethod
    def aux_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name,suite
            )
        
john = EmployeeFactory.new_main_office_employee('John', 100)
jane = EmployeeFactory.aux_main_office_employee('Jane', 500)

print(john)
print(jane)
    