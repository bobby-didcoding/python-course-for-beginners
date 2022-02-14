# Python classes

'''
Classes provide a means of bundling data and functionality together. Creating a 
new class creates a new type of object, allowing new instances of that type to be 
made.

Python classes provide all the standard features of Object Oriented Programming.
The class inheritance mechanism allows multiple base classes, a derived class 
can override any methods of its base class or classes, and a method can call 
the method of a base class with the same name.

The simplest form of class definition looks like this:
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

Class definitions, like function definitions (def statements) must be executed 
before they have any effect.
'''

#basics

class MyClass:
    """A simple example class"""
    i = 12345
    
    def f(self):
        return 'hello world'

MyClass.i # return the int
MyClass.f # returns a function object
MyClass.__doc__ # magic method/dunder method that return the text literal

x = MyClass() #instantiates the class
x.i # return the int
x.f() # calls the class method

'''
Notice how self is passed as the first arg!! 
We pass the methods instance object in as the first arg!
so x.f() is the equivalent of MyClass.f(x)
Note: 'self' has no special meaning to Python - it's just convention
'''

#Class with special initial state - we user __init__
#allows us to pass args to the class for greater flexibility
class MyClass:
    """A simple example class"""
    def __init__(self, my_int:int):
        self.i = my_int
    
    def f(self):
        new = self.i ** 3
        return new

x = MyClass(4) #instantiates the class
x.i # return the int
x.f() # calls the class method

#Instance objects
#We can add and delete attributs to our object

x.counter = 1 # Add a data attribute and assign a value
while x.counter < 10:
    x.counter = x.counter * 2
    #first loop x.counter == 2
    #second loop x.counter == 4
    #third loop x.counter == 8
    #forth loop x.counter == 16
    #fifth loop does not start as x.counter > 10

print(x.counter) #prints 16
del x.counter # delete the data attribute
print(x.counter) # AttributeError

#Class and Instance Variables
class Dog:
    kind = 'canine' # class variable shared by all instances
    def __init__(self, name):
        self.name = name# instance variable unique to each instance
        
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.kind
e.kind
d.name
e.name
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks

#Inheritance

'''
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

Execution of a derived class definition proceeds the same as for a base 
class. When the class object is constructed, the base class is remembered. 
This is used for resolving attribute references: if a requested attribute 
is not found in the class, the search proceeds to look in the base class. 
This rule is applied recursively if the base class itself is derived from 
some other class.

Derived classes may extend or override methods of their base classes.
'''

class Mapping:
    '''
    Private variable example.
    checkout __update - this is called name mangling  
    Is done without regard to syntactical position
    '''
    def __init__(self, iterable):
        self.items_list = []
        self.iterable = iterable
    
    def update(self):
        for item in self.iterable:
            self.items_list.append(item)    

class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

m = MappingSubclass([1,2,3,4])
m.items_list
m.update(["one","two","three"], ["these", "are", "values"])
m.items_list