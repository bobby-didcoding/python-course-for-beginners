#Python control flows - Match statement

'''
Hot off the press in Python 3.10

Structural pattern matching has been added in the form of a match 
statement and case statements of patterns with associated actions. 
Patterns consist of sequences, mappings, primitive data types as 
well as class instances. Pattern matching enables programs to extract 
information from complex data types, branch on the structure of data, 
and apply specific actions based on different forms of data.

A match statement takes an expression and compares its value to 
successive patterns given as one or more case blocks.

Note: We have a class in this demo. Don't get too caught up in how it
works! We have a class video in this course :)
'''

#basics
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

def http_error(status):
    match status:
        case 400 | 401 | 403 | 404:
            return "Not allowed"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


#Patterns can look like unpacking assignments, and can be used to bind variables:
# point is an (x, y) tuple
def http_error(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

point_tuple = (0,0)
point_tuple = (0,123)
point_tuple = (123,0)
point_tuple = (123,456)



#Match class
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(Point(0, 0))
where_is(Point(0, 10))
where_is(Point(10, 0))
where_is(Point(10, 10))