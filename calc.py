
def add(x,y):
    """Add Function"""
    return x + y

def subtract(x,y):
    """Subtract Function"""
    return x - y

def multiply(x,y):
    """Multiply Function"""
    return x*y

def divide(x,y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y
    # return x // y  -full division. it does not give decimals e.g 5/2 =2.5 however, it shows 2
