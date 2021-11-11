"""
@title: exercise1
@author: habi2
@date: 21/10/2021

Create a NxN matrix (represented as list of lists) where the first N - 1 columns have random
numbers in the range 1 to 10 and the last column contains the result of adding the numbers in
previous columns. Show the matrix as follows:
10 + 9 + 3 = 22
4 + 8 + 7 = 19
1 + 9 + 7 = 17
2 + 8 + 8 = 18
"""
import random

size_n = int(input('Enter the order of the matrix: '))
matrix = []
rows = size_n
columns = size_n - 1

#Creamos las listas dentro de la lista que van a ser las diferentes filas de 
#la matriz.
for _ in range(rows):
    matrix.append([])

for i in range(columns):
    for j in range(rows):
        n = random.randint(1, 10)
        matrix[j].append(n)
for i in range(rows):
    matrix[i].append(sum(matrix[i]))

for i in range(rows):
    for j in range(columns + 1):
        if matrix[i][j] == matrix[i][-1]:
            print('\b\b= ', matrix[i][-1])
        else:
            print(matrix[i][j], ' + ', end = '')
