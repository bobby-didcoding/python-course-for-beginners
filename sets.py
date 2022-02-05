#Using python to manipulate sets

'''
Python knows a number of compound data types, 
used to group together other values.
They are:
tuple
dictionary
set
list

A Set is an unordered collection with no duplicate elements. Like a dictionary,
a set is defined by a curly bracket.

Sets are mutable - this means that items can be changed.

Set has a whole bunch of methods available.
add() Adds an element to the set
clear() Removes all the elements from the set
copy() Returns a copy of the set
difference() Returns a set containing the difference between two or more sets
difference_update() Removes the items in this set that are also included in another, specified set
discard() Remove the specified item
intersection() Returns a set, that is the intersection of two or more sets
intersection_update() Removes the items in this set that are not present in other, specified set(s)
isdisjoint() Returns whether two sets have a intersection or not
issubset() Returns whether another set contains this set or not
issuperset() Returns whether this set contains another set or not
pop() Removes an element from the set
remove() Removes the specified element
symmetric_difference() Returns a set with the symmetric differences of two sets
symmetric_difference_update() Inserts the symmetric differences from this set and another
union() Return a set containing the union of sets
update() Update the set with another set, or any other iterable
'''

#The basics
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)# show that duplicates have been removed

'orange' in basket # fast membership testing
'crabgrass' in basket

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a # unique letters in a
a - b # letters in a but not in b
a | b # letters in a or b or both
a & b # letters in both a and b
a ^ b # letters in a or b but not both


#Set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}

#built-in function set()
x = set(('bobby','bobby', 'at', 'didcoding','dot', 'com')) # creates a set object
x