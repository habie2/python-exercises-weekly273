"""
@title: excercise 8.
@author: Javier Sanz Diaz
@date: 2 Oct 2021

Write a program that reads a single character on the keyboard and prints on the screen if
"It is a number" or "It is not a number".
"""
entrada = input('Enter a character: ')
print(type(entrada))

if str(type(entrada)) == """<class 'float'>""" or """<class 'int'>""":
    print('It is a number')
else:
    print('It is not a number')
"""
solution: if character in '0123456789'


Options:
.isnumeric() method

Doesn't work :/
"""