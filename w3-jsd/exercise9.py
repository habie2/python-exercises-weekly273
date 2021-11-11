"""
@title: exercise9. String concatenation.
@author: Javier Sanz Diaz
@date: 27/09/2021

Declare three string variables. Assign any value to the first two variables and make the third one equal to the first one + second one. Print the third variable. What happens? What happens if you make third = first – second?
"""
var1 = str('hello')
var2 = str('terrarian')
var3 = str(var1 + var2)

print(var3)

var3 = str(var1 - var2)

print(var3)
"""
Conclusion: 

In the first case the result is 'helloterrarian', but in the second case we get a TypeError that says that the operand type '-' is unsuported for 'str' and 'str'.
"""