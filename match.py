#Python control flows - Match statement

'''
A match statement takes an expression and compares its value to 
successive patterns given as one or more case blocks.
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