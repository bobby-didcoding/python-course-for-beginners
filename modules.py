#Modules

'''
In Python we are able to write a long program and save as a module. This
is known as creating a script. We are able to import modules across modules
and into the Python interpreter. This negates the need to keep repeating
ourselves.
DRY!....Don't repeat yourself

Pythons standard library can be found here https://docs.python.org/3/library/
'''


from functions import demo_func

def func_1(arg:int):
    x = [y for y in range(2, 10, 2)]
    x.append(arg)
    print(x)

def func_2(number:int, power:int):
    print(pow(number,power))
