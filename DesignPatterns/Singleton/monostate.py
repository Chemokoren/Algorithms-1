""" all members are static :) """
class CEO:
    __shared_state ={
        'name': 'Steve',
        'age': 55
    }
    def __init__(self):
        self.__dict__= self.__shared_state
        
    def __str__(self):
        return f'{self.name} is {self.age} years old'
    
class Monostate:
    __shared_state ={}
    
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__=cls.__shared_state
        return obj
    
class CFO(Monostate):
    def __init__(self):
        self.name =''
        self.money_managed = 0
        
    def __str__(self):
        return f'{self.name} manages ${self.money_managed}bn'
    
if __name__ =='__main__':
    ceo1 = CEO()
    print("CEO 1:",ceo1)
    
    ceo1.age =66
    
    ceo2 =CEO()
    ceo2.age =77
    print("CEO 1:",ceo1)
    print("CEO 2:",ceo2)
    
    ceo2.name ='Tim'
    
    ceo3 = CEO()
    print("THEE CEOS:", ceo1, ceo2, ceo3)
    
    cfo1 = CFO()
    cfo1.name ='Sheryl'
    cfo1.money_managed=1
    
    print("CFO1:", cfo1)
    
    cfo2 =CFO()
    cfo2.name='Ruth'
    cfo2.money_managed =10
    print("CFO1:", cfo1)
    print("CFO2:",cfo2)