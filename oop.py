class PalyerCreate:

    membership = True #class Object Attributes thats are actual attribuit 
    def __init__(self,name):
        if self.membership:
        #if PlayerCreate.membership: also work
        
            self.name = name #attributes this are diyanamic actribuity 
    def run(self):
        print('Ok You Can Run Now ')
    def showName(self):
        print(f'My name is {self.name}')#its works 
        #print(f'My name is {PlayerCreate.name}')#not work as like #if PlayerCreate.membership: also work bcoz its not a class attributes 

    @classmethod
    def adding_thing(self,num1,num2):
        return num1+num2
    
    # @classmethod
    # def adding_thing1(cls,num1,num2):
    #     return cls('Create A INSTANE ',num1 + num2)  #return PalyerCreate('Create A INSTANE ',num1 + num2) 

    @staticmethod
    def adding_thing2(num1,num2):
        return num1 + num2 #dont need self or cls  

class AttacterType:

    def __init__(self,ttype):
        self.ttype = ttype
    def setType(self):

        if self.ttype < 10:
            self.ttype = self.ttype +9


print(PalyerCreate.adding_thing2(12,13))
p1 = PalyerCreate('name')
print(p1.adding_thing1(12,13))
print(PalyerCreate.adding_thing2(12,13))
