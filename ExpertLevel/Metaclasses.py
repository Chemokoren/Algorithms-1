def hello():
    class Hi:
        pass

    return Hi
class Test:
    pass

print(Test)
print(Test())

print("\n################## different implementations of a class ###################### \n")

class Testi:
    pass

Testi2 = type('Test',(), {})

print(type(Testi))
print(type(Testi2))
print(type(Testi2()))

print("################## breaking down class implementation {}=variables ######################")
Mami = type('Test',(), {"x":5})

m =Mami()
m.wy ="hae"
print(m.x)
print(m.wy)

print("################## inheritance ######################")
class Foo:
    def show(self):
        print("hi")

def add_attribute(self):
    self.z =9

Koko =type('kat', (Foo,), {"x":9, "add_attribute":add_attribute})
k =Koko()
k.show()
k.add_attribute()
print(k.z)

print("################## Real Metaclasses ######################")
class Meta(type):
    def __new__(self,class_name,bases,attrs):
        print(attrs)

        a ={}
        for name,val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] =val
        print("aaa:",a)
        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x =5
    y =8

    def hello(self):
        print("hi")

d =Dog()
print(d.HELLO())