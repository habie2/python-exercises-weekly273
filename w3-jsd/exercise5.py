
"""
@title: excercise 5. Float precision
@author: Javier Sanz Diaz
@date: 24 Sept 2021

Declare two float variables. Initialize the first variable with the value 12345678901234567.0 and the
second one with the value 12345678901234568.0. Print the subtraction of them on the screen. What is
the result? Repeat the same procedure with two int variables (remove the decimal). What is the result?
Why? Print the result of the following operation: 0.3 – 0.2, what happens?
"""

var1 = float(12345678901234567.0)
var2 = float(12345678901234568.0)

print('with decimals: ',var1 - var2)

var1 = int(12345678901234567)
var2 = int(12345678901234568)

print('with integrals: ', var1 - var2)

print('0.3 - 0.2 =', 0.3-0.2)

"""
Conclusion:
terminal print->with decimals:  0.0
                with integrals:  -1
                0.3 - 0.2 = 0.09999999999999998

In the first case we get zero because when dealing with float variables, Python
stops "counting" after 15-16 digits, so for the program 
12345678901234568.0 and 12345678901234567.0 are the same number.
    This does not happen with integers, we can store all the digits that memory
allows us (a lot), so we can see that the result of substraction between the 
numbers is -1. 
    And finally when operating 0.3 – 0.2, the 0.2 it is not exactly a 0.2 so we
get this sort of bug. 
"""