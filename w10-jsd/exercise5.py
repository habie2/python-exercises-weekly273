"""
@title: exercise5
@author: habi2
@date: 12/11/2021

Create a program that creates functions which are your own versions of the list methods. Do not
make use of any built-in list methods to implement them. Your program must do all the
necessary checks to make sure that all the functions work. For functions modifying the original
list, the list must no be changed, but a modified version of it must be returned.

count(list1, x): returns the number of elements with the specified value.
index(list1, x): returns the index of the first element with the specified value. If the value
does not exist, the function returns None.
append(list1, x): adds an element at the end of the list.
insert(list1, x, index): adds an element at the specified position.
remove(list1, x): removes the first element in the list with the specified value.
removeAll(list1, x): removes all the elements in the list with the specified value.
clear(list1): removes all the elements from the list.
pop(list1): removes the last element of the list and returns its value.
"""
import random

general_list = [3, 45, 25, 12, 43, 21, 12, 12, 26, 4, 38, 6, 39, 33, 28]

def own_count():
    