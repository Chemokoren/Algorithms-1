from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color =color

    @abstractmethod
    def display():
        pass

    def print_color(self):
        return self.color.get_color()

class Circle(Shape):
    def display(self):
        print("Circle")

class Square(Shape):
    def display(self):
        print("Square")

    
class Color(ABC):

    @abstractmethod
    def get_color(self):
        pass

class Red(Color):
    def get_color(self):
        print("Red Color")

class Green(Color):
    def get_color(self):
        print("Green Color")


red =Red()
green=Green()

green_square =Square(green)
green_square.display()
green_square.print_color()