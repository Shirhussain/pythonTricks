#in python you can return more than one valus

def foo():
    a=20
    b=40
    return a,b 

x,y = foo()
print(x,y)


#Combining multiple string we can eassily concatenate all the tokens available in the list.

country = ["Afhganistan", "USA", "China","india","UK"]

print(" * ".join(country))
# between qoutation you can add whatever you want, for example i use here *


#wnna know the python version ??

import sys
print("python version isn ",sys.version)

# store all values of list in new separate vaiables.
mylist = [1,2,3,5,7]
print('mylist is ',mylist)

p,q,r,s,t =mylist

print('p is ',p)
print('q is ',q)
print('r is ',r)
print('s is ',s)
print('t is ',t)


#convert nested list into one list. Example [[1,2],[3,4],[5,6]] sould be converted into [1,2,3,4,5,6]
list_of_lists = [[1,2],[3,4],[5,6]]

flattend_list = [y for x in list_of_lists for y in x ]
print(flattend_list)

# in above example first 'for x in list_of_lists' execute then "for x in list_of_lists for y in x" will execute then pass the data to y finaly 


# unconventinal way to describe a function: Lambda 

subtract = lambda a,b: a-b
mnf=subtract(100,50)
print(mnf)

