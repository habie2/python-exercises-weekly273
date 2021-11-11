"""
@title: excercise 4.
@author: Javier Sanz Diaz
@date: 14 Oct 2021

Write a program to create a 20 elements int list and filling it randomly with numbers in the range
1 to 9. Ask the user for a number between 1 and 9 (the program must check that the number is
in the desired range) and print if the number is in the list and all the positions where it appears
"""
import random
list = []

for _ in range(20):
    list.append(random.randrange(1, 10))

print(list)

#Input del numero a buscar
searched_num = int(input('Enter a value between 1 and 9: '))
while searched_num < 1 or 9 < searched_num:
    searched_num = int(input('Enter a value between 1 and 9: '))

#Printeada de posicion
for i in range(20):
    if searched_num == list[0]:
        print('%s is in position %s'%(searched_num, i + 1))
    del(list[0])
