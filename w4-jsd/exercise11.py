"""
@title: excercise 11.
@author: Javier Sanz Diaz
@date: 3 Oct 2021

A year is leap-year if it is a multiple of 4, except if it is a multiple of 100. In this last case it will
be leap-year only if it is also a multiple of 400. For example the year 1900 was not a leap-year, but the year
2000 was. Create a program that reads a number by keyboard and calculates if it is a leap year. (Note: you
can use the flow diagram of week 2). Example of outputs (notice the use of past or future tense):
1901 was not a leap year
2016 was a leap year
2400 will be a leap year
2401 will be not a leap year
"""

actual_year =  int(input('what is the actual year? '))
year = int(input('Year: '))

if year < actual_year:
    tense = 'was'
if year > actual_year:
    tense = 'will be'        

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} {tense} a leap year')
        else:
            print(f'{year} {tense} not a leap year')
    else:
        print(f'{year} {tense} a leap year')
else:
    print(f'{year} {tense} not a leap year')
