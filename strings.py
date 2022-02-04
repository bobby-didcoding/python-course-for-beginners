#Using python to manipulate strings

'''
Python can be used to manipulate strings, which can 
be expressed in several ways.

They can be enclosed in single quotes ('...') 
or double quotes ("...")

'\' can be used to escape quotes

Python strings cannot be changed — they are immutable.

We will also look at the built in function called len()
This function returns the length of a string:
'''

#The basics
'spam eggs'  # single quotes
'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

#New line
'"Isn\'t," they said.'
print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output

print(s)  # with print(), \n produces a new line

#Raw string
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote


#String literals
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


#Concatenated
3 * 'un' + 'ium'
'Did' 'Coding'
text = ('Put several strings within parentheses '
        'to have them joined together.')
text
#This only works with two literals though, 
#not with variables or expressions:
prefix = 'Did'
prefix 'Coding'
prefix + 'Coding'

#Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   
-9  -8  -7  -6  -5  -4  -3  -2  -1
'''

word = 'Didcoding'
word[0]  # character in position 0
word[5]  # character in position 5
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)
word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end
word[:2] + word[2:]
word[:4] + word[4:]


#changing strings
word[0] = 'P'
'P' + word[1:]
word[:2] + 'di'

#Sting length
s = 'bobby-didcoding'
len(s)