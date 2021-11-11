"""
@title: excercise 6.
@author: Javier Sanz Diaz
@date: 17 Oct 2021

Write a program that creates a tuple with the names of the months of the year. Then, the program
will ask the user for a number. If the number is between 1 and the maximum length of the tuple,
it will show the corresponding month of the year. Otherwise, it will show an error message and
will ask for another number. The program will run until the user enters a 0.
"""
months_tuple = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
months_num = int(input(f'Enter a number between 1 and {len(months_tuple)}: '))

while months_num != 0:
    while months_num > 12 or months_num < 1:
        months_num = int(input(f'ERROR: Enter a number between 1 and {len(months_tuple)}: '))
    print(f'{months_tuple[months_num - 1]} is number {months_num}')
    months_num = 0