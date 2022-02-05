#Python functions

'''
Think of a function as a little named container for a group of your code!

To run the code in a function, you must call the function.

A function can be called from anywhere after the function is defined. 

example...
>>>def demo_func(param:int):
...    """This is just a demo
...    function.
...    """
...    calc = param + 4
...    return calc

>>>demo_func(6)
10

Functions can return a value using a return statement. Functions are 
a common feature among all programming languages

The keyword def introduces a function definition. It must be followed 
by the function name and the parenthesized list of formal parameters. 
The statements that form the body of the function start at the next line, 
and must be indented.

def demo_func(param:int):
    """This is just a demo
    function.
    """
    calc = param + 4
    return calc

There are 3 forms of function arguments
1) Position only arguments
2) Positional or keyword arguments
3) Keyword only arguments (named parameters)
'''

#basics
def demo_func(param:int):
    """This is just a demo
    function.
    """
    calc = param + 4
    return calc

demo_func(6)


#function arguments
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
'''
def combined_example(pos_only, /, standard, *, kwd_only):
                     --------     --------     ---------
                        |             |                 |
                        |        Positional or keyword  |
                        |                               |
                        -- Positional only              --Keyword only
'''
standard_arg(2)
pos_only_arg(2)
kwd_only_arg(arg=2)
combined_example(2, 2, kwd_only=2)
combined_example(2, standard=2, kwd_only=2)

'''
As guidance:

Use positional-only if you want the name of the parameters to not 
be available to the user. This is useful when parameter names have 
no real meaning, if you want to enforce the order of the arguments 
when the function is called or if you need to take some positional 
parameters and arbitrary keywords.

Use keyword-only when names have meaning and the function definition 
is more understandable by being explicit with names or you want to 
prevent users relying on the position of the argument being passed.

For an API, use positional-only to prevent breaking API changes if 
the parameter’s name is modified in the future.
'''

