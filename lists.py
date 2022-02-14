#Using python to manipulate lists

'''
Python knows a number of compound data types, 
used to group together other values. The most
versatile of which is a list.
Others include:
tuple
dictionary
set

Lists are written as a list of comma-separated 
values (items) between square brackets

Lists are mutable - this means that items can be changed

List have a bunch of methods available.
append() Adds an element at the end of the list
clear()	Removes all the elements from the list
copy() Returns a copy of the list
count()	Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list
'''

#The basics
squares = [1, 4, 9, 16, 25]
squares

#Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   
-9  -8  -7  -6  -5  -4  -3  -2  -1
'''

squares[0]  # indexing returns the item
squares[-1]
squares[-3:]  # slicing returns a new list


#Create a list copy
squares[:]

#Concatenation (glue together)
squares + [36, 49, 64, 81, 100]

#Alter items
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
cubes

#list methods
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes

#Length
letters = ['a', 'b', 'c', 'd']
len(letters)


#Nesting
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]


#List comprehension
y = []
for x in range(10):
    y.append(x**2)

y
y = [x**2 for x in range(10)]
y

#built-in function list()
x = list(('bobby', 'at', 'didcoding','dot', 'com')) # creates a list object
x
