# Design Patterns
-Design patterns are common architectural approaches
-Popularized by the Gang of Four(GoF) book(1994 -Smalltalk & C++)
-Universally relevant
    - Internalized in some programming languages
    - Libraries
    - Your own code
## SOLID Design Principles
- Set of design principles  related to software design (selection of 5 desing principles from a large number)
- Introduced by Robert C. Martin
- Frequently referenced in design pattern literature
### Single Responsibility principle (SRP/SOC-Seperation of concerns)
- A class should only have one reason to change
- Seperation of concerns - different classes handling different, independent tasks/problems
### Open Closed Principle (OCP)
- class is open for extension but closed for modification
### Liskov Substitution principle
- You should be able to substitute a base type for  subtype
### Interface Segregation Principle
- Don't put too much into an interface; split into seperate interfaces
- YAGNI - You Ain't Going to Need it
### Dependency Inversion Principle
- High-level modules should not depend on low-level ones; use abstractions


## Design Patterns
    - Creational
    - Structural
    - Behavioral
"""



Gamma Categorization
--------------------
Design Patterns are typically split into three categories
- This is called Gamma Categorization after Erich Gamma, one of GoF authors

Creational Patterns 
-------------------
- Deal with the creation (construction) of objects
- Explicit (constructor) vs. implicit (DI, reflection, etc.)
- Wholesale (single statement) vs. piecewise (step-by-step)

a) Builder
b) Factories
    -Abstract Factory
    -Factory Method
c) Prototype
d) Singleton

Structural Patterns
-------------------
- concerned with the structure (e.g. class members)
- Many patterns are wrappers that mimic the underlying class' interface
- Stress the importance of good API design

a) Adapter
b) Bridge
c) Composite
d) Decorator
e) Facade
f) Flyweight
g) Proxy

Behavioural Patterns
--------------------

- They are all different; no central theme 
- They are all doing their own thing/ there is some overlap here and there e.g the strategy
and the template method design patterns. They are kind of doing the same thing but they are doing it using completely different object oriented mechanisms
- Each is unique in their approach meaning that they solve a particular problem in a particular way, have a particular set of concerns etc.

a) Chain of Responsibility
b) Command
c) Interpreter
d) Iterator
e) Mediator
f) Memento
g) Observer
h) State
i) Strategy
j) Template Method
k) Visitor
"""

# Creational Design Pattern: ## Reflection
* In creational design patterns, one of the options for implicitly creating objects involves using reflection. 
* Reflection allows a program to examine its own structure and behavior at runtime. This can be leveraged to instantiate objects without directly invoking their constructors. 
* Let's look at an example using the Factory Method pattern, a creational pattern, and how reflection can be used to implicitly create objects.

## Factory Method Pattern:

The Factory Method pattern provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. This pattern helps promote loose coupling between the creator (factory) and the created objects.

### Implicit Object Creation with Reflection:

Reflection in Python can be used to dynamically create objects without directly invoking their constructors. Here's a simple example of how this can work with the Factory Method pattern:

Suppose we have a base class Product and two subclasses ConcreteProductA and ConcreteProductB:

```

class Product:
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "Product A"

class ConcreteProductB(Product):
    def operation(self):
        return "Product B"

```

Now, let's create a factory class that uses reflection to dynamically create objects based on a given product type:

```
class ProductFactory:
    @staticmethod
    def create_product(product_type):
        class_name = f"ConcreteProduct{product_type}"
        product_class = globals()[class_name]
        return product_class()

# Usage
product_type = "A"
product = ProductFactory.create_product(product_type)
print(product.operation())  # Output: Product A


```

* In this example, we use the globals() function to access the global symbol table and retrieve the class corresponding to the desired product type. This way, we're using reflection to instantiate the appropriate product class based on the given type.

* While using reflection for object creation can provide flexibility, it also comes with potential downsides, such as decreased performance, reduced compile-time type checking, and increased complexity. It's important to carefully consider whether using reflection is the best approach for your specific use case, and to document the code clearly to indicate its usage.

* Also, remember that Python's dynamic nature and strong support for introspection and reflection make it well-suited for this kind of approach. Other programming languages might have varying degrees of support for reflection, and the techniques might differ based on the language's features and limitations.

# Creational Design Pattern: ## DI

* Dependency Injection is a design pattern that promotes loose coupling between components by allowing dependencies to be injected from the outside rather than being created internally.

* In the context of implicit object creation, DI involves providing dependencies to a class or component without that class being responsible for creating those dependencies. 
* This can be achieved through constructor injection, setter injection, or interface-based injection. Let's see how this works in the context of a creational pattern, such as the Abstract Factory pattern.

## Abstract Factory Pattern with Implicit Object Creation using DI:

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. Using DI, we can implicitly create objects by injecting the factory responsible for creating those objects.

Suppose we have an abstract factory for creating different types of products:

```
class AbstractFactory:
    def create_product(self):
        pass

class ConcreteFactoryA(AbstractFactory):
    def create_product(self):
        return ConcreteProductA()

class ConcreteFactoryB(AbstractFactory):
    def create_product(self):
        return ConcreteProductB()


```

* Now, let's implement a client class that relies on the abstract factory:

```

class Client:
    def __init__(self, factory):
        self.factory = factory
    
    def get_product(self):
        product = self.factory.create_product()
        return product.operation()

# Usage
factory_a = ConcreteFactoryA()
factory_b = ConcreteFactoryB()

client_a = Client(factory_a)
client_b = Client(factory_b)

print(client_a.get_product())  # Output: Product A
print(client_b.get_product())  # Output: Product B

```

In this example, the Client class is dependent on an AbstractFactory instance. The factory is injected into the client's constructor, and the client retrieves a product from the factory using DI.

### Advantages of Implicit Object Creation using DI:

   -  Flexibility: DI allows you to change the behavior of a class by changing the injected dependencies without modifying the class itself.

   - Testability: With DI, you can easily inject mock or stub objects for testing purposes, facilitating unit testing.

   - Loose Coupling: Components become loosely coupled since they don't directly create their dependencies.

   - Reusability: The same components can be used with different implementations of dependencies, promoting code reuse.

Note: While DI is a powerful technique for managing dependencies and promoting flexibility, it requires careful design and management of object lifetimes and scopes. Overusing DI can lead to complex configuration and reduced performance, so it's important to strike the right balance based on the needs of your application.