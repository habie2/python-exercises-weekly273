"""
@title: excercise 4.
@author: Javier Sanz Diaz
@date: 7 Oct 2021

As you know, when we ask the user to enter a number in Python using input, we need to cast
the number to int or float to be able to work with it. But if the user enters something which
is not a number the program fails. A possible solution is to use the isdigit() function of
strings, which returns True if the string is a number (for example '3434'.isdigit() returns
True). This works for integer numbers but not for float, as the point is not recognized as a
number ('34.22'.isdigit() returns False). Create a program that asks the user to
enter a number and keeps asking until a number is introduced. At the end it prints the square of
the entered number. It must work both for integer and float numbers.
"""
still = 1

while still == 1:
    num = input('Enter a number: ')

    if num.isdigit() == True:
        print(int(num) ** 2)
        still = 0
    else:
        try:
            print(float(num) ** 2)
            still = 0
        except ValueError:
            print(f'{num} is not a number, try again:')