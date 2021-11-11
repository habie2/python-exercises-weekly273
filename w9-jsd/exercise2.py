"""
@title: exercise2
@author: habi2
@date: 08/11/2021

Create a program with the following functions:
a. createListNumbers: Creates a list of 10 random elements all even numbers and returns
it.
b. calculateFigures: receives a list as parameter and calculates the maximum, minimum
and average values of the list. It returns the calculated values.
"""
import random 

def createListNumbers():
    lista = []
    while len(lista) != 10:
        num = random.randint(1, 100)
        if num % 2 == 0:
            lista.append(num)
    return lista
def calculateFigures(lista_parameter = []):
    num_max, num_min, average = 0, 50, 0 
    for i in range(len(lista_parameter)):
        if lista_parameter[i] > num_max:
            num_max = lista_parameter[i]
        if lista_parameter[i] < num_min:
            num_min = lista_parameter[i]
        average += lista_parameter[i]
    average /= len(lista_parameter)

    return num_max, num_min, average

print(createListNumbers(), calculateFigures([26, 47, 44, 40, 17, 5, 40, 43]))

