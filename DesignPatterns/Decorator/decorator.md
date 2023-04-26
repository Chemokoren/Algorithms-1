"""
Decorator
---------

- Adding behaviour without altering the class itself or inheriting from them

Motivation
- Want to augment an object with additional functionality
- Do not want to rewrite or alter existing code (OCP)
- Want to keep new functionality seperate (SRP)
- Need to be able to interact with existing structures

Two options:
-----------

- Inherit from required object (if possible)
- Build a decorator, which simply references the decorated object(s)

A decorator facilitates the addition of behaviours to individual objects without inheriting from them.

Summary
-------

- A decorator keeps the reference to the decorated object(s)
- Adds utility attributes and methods to augment the object's features
- May or may not forward calls to the underlying object
- Proxying of underlying calls can be done dynamically
- Python's fuctional decorators wrap fuctions; no direct relation to the GoF Decorator  pattern

"""
