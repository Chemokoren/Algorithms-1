"""
"""
from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESIAN =1
    POLAR =2
    
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f'x: {self.x}, y: {self.y}'
    

# take out factory methods to a seperate class
class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))
if __name__ == '__main__':
    # p = Point(2, 3)
    p1 = PointFactory.new_cartesian_point(1,2)
    p2 = PointFactory.new_polar_point(1,2)
    print(p1, p2)