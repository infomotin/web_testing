def aFun(getFun):
    getFun()

def greet():
    print('Have A Funny day')

a = aFun(greet)

# print(a)



#Hight Order Functions map filter reduce are HOC

def greeting (take_aFun):
    take_aFun()
def another_greet():
    def fun1():
        return 5
    return fun1

another_var = greeting(another_greet)

# print(another_var)



# How to Work on Decoretor 
def simpel_fun():
    print('Hello Fun')


def my_decoretor(func):

    status = True
    def exc_func():
        if status:
            print('***********')
            func()
            print('***********')
        else:
            pass
            
    return exc_func

# That Is Using Function Are 
@my_decoretor
def sim_funDeco():
    print("Hello Teko")

@my_decoretor
def haeve_aFun():
    sim_funDeco()

# sim_funDeco()
# haeve_aFun()


#Decoretor Fun With arguments 

#Build Decoretor Fun 

def my_deco(take_func):
    def excu_func(*args,**kwargs):
        print("''''''''@@@@@''''''''")
        take_func(*args,**kwargs)
        print("''''''''@@@@@''''''''")
    return excu_func

#using Decoretor 
@my_deco
def using_dec():
    print('Hello Decoretor ....')
# using_dec()


#Build Decoretor 
from time import time

def performance(take_func):
    def excut_fun(*args,**kwargs):
        st = time()
        r = take_func(*args,**kwargs)
        et = time()
        print(f'Excuting Time Are {-st + et } ms')
        return r
    return excut_fun



#using Decoretor for chaking performence 
@performance
def runTine_cal():
    for i in range(100000000):#if i % 2 !== 6:
        i = i*2
runTine_cal()
