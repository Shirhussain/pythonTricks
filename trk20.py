# this module is print some funthing we have in python, like ==> Beautiful is better than ugly.

# (0)  import this




# (1) Enum -> in the following example i use the range and wnna start from 1 up to 3 if i don't give the number 1 it will start from 0  

class Enum:
    shir, Bill, Jeff = range(1,4)

# if i want to access to the values i cand do the following 
print(Enum.shir)
#or 
print(Enum.shir==1) # it will print to True






# (2) there is no diffrence in following examples
x,y,z = 1,2,3
print(x,y,z)
a,b,c = (4,5,6)
print(a,b,c)
d,e,f = [7,8,0]
print(d,e,f)






# (3)  F string which will let you to use instead of formating

name = "shir"
age = 22
print("Hello my name is ", name, "and I am ",age , "yeaers old")
print("Hello my name is "+name+" and i am "+str(age)+"yeares old")

# the nice thing in f string is you can add something in your values
# if you gnna you Upper case (F) also there is no diffrence

st = f"Hello my name is {name} and i am {age +10}"
print(st)





# (4) if we need the index of our list so you can do the following but be4 that i wil show you the old way 

z = [3,5,6,7,90]

for i in range(len(z)):
    print(i, z[i])

# the new way or trick is here we go

for i, e in enumerate(z):
    print(i,e)





# (5) The zip function ===> it's very usefull when we wnna access the same element from multiple list 
# first i will show you the old way then have a look at the trick

names = ["Shir","jeff","Ellon","Bil"]
ages  = ["22", "50","40","70"]

fav_color = ["blud","green","yellow","gray"]


for i in range(len(names)):
    print(names[i],ages[i],fav_color[i])

#trick is here the first one is with tuple 

print(list(zip(names,ages,fav_color)))

# we can ittrate with for 

for tup in zip(names, ages, fav_color):
    print(tup)

# if u wnna remove the tupe so do the following

for name, age, color in zip(names, ages, fav_color):
    print(name, age, color)




# (6) this one Hellp, it's extremely usefull when you want to look for spesific ductumentation, method or  classes like that 

#help(list)
# or you use specific module like os, every documentation comes along 
import os 
help(os)





# (7) it's Dir function it's good when yo wnna look at sepcific method or function of object 

z = ""
print(dir(z))

# it's very usfull when you import some module like queue 

import queue 
print(dir(queue.Queue))





# (8) List comprehention 

z = [i for i in range(8)]
print(z)

# also you can add some if string as well 

z = [i for i in range(10) if i%2 ==0 ]
print(z)

# also i can use nested list as well -> here we go 

z = [[] for i in range(8)]
print(z)

# or
z = [[100,500] for i in range(8)]
print(z)

# or even we can use nest for as well 

z = [[j for j in range(i)] for i in range(8)]
print(z)
# which is printing something like this [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6]]

# also you can use zip 
z = [[x,y] for x,y in zip(range(5), range(5,10))]
print(z)

# which is printing something lie this [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]

# ofcourse you can jsut print x or y 

z = [x for x,y in zip(range(5), range(5,10))]
print(z)
# you will get this -> [0, 1, 2, 3, 4]

# if you don't need the variable you can use anonymous variable ( _ ) as well, it will not asign anything or store anything also you can not access

for _ in range(5):
    print("Hello Shir Husain Danishya")
# it dosn't matter if you put (i) or ( _ )  just ( _ ) looks a lettle bit cleaner, it tell that we will not relay on this variable 

z = [x for x,_ in zip(range(5), range(5,10))]
print(z)




# (9) .join which is use for joining or concatinating list of values 

country = ['Afghanistan', 'USA','USB','UK','China','India']
print("".join(country))
# inside the qotation any sperator you can use 




# (10) Reversing

st = "Afghanistan"
print(st[::-1])




# (11)  printing Hellow world by using  
# import __hello__





# (12) if you wnna print the size of something you can use sys in byte 
import sys

a = 10000
print(sys.getsizeof(a))





# (13) for showing max of something 

a = [1,2,3,4,5,5,5,5,5,4,3,3,3,3,3,3,11,1,1,1,1,1,1,1,1,1,1,6,6,6,6]

print(max(set(a), key =a.count))
# the above example print (1) 

# for advance one you can use lambda 

a = [(1,3,5,6),(4,5,4,3),(3,0,2,1)]
print(max(a, key=lambda y: y[2]))
# which is printing (1, 3, 5, 6) for index 2 the max is 5 that's y it print 





# for some fun you can u can use antigravity 

import antigravity





# (14) you can multply the string to print multiple time 

print("hello "*10+"i love you "*5)





# (15) using *args but if you wnna use dictionary so you have to use **kwargs 

def func(*args):
    print(args)

func(2,3,5,5,0)
func(1,3,5,65,6,5,000,2)

# using both 

def func(*args, **kwargs):
    print(args, kwargs)

func(34,5,2,5,a=20, d=30,y=z)


