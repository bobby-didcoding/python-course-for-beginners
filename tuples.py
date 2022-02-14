#Using python to manipulate tuples

'''
Python knows a number of compound data types, 
used to group together other values.
They are:
tuple
dictionary
set
list

Tuples are written as a list of comma-separated 
values (items) between parentheses.


Tuples are immutable - this means that items can not be changed. However,
a tuple can contain mutable objects.

Tuple has 2 methods available.
count()	Returns the number of elements with the specified value
index() Returns the index of the first element with the specified value
'''

#The basics - tuple packing
t = 12345, 54321, 'hello!'
t[0]
t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v

#Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   
-9  -8  -7  -6  -5  -4  -3  -2  -1
'''

t[0]  # indexing returns the item
t[-1]

#trailing comma
empty = ()
singleton = 'hello',
len(empty)
len(singleton)
singleton

#Unpacking a tuple
x, y, z = t
x
y
z

#built-in function tuple()
x = tuple(['bobby', 'at', 'didcoding','dot', 'com']) # creates a tuple object
x

#Tuple comprehension...Just use list comprehension with the tuple function
tuple([x**2 for x in range(10)])