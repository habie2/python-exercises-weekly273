"""
@title: exercise8. Division by zero.
@author: Javier Sanz Diaz
@date: 27/09/2021

Declare three int variables. Assign 5 to the first one and 0 to the second one. Assign to the third variable the result of dividing the first variable by the second one. Print the result on the screen. Is there any error? Why? Does the result change if the variables are declared as float?

"""
"""
var1 = int(5)
var2 = int(0)
var3 = int(var1 / var2)

print(var3)

"""
var1 = float(5)
var2 = float(0)
var3 = float(var1 / var2)

print(var3)
"""
Conclusion: 

In both cases the code gives a ZeroDivisionError, because is not able to divide by zero. 
"""