numbers = [10, 20, 30, 40, 50]

def get_next_number():
    for num in numbers:
        return num
        

def get_next_number2():
    for num in numbers:
        yield num
        

gtr = get_next_number() 
gtr2 = get_next_number2()

print(type(gtr))
print(type(gtr2))
print(hasattr(gtr, '__next__',))
print(hasattr(gtr2, '__next__',))

'''
Output:
<class 'int'>
<class 'generator'>
False
True
'''




x = get_next_number()
print(x)
print(x)
print(next(x))

'''
Output:
10
10
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-41-86787ebf2884> in <module>
      2 print(x)
      3 print(x)
----> 4 print(next(x))

TypeError: 'int' object is not an iterator
'''


def get_all_numbers():
    num_list = []
    for num in numbers:
        num_list.append(num)
    return num_list

z = get_all_numbers()
print(z)

'''
Output:
[10, 20, 30, 40, 50]
'''


y = get_next_number2()
print(y)

'''
Output:
<generator object get_next_number2 at 0x109251050>
'''





y = get_next_number2()
print(next(y))
print(next(y))
print(next(y))

'''
Output:
10
20
30
'''


cities = ['New York', 'Warsaw', 'Berlin', 'Paris', 'Las Vegas']

i = 0
for city in cities:
    i+=1
    print(i, city)

'''
Output:
1 New York
2 Warsaw
3 Berlin
4 Paris
5 Las Vegas
'''



for i, city in enumerate(cities, 1):
    print(i, city)

'''
Output:
1 New York
2 Warsaw
3 Berlin
4 Paris
5 Las Vegas
'''


country = ('Poland', 'Germany', 'USA', 'France', 'Japan')
capital = ('Warsaw', 'Berlin', 'Washington', 'Paris', 'Tokyo')

place = zip(country, capital)
place_dict = dict(zip(country, capital))

print(place)
print(place_dict)

'''
Output:
<zip object at 0x109325d20>
{'Poland': 'Warsaw', 'Germany': 'Berlin', 'USA': 'Washington', 'France': 'Paris', 'Japan': 'Tokyo'}
'''




for place in list(zip(country, capital)):
    print(place)

'''
Output:
('Poland', 'Warsaw')
('Germany', 'Berlin')
('USA', 'Washington')
('France', 'Paris')
('Japan', 'Tokyo')
'''







numbers = [10, 20, 30, 40, 50]

def get_all_numbers():
    num_list = [x for x in numbers]
    return num_list

z = get_all_numbers()
print(z)

'''
Output:
[10, 20, 30, 40, 50]
'''



def get_coordinates():
    x = random.randint(1,10)
    y = random.randint(1,100)
    return x,y

print(type(get_coordinates()))

corr = get_coordinates()
first, second = get_coordinates()

print('first coordinate ', first)
print('second coordinate ', second)

'''
<class 'tuple'>
first coordinate  2
second coordinate  74
'''


def get_coordinates():
    x = random.randint(1,10)
    y = random.randint(1,100)
    z = random.randint(1,200)
    return x, y, z

corr = get_coordinates()
first, *second = get_coordinates()

print('first coordinate ', first)
print('second coordinate ', second)

'''
Output:
first coordinate  9
second coordinate  [38, 27]
'''



for more info go to website  here ---> https://pyplane.com/blog/5-python-tips-and-tricks/

