def mine(string):
    def wrapper():
        print("Started")
        print(string)
        print("Ended")

    # return wrapper()
    return wrapper

x =mine("hello")
print(x)
x()

print("#######################################")
def func(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")
    return wrapper

def func2():
    print("I am func2")
def func3():
    print("I am func3")

x =func(func3)
y =func(func2)
print(x)
print(y)
x()
y()

print("############ Alternative #############")

func3 =func(func3)
func2 =func(func2)
func3()
func2()

print("############ Decorators #############")
@func
def func4():
    print("I am func4")
@func
def func5():
    print("I am func5")

func4()
func5()


print("############ unlimited arguments #############")
def funct(f):
    def wrapper(*args, **kwargs):
        print("Begin")
        f(*args,**kwargs)
        print("End")
    return wrapper

@funct
def trial1(x,y):
    print(x,y)

@funct
def trial2():
    print("I am trial 2")

trial2()
trial1(5,6)

print("############ return  #############")
def myFunc(f):
    def wrapper(*args,**kwargs):
        print("Started")
        rv =f(*args,**kwargs)
        print("Ended")
        return rv
    return wrapper

@myFunc
def deFunc(x,y):
    print(x)
    return x

@myFunc
def deFunc2():
    print("I am the function")

x =deFunc(5,6)
print(x)

print("############ timer  #############")
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start =time.time()
        rv =func()
        total =time.time() - start
        print("Time:", total)
        return rv
    return wrapper

@timer
def test():
    for _ in range(1000):
        pass

@timer
def test2():
    time.sleep(2)

test()
test2()