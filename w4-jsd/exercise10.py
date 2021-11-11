"""
@title: excercise 10.
@author: Javier Sanz Diaz
@date: 3 Oct 2021

Create a program that calculates and shows the final salary of a worker depending on the
base salary and seniority according to the following rules:
    a. Ask the user about the base salary. If the base salary is bigger or equal than 1000 just show it as
    the final salary.
    b. If the base salary is less than 1000, ask the user about the seniority (only ask about it in this
    case!)
        ● If seniority is at least 10 years, the salary will be increased by 20%.
        ● If seniority is less than 10 years, the salary will be increased by 5%.
"""

base_salary =  float(input('What is your base salary? '))

if base_salary >= 1000:
    print('Final salary of the worker is: \n%i Euros'%base_salary)
else:
    seniority = float(input('How many years have you been working? '))
    if seniority >= 10:
        base_salary *= 1.2
        print('Final salary of the worker is: \n%f Euros'%base_salary)
    else:
        base_salary *= 1.05
        print('Final salary of the worker is: \n%f Euros'%base_salary) 