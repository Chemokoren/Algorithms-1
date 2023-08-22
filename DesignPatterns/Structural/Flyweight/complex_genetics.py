class ComplexGenetics(object):
    def __init__(self):
        pass
    
    def genes(self, gene_code):
        return "ComplexPatter[%s]TooHugeinSize" % (gene_code)
    
class Families(object):
    
    family ={}
    
    def __new__(cls, name, family_id):
        
        try:
            id =cls.family[family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.family[family_id] =id
        return id
    
    def set_genetic_info(self, genetic_info):
        cg =ComplexGenetics()
        self.genetic_info =cg.genes(genetic_info)
        
    def get_genetic_info(self):
        return (self.genetic_info)
    
def test():
    data =(('a',1,'ATAG'), ('a','2','AAGT'),('b',1,'ATAG'))
    family_objects =[]
    for i in data:
        obj =Families(i[0],i[1])
        obj.set_genetic_info(i[2])
        family_objects.append(obj)
        
    for i in family_objects:
        print("id  ="+ str(id(i)))
        print(i.get_genetic_info())
    print("similar id's says that they are same objects ")
    
if __name__ =='__main__':
    test()