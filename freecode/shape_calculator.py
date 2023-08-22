
class Rectangle:

    def __init__(self ,width, height):
        self.width = width
        self.height = height

    def set_width(self ,width):
        self.width =width

    def set_height(self, height):
        self.height =height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return ("Too big for picture.")
        else:
            return ((("*" * self.width) + "\n") * self.height)

    def get_amount_inside(self, shape):
        areaGuest = shape.get_area()
        areaHome = self.get_area()
        i = 0
        while areaHome >= areaGuest:
            areaHome = areaHome - areaGuest
            i = i + 1
        return i

    def __str__(self):
        return (("Rectangle(width={0}, height={1})").format(self.width, self.height))

    # def get_amount_inside(self, my_shape):

    #     return (self.get_area() // my_shape.get_area())


class Square(Rectangle):
    def __init__(self, sideval):
        Rectangle.width = sideval
        Rectangle.height = sideval

    def set_side(self, sideval):
        Rectangle.set_height(self, sideval)
        Rectangle.set_width(self, sideval)

    def __str__(self):
        return (("Square(side={0})").format(self.width))


rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

