"""
@title: exercise3
@author: habi2
@date: 21/10/2021

Fill a 3x3 matrix with random numbers considering that the values cannot be repeated:
7 3 21
9 12 1
8 13 5
Put in order the previous matrix as in the example shown below without using max(), min(),
neither sort()
1 3 5
7 8 9
12 13 21
"""
import random

matrix = []
matrix_ordered =[]
n_rows = 3
n_columns = 3
nums_matrix = []
nums_matrix_counter = 0
nums_matrix_ordered = []
#Generamos una lista con los elementos aleatorios que no se repiten
for _ in range(n_rows * n_columns):             
    new_number = random.randint(0, 25)
    while new_number in nums_matrix:
        new_number = random.randint(0, 25)
    nums_matrix.append(new_number)

#Generamos la matriz con el orden aleatorio
for i in range(n_rows):
    matrix.append([])
    for _ in range(n_columns):
        matrix[i].append(nums_matrix[nums_matrix_counter])
        nums_matrix_counter += 1

#printeamos la matriz con orden random
for i in range(n_rows):
    for j in range(n_columns):
        print(matrix[i][j], end = ' ')
    print('')

#Sol1_ordenar: ordenamos los numeros de la matriz, lo vamos a hacer buscando 
# los minimos de la lista y borrandolos de la original para appendearlos en la
# ordenada
minimum = 25
counter = 0
while len(nums_matrix) !=  0:
    for i in range(len(nums_matrix)):
        if nums_matrix[i] < minimum:
            minimum = nums_matrix[i]
            num = i
    nums_matrix_ordered.append(minimum)
    del(nums_matrix[num])
    counter += 1
    minimum = 25

#Generar matriz ordenada
nums_matrix_counter = 0

for i in range(n_rows):
    matrix_ordered.append([])
    for _ in range(n_columns):
        matrix_ordered[i].append(nums_matrix_ordered[nums_matrix_counter])
        nums_matrix_counter += 1

#Printeamos la matriz ordenada
print('\nThe ordered matrix is:')
for i in range(n_rows):
    for j in range(n_columns):
        print(matrix_ordered[i][j], end = ' ')
    print('')

