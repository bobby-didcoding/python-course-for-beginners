#Using python as a calculator

'''
We can use the interpreter to take an input and return an output!

Arithmetic Opperators:
We have a whole bunch of opperators at our disposal
+ Addition
- Subtraction
* Multiplication
/ Division
// Floor division
% Modulus (remainder of x / y) | use divmod(a, b) 
** Exponentiation (power of) | can also use pow(x , y) instead of x**y

Assignment Opperators:
= Equals

Number Types:
int (2, 3, 458, 678)
float (2.2, 3.5, 5.666675678)

Build in Function:
round() Rounds a numbers with the specified number of 
decimals i.e. round(number, decimals) 


lastly, Python has a handy way of making big int's easier to read
4000000000 can be written as 
4_000_000_000
'''


#The basics
2 + 2 # simple addition
5 - 2 # simple subtraction
7 * 10 # simple multiplication

#Division and Modulus
10 / 4  # classic division returns a float
10 // 4  # floor division discards the fractional part
10 % 4 # the % operator returns the remainder of the division
divmod(10,4)

#Fancy sums
50 - 5*6 
(50 - 5*6) / 4
5 * 3 + 2  # floored quotient * divisor + remainder

#Exponentiation (power of)
5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7
pow(2,7)

#Using variables
width = 60
height = 3 * 7
width * height


#In interactive mode, the last printed expression is assigned to the variable _.
tax = 12.5 / 100
price = 100.50
price * tax #this is assigned to '_' and we use it in the next expression
price + _ #We reference '_' but this expression is now assigned to '_'
round(_, 2)
