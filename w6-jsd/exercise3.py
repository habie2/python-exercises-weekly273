"""
@title: excercise 3.
@author: Javier Sanz Diaz
@date: 14 Oct 2021

Write a program that:
a) Asks the user to enter the length of the float list to create. It must check that the number is
greater than 0, if not, it will continue asking for the length.
b) Fills it randomly with numbers between 1 and 49.
c) Creates a variable called total, it will store the addition of the integer part of all the elements
of the list.
d) Prints the list and the value of total.
"""
import random

length_list = int(input('Enter the lenght of the list: '))
a = []
total = 0

while length_list < 0:
    length_list = int(input('Enter the lenght of the list: '))

for _ in range(length_list):
    randnum = random.randrange(1, 49)
    a.append(randnum)
    total += randnum

print(a)
print('Sum: %i'%total)
