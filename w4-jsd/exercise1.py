"""
@title: excercise 1. Assignment operators
@author: Javier Sanz Diaz
@date: 2 Oct 2021

The only "real" assignment operator is the equal symbol (=), but Python has 
also some other assignment operators as the following example shows (copy it 
into a program and run it). How do these operators work?
"""

a = 4
a += 2          #a = a + 2
print(a)    
a -= 3          #a = a - 3
print(a)
a *= 3          #a = a * 3
print(a)
a /= 2          #a = a / 2
print(a)
a %= 4          #a = a % 4
print(a)
a == 0          #It compares the value of a (0.5) to 0, if we print this 
                #operator, we would get a false, but as we are printing a, we 
                #obtain 0.5
print(a)
a //= 2         #a = a // 2, the rounded result of a / 2.
print(a)