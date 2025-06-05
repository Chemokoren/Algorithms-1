# What is factory design pattern?
In Factory design pattern, what is the difference between Abstract Factory and Factory Method

# Factory Design Pattern
The Factory Design Pattern is a creational pattern used to create objects without specifying their exact class. It provides an interface for creating instances of a class while allowing subclasses to alter the creation process.

Instead of directly instantiating objects with new, the Factory Pattern encapsulates object creation logic, ensuring that the creation logic remains separate from the business logic.

## Difference Between Abstract Factory and Factory Method

Both Abstract Factory and Factory Method fall under the Factory pattern, but they serve different purposes.

### Factory Method Pattern:

Defines an interface for creating objects but allows subclasses to decide which class to instantiate.

Encourages the use of inheritance.

Typically uses a single factory method in a base class to create objects.

Example:

from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def create(self):
        pass

class ConcreteProductA(Product):
    def create(self):
        return "Product A Created"

class ConcreteProductB(Product):
    def create(self):
        return "Product B Created"

class FactoryMethod(ABC):
    @abstractmethod
    def factory_method(self):
        pass

class FactoryA(FactoryMethod):
    def factory_method(self):
        return ConcreteProductA()

class FactoryB(FactoryMethod):
    def factory_method(self):
        return ConcreteProductB()

<!-- Usage -->
```
    factory = FactoryA()
    product = factory.factory_method()
    print(product.create())  # Output: Product A Created
```

### Abstract Factory Pattern:
Works at a higher level, providing an interface for creating families of related objects without specifying concrete classes.

Encourages composition (rather than inheritance) to produce groups of objects.

Used when multiple factories produce different types of related objects.

Example:

from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self):
        pass

    @abstractmethod
    def create_service(self):
        pass

# Concrete Factory A
class FactoryA(AbstractFactory):
    def create_product(self):
        return ConcreteProductA()

    def create_service(self):
        return ConcreteServiceA()

# Concrete Factory B
class FactoryB(AbstractFactory):
    def create_product(self):
        return ConcreteProductB()

    def create_service(self):
        return ConcreteServiceB()

class ConcreteProductA:
    def operation(self):
        return "Product A Operation"

class ConcreteServiceA:
    def operation(self):
        return "Service A Operation"

class ConcreteProductB:
    def operation(self):
        return "Product B Operation"

class ConcreteServiceB:
    def operation(self):
        return "Service B Operation"

<!-- # Usage -->
```
    factory = FactoryA()
    product = factory.create_product()
    service = factory.create_service()
    print(product.operation())  # Output: Product A Operation
    print(service.operation())  # Output: Service A Operation
```



### Key Differences

#### Feature	        Factory Method	                            Abstract Factory
Purpose	                Creates single product	                    Creates families of related products
Flexibility	            Subclasses decide what to instantiate	    Provides a unified interface for related objects-implementation  Uses inheritance	                         Uses composition
Example Use Case	    When one class creates objects	            When a group of related objects must be
                                                                    instantiated together

### When to Use Each
Use Factory Method when a single object creation needs to be controlled by subclasses.
Use Abstract Factory when multiple related objects need to be created together, ensuring consistency across a product family.

Would you like a real-world analogy or additional refinements for your use case? 🚀