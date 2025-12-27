# all members are static

class CEO:
    
    __shared_state ={
        'name': 'Steve',
        'age': 55
    }
    
    def __init__(self):
        self.__dict__ =self.__shared_state
        
    def __str__(self):
        return f'{self.name} is {self.age} years old'
    
class Monostate:
    _shared_state ={}
    
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__=cls._shared_state
        return obj
    
class CFO(Monostate):
    
    def __init__(self):
        self.name =''
        self.money_managed =0
        
    def __str__(self)->str:
        # return super().__str__()
        return f'{self.name} manages ${self.money_managed}bn'
    
if __name__=='__main__':
    ceo1 =CEO()
    print(ceo1)
    
    ceo2 =CEO()
    ceo2.age =77
    print("ceo 1:", ceo1)
    print("ceo 2:",ceo2)

    ceo2.name ='Tim'
    # 
    ceo3 =CEO()
    print(f"ceo 1:{ceo1}", f"ceo 2:{ceo2}", f"ceo 3:{ceo3}", sep='\n')

    cfo1 =CFO()
    cfo1.name='Sheryl'
    cfo1.money_managed=1

    print(cfo1)

    cfo2 =CFO()
    cfo2.name='Ruth'
    cfo2.money_managed=10

    print(f"cfo 1:{cfo1}", f"cfo 2:{cfo2}", sep='\n')