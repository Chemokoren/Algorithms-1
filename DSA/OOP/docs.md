### Encapsulation

**Encapsulation** is the practice of bundling data (attributes) and the methods that operate on that data into a single unit, a class. It restricts direct access to some of an object's components, which prevents unauthorized or unintended changes.

In Python, we achieve this by using naming conventions:

  * A single leading underscore (`_`) on a variable (e.g., `_salary`) indicates that it is a **protected** attribute, a signal to other developers that it should not be accessed directly from outside the class.
  * A double leading underscore (`__`) on a variable (e.g., `__bank_account`) makes it a **private** attribute, which Python's name mangling system makes very difficult to access from outside the class.

**Example:**

```python
class Employee:
    def __init__(self, name, salary):
        # Protected attribute
        self._name = name

        # Private attribute using name mangling
        self.__salary = salary

    def get_salary(self):
        """A public method to safely access the salary."""
        return self.__salary

    def set_salary(self, new_salary):
        """A public method to safely update the salary."""
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary cannot be negative.")

# Create an object
emp = Employee("Alice", 50000)

# The private attribute is not directly accessible
# print(emp.__salary) # This will raise an AttributeError

# Instead, we use a public method to access it
print(f"Alice's salary is: {emp.get_salary()}")

# We use a public method to safely change it
emp.set_salary(60000)
print(f"Alice's new salary is: {emp.get_salary()}")
```

-----

### Inheritance

**Inheritance** is a mechanism where a new class inherits attributes and methods from an existing class. The existing class is called the **parent** or **base** class, and the new class is called the **child** or **derived** class. This promotes code reusability and establishes a logical relationship between classes.

**Example:**

```python
class Animal:
    """Parent class."""
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    """Child class inheriting from Animal."""
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    """Another child class inheriting from Animal."""
    def speak(self):
        return f"{self.name} says Meow!"

# Create objects of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())
```

-----

### Polymorphism

**Polymorphism** means "many forms." In OOP, it refers to the ability of a method to act differently based on the object that calls it. This is often achieved through inheritance, where child classes can **override** the parent class's methods to provide their own specific implementation.

**Example:**

Using the `Animal`, `Dog`, and `Cat` classes from the inheritance example, the `speak()` method is a perfect illustration of polymorphism. Even though both `Dog` and `Cat` have a `speak()` method, the output is different because each class provides its own unique implementation.

```python
def make_it_speak(animal):
    """A function that works with any object of type Animal."""
    print(animal.speak())

make_it_speak(Dog("Rex"))
make_it_speak(Cat("Garfield"))
```

-----

### Defining Classes

A class is a blueprint for creating objects. It defines a set of **data attributes** and **methods** that the objects of that class will have.

#### Data Attributes

These are the variables that store the state of an object.

  * **Instance Variables:** These belong to an individual object. Each object gets its own copy of the instance variables. They are defined inside the `__init__` method.

      * **Example:** `self.name` and `self.salary` in the `Employee` class.

  * **Class (Static) Variables:** These belong to the class itself, not to any single instance. All objects of the class share the same class variable. They are defined outside of any method.

      * **Example:**

    <!-- end list -->

    ```python
    class Student:
        # Class variable
        school_name = "Central High"

        def __init__(self, name):
            # Instance variable
            self.name = name

    s1 = Student("John")
    s2 = Student("Jane")

    print(f"{s1.name} attends {s1.school_name}")
    print(f"{s2.name} attends {s2.school_name}")

    # Changing the class variable affects all instances
    Student.school_name = "East High"

    print(f"{s1.name} now attends {s1.school_name}")
    ```

  * **Local Variables:** These are defined inside a method and only exist while the method is running. They cannot be accessed from outside the method.

      * **Example:** `new_salary` inside the `set_salary` method of the `Employee` class.

#### Methods

These are functions that are defined inside a class and describe the behaviors of an object.

  * **Instance Methods:** These are the most common type of method. They operate on an object's instance variables and take `self` as their first argument.

      * **Example:** The `get_salary()` and `set_salary()` methods in the `Employee` class.

  * **Class Methods:** These methods operate on the class itself, not on an instance. They take `cls` (short for class) as their first argument and are marked with the `@classmethod` decorator. They are often used as factory constructors.

      * **Example:**

    <!-- end list -->

    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @classmethod
        def from_birth_year(cls, name, year):
            # This is a class method that returns a new Person instance
            age = 2025 - year
            return cls(name, age)

    # Use the class method to create an object
    person = Person.from_birth_year("Bob", 1990)
    print(person.age)
    ```

  * **Static Methods:** These methods are not bound to an instance or the class. They don't take `self` or `cls` as their first argument and are marked with the `@staticmethod` decorator. They are essentially regular functions placed inside a class for logical grouping.

      * **Example:**

    <!-- end list -->

    ```python
    class MathUtil:
        @staticmethod
        def add(x, y):
            return x + y

    result = MathUtil.add(10, 20)
    print(result)
    ```