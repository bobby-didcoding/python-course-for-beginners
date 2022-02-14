#Python control flows - Loop clauses

'''
Python has a few statements and clauses that we can use in loops. 
These are:
break
continue
else 
pass

Loop statements may have an else clause; it is executed when the 
loop terminates through exhaustion of the iterable (with for) or 
when the condition becomes false (with while), but not when the 
loop is terminated by a break statement. 
'''

#Break statement
for n in range(2, 10): #equivalent of...for n in [2,3,4,5,6,7,8,9]:
    for x in range(2, n): #first loop is for x in range(2, 2):
        if n % x == 0: 
            print(n, 'equals', x, '*', n//x)
            break
    #the else runs when no break clause occurs
    else:
        print(n, 'is a prime number')


#Continue statement
for num in range(2, 10): #equivalent of...for n in [2,3,4,5,6,7,8,9]:
    if num % 2 == 0:
        print("Found an even number", num)
        continue #Will continue with the next loop
    print("Found an odd number", num)


#Pass statement
class MyPassClass:
    pass


def my_pass_def(*args):
    pass #Needs looking at