"""
@title: exercise4
@auhor: habi2
@date: 22/10/2021

A wood workshop sells wood boards of 10 different sizes, which they call size 0, size 1, etc.
Create a program that:
a. Generates 10 random numbers, between 0 and 10. Each one will represent the stock for
each available board size. It must print the number of boards of each size in the warehouse.
b. Asks the user about the number of customers that will buy boards. It will keep asking while it
is smaller than 1.
c. Automatically generates an order for each of the customers. Each order will contain for each
available size a random number of boards between 0 and 4.
d. Prints the orders into the screen.
e. Sells boards to the customers, starting by the first one, reducing the number of boards in the
stock.
f. Prints the pending orders for each customer (only if he/she has pending orders). A pending
order is the number of boards of each size that cannot be sold as there are not enough
boards in stock.
Example:
Stock: size0 size1 size2 size3 size4 size5 size6 size7 size8 size9
1 6 4 5 5 8 1 8 7 2
Enter the number of customers, please
3
Original orders
Customer 0: 3 3 1 0 3 0 2 3 3 3
Customer 1: 0 3 3 1 1 0 0 1 3 0
Customer 2: 2 3 0 1 0 2 0 0 0 3
Pending orders
Customer 0: 2 0 0 0 0 0 1 0 0 1
Customer 2: 2 3 0 0 0 0 0 0 0 3
"""
import random

matrix_stock = [['size0', 'size1', 'size2', 'size3', 'size4', 'size5', 'size6',
'size7', 'size8', 'size9',], []]

for _ in range(10):         #Nº elementos
    matrix_stock[1].append(random.randrange(1, 10))

print('Stock:')
for i in range(2):          #Nº filas           
    for j in range(10):     #Nº columnas
        if i == 0:          #Condicion para que los numeros cuadren
            a = '  '
        else:
            a = '      '
        print(matrix_stock[i][j], end = a)    
    print('')
    
q_costumers = int(input('Enter the number of customers, please' + '\n'))
while q_costumers < 1:
    q_costumers = int(input('Enter the number of customers, please' + '\n'))

matrix_og = []

print('\nOriginal orders:')
for i in range(q_costumers):    #Nº filas
    matrix_og.append([f'Costumer {i}: '])
    for j in range(10):      #Nº columnas
        matrix_og[i].append(random.randrange(0,5))

#Imprimir original orders
for i in range(q_costumers):
    for j in range(11):          #Nº columnas(10 tipos de madera) + la del costumer = 11
        if j == 0:
            print(matrix_og[i][j])
        else:
            print(matrix_og[i][j], end='      ')
    print('')

matrix_pen = []

#Generar pending orders
print('\nPending orders:')
for i in range(q_costumers):    #Nº filas
    matrix_pen.append([f'Costumer {i}: '])
    for j in range(10):      #Nº columnas
        if int(matrix_stock[1][j]) - int(matrix_og[i][j+1]) >= 0:       #Si es positivo o cero lo que queda
            matrix_pen[i].append(0)
            matrix_stock[1][j] = int(matrix_stock[1][j]) - int(matrix_og[i][j+1])
        else:       #Si no hay suficiente stock
            matrix_pen[i].append(-(int(matrix_stock[1][j]) - int(matrix_og[i][j+1])))
            matrix_stock[1][j] = 0



for i in range(q_costumers):
    if matrix_pen[i] != [f'Costumer {i}: ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
        for j in range(11):          #Nº columnas(10 tipos de madera) + la del costumer = 11
            if j == 0:
                print(matrix_pen[i][j])
            else:
                print(matrix_pen[i][j], end='      ')
                '''
                if matrix_pen[i][j] > 0:
                    print(matrix_pen[i][j], end='      ')
                else:
                    print(0, end='      ')'''
    print('')