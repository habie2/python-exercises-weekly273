"""
@title: exercise6
@author: habi2
@date: 09/11/2021

Write a function that determines how many days there are in a particular month. The function
will receive two parameters: the month, as an integer between 1 and 12, and the year as a fourdigit integer. Consider the existence of leap years. Create a main program that reads a month
and a year from the keyboard and displays the number of days in that month on the screen.
"""

def month_counter(month = int(input('Introduce the number of the month: ')), year = int(input('Inntroduce the number of the year: '))):
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0:
        days_per_month[1] = 29
    return  days_per_month[month - 1]

print(month_counter())