"""
@title: exercise7
@author: habi2
@date: 12/11/2021

The Fibonacci sequence is defined by the following formula:
if n = 0 f(n) = 0
if n = 1 f(n) = 1
if n > 1 f(n) = f(n - 1) + f(n - 2)
Define a function that prints the Fibonacci sequence from a given number. Example:
fibonacci(7)
Output: [0, 1, 1, 2, 3, 5, 8, 13]
"""

def fibbo(num:int):
    output_list = []
    for i in range(num + 1):
        if i == 0:
            output_list.append(0)
        elif i == 1:
            output_list.append(1)
        else:
            output_list.append(output_list[i-1]+output_list[i-2])
    return output_list

print(fibbo(100))