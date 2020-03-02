def mulTiply(li):
    n_list = []
    for list_a in li:
        n_list.append(list_a+2)
    return n_list
print(mulTiply([1,2,6,4]))
#efact on outside World 

my_list = [4,5,6,8,8]
def multiplae (items):
    return items*2

# calling this fun with data 
print(multiplae(my_list))
# Using Map On Funtions Programming 
print(list(map(multiplae,my_list)))

#create a fun for any itmes are Showing twitch Time 


def twitch(item):
    return f'{item }' f' This is Calling Concatinate {item}'
# map fun must be taken 2nd parametter are iterable and fist paramitter are takken fun , working with eatch items on this functions 
print(list(map(twitch,[ i for i in range(10) if i> 2 ]))) #twitch taken i and work on its and return it to list object 


# Using ZIP fun 4,7,89
my_list1 = [7,8,9,1,4,7]
your_list = list(range(7))

print(list(zip(my_list1,your_list)))