"""
@title: exercise3
@author: habi2
@date: 08/11/2021

Create a function that generates a random number between a minimum and a maximum. It will
have a third parameter to state if it must return an integer, float or complex number.
"""
import random

def new_fun(num_min, num_max, num_type):
    '''num_type parameter description:
    depending on the number introduced:
    1 -> integer
    2 -> float
    3 -> complex    
    '''
    num = random.randint(num_min, num_max)
    if num_type == 1:
        return int(num)
    elif num_type == 2:
        return float(num)
    elif num_type == 3:
        return complex(num)

print(new_fun(47, 220, 1))
print(new_fun(47, 220, 2))
print(new_fun(47, 220, 3))