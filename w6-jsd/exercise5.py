"""
@title: excercise 5.
@author: Javier Sanz Diaz
@date: 17 Oct 2021

Write a program that guesses the number that the user has thought (1 to 100). The program will
generate random numbers and must control that none of them is repeated. It will also be able to
detect if the user is lying (if it has already tried all the numbers and the user says it is none of
them). It has also to count how many attempts were needed to guess the number.
"""
import random

#Generar la lista
list = []
for i in range(1, 101):
    list.append(i)
print(list)

num = random.randrange(1,101)
question = 1
num_tries = 0

while list != [] and question != 'yes':
    if num in list:
        question = input('Is %i the number you are thinking of? (yes/no)'%num)
        del(list[list.index(num)])
        num = random.randrange(1,101)
        num_tries += 1
    else:
        num = num = random.randrange(1,101)

if question == 'yes':
    print('It took %i tries'%num_tries)
else:
    print('We cought you, naughty naughty')
        
"""
Alternativesolution: 
Generar otra lista con falsos y cambiar a true el index si es igual 
y luego comprobar si es igual a false la otra lista

"""