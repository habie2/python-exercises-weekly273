"""
@title: exercise1
@author: habi2
@date: 11/11/2021

Create three functions to: 
(a) ask the user for a positive number in the range (1, 10) 
(b) generate a random list of this number of elements and 
(c) to find the minimum of the list.
Create a program that uses them.
"""
import random 

def ask_user(answer = int(input('Enter a positive number in the range (1, 10): '))):
    return answer 
 
def random_list(length_list: int):
    lista_randoms = []
    for _ in range(length_list):
        lista_randoms.append(random.randint(1, 10))
    return lista_randoms

def minimum(lista: list):
    minimo = lista[0]
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo

print(minimum(random_list(ask_user())))
