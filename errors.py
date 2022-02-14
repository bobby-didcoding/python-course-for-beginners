#Handling errors

'''
Python has (at least) two distinguishable kinds of errors: 
syntax errors and exceptions.

Syntax errors: Also known as parsing errors, are perhaps the 
most common kind of complaint you get while you are still learning Python.

Exceptions: Errors detected during execution are called exceptions and are not 
unconditionally fatal: you will soon learn how to handle them in Python programs.

Here are all of Pythons built-in exception
ArithmeticError Raised when an error occurs in numeric calculations
AssertionError Raised when an assert statement fails
AttributeError Raised when attribute reference or assignment fails
Exception Base class for all exceptions
EOFError Raised when the input() method hits an "end of file" condition (EOF)
FloatingPointError Raised when a floating point calculation fails
GeneratorExit Raised when a generator is closed (with the close() method)
ImportError Raised when an imported module does not exist
IndentationError Raised when indentation is not correct
IndexError Raised when an index of a sequence does not exist
KeyError Raised when a key does not exist in a dictionary
KeyboardInterrupt Raised when the user presses Ctrl+c, Ctrl+z or Delete
LookupError Raised when errors raised cant be found
MemoryError Raised when a program runs out of memory
NameError Raised when a variable does not exist
NotImplementedError Raised when an abstract method requires an inherited class to override the method
OSError Raised when a system related operation causes an error
OverflowError Raised when the result of a numeric calculation is too large
ReferenceError Raised when a weak reference object does not exist
RuntimeError Raised when an error occurs that do not belong to any specific expections
StopIteration Raised when the next() method of an iterator has no further values
SyntaxError Raised when a syntax error occurs
TabError Raised when indentation consists of tabs or spaces
SystemError Raised when a system error occurs
SystemExit Raised when the sys.exit() function is called
TypeError Raised when two different types are combined
UnboundLocalError Raised when a local variable is referenced before assignment
UnicodeError Raised when a unicode problem occurs
UnicodeEncodeError Raised when a unicode encoding problem occurs
UnicodeDecodeError Raised when a unicode decoding problem occurs
UnicodeTranslateError Raised when a unicode translation problem occurs
ValueError Raised when there is a wrong value in a specified data type
ZeroDivisionError Raised when the second operator in a division is zero
'''
#Basic examples
10 * (1/0)
4 + spam*3
'2' + 2

#Handling exceptions

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    #Add multiple exceptions in a tuple (RuntimeError, TypeError, NameError)
    except (RuntimeError, TypeError, NameError, ValueError): 
        print("Oops!  That was no valid number.  Try again...")


def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


'''
The try/except statement has an optional else clause, which, when present, 
must follow all except clauses. It is useful for code that must be executed 
if the try clause does not raise an exception.

If a finally clause is present, the finally clause will execute as the last
task before the try statement completes. The finally clause runs whether or 
not the try statement produces an exception. The following points discuss 
more complex cases when an exception occurs.
'''
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except TypeError:
        print("Must be int!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")