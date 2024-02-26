"Bridge Pattern Use Case Example"

from circle_implementer import CircleImplementer
from square_implementer import SquareImplementer
from circle import Circle
from square import Square

CIRCLE = Circle(CircleImplementer)
CIRCLE.draw()

SQUARE = Square(SquareImplementer)
SQUARE.draw()