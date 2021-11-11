"""
@title: excercise 4.
@author: Javier Sanz Diaz
@date: 2 Oct 2021

Write a program that reads two integer numbers on the keyboard and shows the 
result of dividing the first by the second. If the second is zero, instead of 
performing the division it will print "Cannot divide by zero".
"""

num1 = int(input('Number 1:'))
num2 = int(input('Number 2:'))

if num2 == 0:
    print('Cannot divide by zero')
else:
    print(num1 / num2)