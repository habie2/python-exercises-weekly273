"""
@title: excercise 2.
@author: Javier Sanz Diaz
@date: 14 Oct 2021

Create a list of any type, with length greater than 20. Initialize all its elements to random values.
Create a second list and make it equal to the first one (with a = b). Change the value of an element
of the first list. Print both lists. Does the corresponding element of the second list change? Why?
Create two additional lists and repeat the previous steps, but instead of = copy the elements of
the first into the second one by one. Can you see any difference?
"""
import random

a = []
for x in range(20):
    a.append(random.randrange(0, 100))
b = []
b = a
c = a.copy()
a[12] = 'hola'
print(a)
print(b)
print(c)

'''
Conclusion:
At first it prints the whole list even if we make changes in the list. However 
if we copy it, the modifications that we make later will not be taken into 
account.
'''