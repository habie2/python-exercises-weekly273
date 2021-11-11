"""
@title: excercise 3.
@author: Javier Sanz Diaz
@date: 7 Oct 2021

Create a program to generate and print on screen the N perfect numbers smaller than the value
that the user introduces using the keyboard. A number is a perfect number when it is equal to
the addition of all its divisors except itself (You can rely on the flow diagram of the similar
exercise of a previous week). Example:
Introduce the top limit to generate perfect numbers and press Enter
10000
The number 6 is perfect
The number 28 is perfect
The number 496 is perfect
The number 8128 is perfect
"""
limit = int(input('Introduce the top limit to generate perfect numbers and press Enter \n'))
n = 1

while limit != n:
    divisor = n
    acum = 0
    while divisor >= 2:
        if n % divisor == 0:
            acum += (n/divisor)
        divisor -= 1
    if acum == n:
        print(f'{n} perfect number')
    n += 1