"""
Imagine that you want a burger, but you don't want to worry about getting all
the ingredients and putting them together, so instead, you just order a burger.

We can do the same thing with code:

if it takes a list of ingredients to create a burger, we can instead use a 
factory which will instantiate the burger for us and return it to us whether 
it is a cheeseburger, a deluxecheeseburger or a veganburger.

All we have to do is tell the factory what kind of burger we want just like
we do at a restaurant.

But, be careful because this way, you will never know what is inside the 
special sauce(burger).

Alternatively, if you want alittle more control over how the sausage is made,
you can go with the builder pattern.

"""
class Burger:
    
    def __init__(self, ingredients):
        self.ingredients = ingredients
        
    def print(self):
        print(self.ingredients)
        
class BurgerFactory:
    
    def createCheeseBurger(self):
        ingredients =["bun", "cheese", "beef-patty"]
        return Burger(ingredients)
    
    def createDeluxeCheeseBurger(self):
        ingredients =["bun","tomatoe", "lettuce", "cheese", "beef-patty"]
        return Burger(ingredients)
    
    def createVeganBurger(self):
        ingredients =["bun", "special-sauce", "veggie-patty"]
        return Burger(ingredients)
    
burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger().print()
burgerFactory.createDeluxeCheeseBurger().print()
burgerFactory.createVeganBurger().print()