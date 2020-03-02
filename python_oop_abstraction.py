class PalyerCreate:

    membership = True #class Object Attributes thats are actual attribuit 
    def __init__(self,name):
        if self.membership:
        #if PlayerCreate.membership: also work
        
            self.name = name #attributes this are diyanamic actribuity 
    def run(self):
        print('Ok You Can Run Now ')

    def speak(self):
        print(f"My Name is {self.name} and nich ")
    def showName(self):
        print(f'My name is {self.name}')#its works 
        #print(f'My name is {PlayerCreate.name}')#not work as like #if PlayerCreate.membership: also work bcoz its not a class attributes 

    @classmethod
    def adding_thing(self,num1,num2):
        return num1+num2
    
    # @classmethod
    # def adding_thing1(cls,num1,num2):
    #     return cls('Create A INSTANE ',num1 + num2)  #return PalyerCreate('Create A INSTANE ',num1 + num2) 
    #this cls are change his own arrtriube and relaiabame on this properthic s 

    @staticmethod
    def adding_thing2(num1,num2):
        return num1 + num2 #dont need self or cls  


p1 = PalyerCreate('Boabe')

p1.speak = 'Hello I change Your Method '
print(p1.speak())#ha ha ha ha ha ha ha ha 

# create A supper inheritance class 

class User(object):
	membership = True
	def __init__(self, user,password):
		if self.membership:
			self._user = user
			self._password = password
	def registration(self):
		def __len__(self):
			return 5
		def __call__(self):
			return 'Hyi this is nachi game'
		if len(self._password)==5:
			User.membership = False
	def login(self):
		print('LOGIN')
	def attack(self):
		print('Nothing To Do')

class AnotherPlayer(User):
	def __init__(self,name,power,email):
		super().__init__(self,email)
		self.name = name
		self.power = power
		
	def attack(self):
		User.attack(self)
		print(f'Number Of power is {self.power}')
class Wizer(User):
	def __init__(self,name,power,email):
		User.__init__(self,email)
		self.name = name
		self.power = power
		
	def attack(self):
		User.attack(self)
		print(f'Number Of power is {self.power}')
#do it tow Way 
class AcharPalyer(User):
	def __init__(self,name,num_arch,email):
		self.name = name
		self.num_arch = num_arch
		self.email = email
		
	def attack(self):
		print(f'Number Of archer is {self.num_arch}')		

			
	##Funtional Programming 