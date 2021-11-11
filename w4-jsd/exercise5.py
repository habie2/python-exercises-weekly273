"""
@title: excercise 5.
@author: Javier Sanz Diaz
@date: 2 Oct 2021

Write a program that reads two names and two ages on the keyboard and prints who is
older. Example: if we introduce Pepe 23 and Luisa 18, it must print Pepe is older than Luisa. If
they are the same age it must print Pepe and Luisa are the same age
"""

name1, age1 = input('Name 1: '), int(input ('Age 1: '))
name2, age2 = input('Name 2: '), int(input ('Age 2: '))

if age1 > age2:
    print('%s is older than %s'%(name1, name2))
elif age1 == age2:
    print('%s and %s are the same age'%(name1, name2))
else:
    print('%s is older than %s'%(name2, name1))
