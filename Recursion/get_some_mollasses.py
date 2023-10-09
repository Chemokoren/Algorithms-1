def getMolasses(n: Neighbor)->Ingredient:
    """ Method to recursively get some molasses from the neighbor"""
    c = MeasuringCup()
    if(hasMolasses(neighbor)):
        return molasses
    else:
        m = getMolasses(n.getNeighbor()) # is an Ingredient
        c.add(m)

# Talia, the Tail Recursive Chef

