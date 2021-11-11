"""
@title: excercise 13.
@author: Javier Sanz Diaz
@date: 3 Oct 2021

Create a program to simulate a calculator. It must ask for two numbers and the operator (+
- * / // **) and show the result. If the operator is not a valid one, it must print the wrong operator
and finish.
"""
num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
operator = input('Enter the operator (+, -, *, /, //, **):')

if operator == ('+' or  '-' or '*' or '/' or '//' or '**'):
    if operator == '+':
        print(f'Result: {num1 + num2}')
    elif operator == '-':
        print(f'Result: {num1 - num2}')    
    elif operator == '*':
        print(f'Result: {num1 * num2}')
    elif operator == '/':
        print(f'Result: {num1 / num2}')
    elif operator == '//':
        print(f'Result: {num1 // num2}')
    elif operator == '**':
        print(f'Result: {num1 ** num2}')
else:
    print('wrong operator entered')

'''
Doubt: Why if I put a random str (ex: 's') the program goes down the if 
path?
Resuelto: Hay que poner paretesis:

if operator == ('+' or  '-' or '*' or '/' or '//' or '**'):

or:

if (operator == '+' or  operator == '-' or operator == '*' or 
operator == '/' or operator == '//' or operator == '**'):
'''