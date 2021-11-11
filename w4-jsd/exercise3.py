"""
@title: excercise 3. Relational operators
@author: Javier Sanz Diaz
@date: 2 Oct 2021

Type the code below. What is the result of the program? Why?
"""

a = 3
b = 8
c = 3.0
s = a != 0          # It prints if a is different than 0, true
r = a == 0          # It prints if a is equal to 0, false 
t = a <= b          # It prints if a is minor or equal to b, true    
u = b >= a          # It prints if b is major or equal to a, true    
v = b > a           # It prints if b is major than a, true    
w = b < a           # It prints if a is minor than b, false    
x = c == 3.0        # It prints if c is equal to 3.00, true
print("r:", r)
print("s:", s)
print("t:", t)
print("u:", u)
print("v:", v)
print("w:", w)
print("x:", x)

"""
Result: 

r: False
s: True 
t: True 
u: True 
v: True 
w: False
x: True
"""