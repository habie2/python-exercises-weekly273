"""
@title: excercise 6.
@author: Javier Sanz Diaz
@date: 2 Oct 2021

Write a program that prints on the screen the price of a cinema ticket according to the age of
the customer. The program must read the user’s age and calculate the price as follows: (a) Normal ticket: 9
Euros; (b) Children under 5: 60% discount; (c) People over 60: 55% discount; (d) Young people under 26: 20%
discount.
"""

age = int(input('Please enter your age: '))
price = 9
if age <= 5:
    price *= 0.4
elif age <= 26:
    price *= 0.8
elif age >= 60:
    price *= 0.45

print(price)