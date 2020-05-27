hero_name = ('Iron Man','Captain America','HawKeye','Black Widow')
first_last_name = ('Tony Stark','Steve Rogers','Clint Barton','Natasha Romanova')

# here i gonna create a dictionary with key and value 
heros = dict(zip(hero_name,first_last_name))

print(heros)

# if i gonna reverse it so i have to do the following
heros.keys()
#or 
heros.values()

print(heros.values())
# if i use (item) i will get a list of tuple that contain key and value 
heros.items()
print(heros.items())

# if i wanna reverse this dictionary(heros.items) which key bacom a value and value bacome a key 

heros_reverse = {value:key for key, value in heros.items()}
print(heros_reverse)



heroes = ['Iron Man', 'Captain America','Hawkeye','Black Widow']

i=0
for hero in heroes:
    #if i wanna start from one so i have to put (i+=1) befor print otherwise if i wnna start from zero  so i put afther print
    print(i,hero)
    i+=1

# another cool way is called enumeration

for i, hero in enumerate(heroes):
    print(i,hero)
# if i wnna start from specific number so i have to define it as follows 

for i, hero in enumerate(heros,10):
    print(i,hero)













# get all position metting and criteria

avengers = ['Hulk','Spiderman','Iron Man','Thor','Captain America','Hulk']
avengers.index('Hulk')
print(avengers.index('Spiderman'))

# as you can se in avengers we have to position for 'Hulk' but we just got the first one not the last one so i have to do the following style to find out both positions

# i need to define a condation 

hulk_positions = [i for i,x in enumerate(avengers) if x=='Hulk']
print(hulk_positions)

hulk_positions.append('one')
print(hulk_positions)
# apply debuging statments into the code with the use of assert 

# here i will caheck if it's not an (integer)  so it should give me and error with ( Wrong type of data in position {i}

for i, pos in enumerate(hulk_positions):
    assert isinstance(pos, int), f'Wrong type of data in position {i}'







# get highest Argument position

numbers = [0,10,40,23,13,0,343,100,999]
print(max(numbers))

# we got 999 but we want the position of 999 so i use numpy
import numpy as np

highest_value_position = np.argmax(numbers)
print(highest_value_position)
