"""
@title: excercise 1.
@author: Javier Sanz Diaz
@date: 7 Oct 2021

Ask the user two integer numbers A and B such as A + 5 < B. Keep asking until the former
condition is met. Then randomly generate and print 5 integer numbers in the interval [A,B] such
as they are even and odd in an alternative way. It does not matter if the values are repeated;
the aim is alternatively printing odd and even numbers.
Example: for the interval [3,9] a valid sequence of numbers is: 6, 7, 6, 3, 4
"""
import random

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

while (num1 + 5 < num2) == False:
    num1 = int(input('\nEnter first number: '))
    num2 = int(input('Enter second number: '))
print(f'for the interval [{num1},{num2}] a valid sequence of numbers is:',
f'{random.randrange(num1, num2, 1)}, {random.randrange(num1, num2, 2)},',
f'{random.randrange(num1, num2, 1)}, {random.randrange(num1, num2, 2)}, '
f'{random.randrange(num1, num2, 1)}')