"""
# Pylint Tutorial

"""

#pylint: disable=too-few-public-methods
class Car:
    """Example class"""
    def __init__(self, color):
        self.color = color

MYCAR = Car('blue')

def crash(car1, car2): #pylint: disable=unused-argument
    """ An example function"""
    car1.color = 'burnt'

crash(Car('red'), MYCAR)
