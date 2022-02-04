#Python control flows - If statement

'''
Python uses the usual flow control statements known 
from other languages, with some twists.
Perhaps the most well-known statement type is the 
if statement.


Think of an if statement as a way to check to see if
conditions are met!

If a condition is met, do something...
else do something different!

'elif' stands for 'else if'

both elif and else are optional!

Note: I will be defining a function to demo :)
'''

#The basics
def number_play(x):
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

number_play(-1)
number_play(0)
number_play(1)
number_play(2)
