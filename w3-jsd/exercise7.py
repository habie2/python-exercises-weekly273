"""
@title: exercise7. Copy of variables.
@author: Javier Sanz Diaz
@date: 26/09/2021

Create two variables of any type, assign a value to the first one, and assign the first one to the second one. Print on the screen the second variable. Extend the program with a new instruction that changes the value of the first variable, and add another instruction to print again the second one. Does the second variable change its value? Why?
"""
var1 = 22
var2 = var1

print(var2)

var1 = 23

print(var2)
"""
Conclusion: 

No, the value remains the same because, as an interpreted lenguage, the computer "reads" line by line.
"""