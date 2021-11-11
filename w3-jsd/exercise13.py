"""
@title: exercise13. Out of range operations.
@author: Javier Sanz Diaz
@date: 26/09/2021

Create a float variable with a value out of range by multiplying to big numbers. What is the result? Now generate the out of range number by using power operator (**). What is the result?
"""
n1 = float(123456789123456789123456789123456789)
n2 = float(123456789123456789123456789123456789)

var = float(n1 * n2)

print(var)

var = float(n1 ** n2)

print(var)
"""
Conclusion: 
In the first case we get a number that is multiplied by ten powered to x number. In the second case, we get an OverflowError that says, 'numeric result out of range'.

"""