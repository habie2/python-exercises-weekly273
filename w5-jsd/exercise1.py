"""
@title: excercise 1.
@author: Javier Sanz Diaz
@date: 7 Oct 2021

Create a program that generates a random number between 1 and 20, do not show this number
on the screen and keep it hidden. Then try to find out its value. As you enter values the program
must indicate if the number entered is greater or less than the one that the program has
generated and also the number of tries.
"""
import random

a = random.randrange(1, 20)
num_tries =  0
num_input = int(input('Enter a number: '))

while num_input != a:
    if num_input < a:
        print('The number entered is less than the random one')
    else:
        print('The number is greater than the random one')
    num_tries += 1
    print(f'Number of tries {num_tries}')
    num_input = int(input('\nEnter a number: '))

print(f'Congratulations, the number was {a}')