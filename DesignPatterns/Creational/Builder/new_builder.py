"""
Builder Creational Pattern

The idea is if we want to make a burger, we don't immediately have to pass in
all the parameters. We can use a BurgerBuilder instead. Having an individual
method for adding each ingredient whether it is a bun, patty or cheese, each
one will return a reference to the builder. Finally, we will have a build
method which will return the final product.

use: protocol buffers
"""
class Burger:
    
    def __init__(self):
        self.buns   = None
        self.patty  = None
        self.cheese = None
        
    def setBuns(self, bunStyle):
        self.buns = bunStyle
        
    def setPatty(self, pattyStyle):
        self.patty = pattyStyle
        
    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle
        
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()
        
    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self
    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self
    def build(self):
        return self.burger
    
burger = BurgerBuilder()\
            .addBuns("sesame")\
            .addPatty("fish-patty")\
            .addCheese("swiss cheese")\
            .build()
                   
        
    