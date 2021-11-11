"""
@title: excercise 2. Operator precedence
@author: Javier Sanz Diaz
@date: 2 Oct 2021

Type the code below. What is the result of the program? Why?
"""

a, b, c, d = 5, 3, 20, 20
c -= (a + 1) / b - 3 + a % b
d -= (a + 1) / (b + 3 - 4 * a) % b
print("c:", c)
print("d:", d)

"""
Conclusion: 

The difference is that in the first case, the program does 'a % b' before 
doing the sum and the substraction. In the second case all the operations in 
the parenthesis are done before the 'x % b', being x the result of the 
parenthesis.
"""