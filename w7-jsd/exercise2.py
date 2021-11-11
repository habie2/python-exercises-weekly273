"""
@title: exercise2
@author: habi2
@date: 21/10/2021

Create a program to generate two matrixes (as lists of lists) of integers M1 and M2, which can
be of different size, by requesting the sizes and the values by keyboard. Then it should show the
elements of M1 that are included on M2.
Specify the number of rows of the M1 matrix and press Enter: 2
Specify the number of columns of the M1 matrix and press Enter: 3
Introduce the term in the 0, 0 position and press Enter: 1
Introduce the term in the 0, 1 position and press Enter: 3
Introduce the term in the 0, 2 position and press Enter: 5
Introduce the term in the 1, 0 position and press Enter: 7
Introduce the term in the 1, 1 position and press Enter: 9
Introduce the term in the 1, 2 position and press Enter: 11
The M1 matrix is:
1 3 5
7 9 11
Specify the number of rows of the M2 matrix and press Enter: 3
Specify the number of columns of the M2 matrix and press Enter: 2
Introduce the term in the 0, 0 position and press Enter: 1
Introduce the term in the 0, 1 position and press Enter: 2
Introduce the term in the 0, 2 position and press Enter: 3
Introduce the term in the 1, 0 position and press Enter: 4
Introduce the term in the 1, 1 position and press Enter: 5
Introduce the term in the 1, 2 position and press Enter: 6
The M2 matrix is:
1 2
3 4
5 6
The term 1 is included in both matrixes
The term 3 is included in both matrixes
The term 5 is included in both matrixes
"""
#For m1
m1 = []
rows_m1 = int(input('Specify the number of rows of the M1 matrix and press Enter: '))
columns_m1 = int(input('Specify the number of colums of the M1 matrix and press Enter: '))

for i in range(rows_m1):
    m1.append([])
    for j in range(columns_m1):
        m1[i].append(int(input(f'Introduce the term in the {i}, {j}  position and press Enter: ')))

#Para hacer la matrix tenemos que estar fuera del for, porque la queremos imprimir despues no a trozos :):
print('The matrix M1 is:')
for i in range(rows_m1):
    for j in range(columns_m1):
        print(m1[i][j], end = ' ')
    print('')

#For m2
m2 = []
rows_m2 = int(input('Specify the number of rows of the M1 matrix and press Enter: '))
columns_m2 = int(input('Specify the number of colums of the M1 matrix and press Enter: '))

for i in range(rows_m2):
    m2.append([])
    for j in range(columns_m2):
        m2[i].append(int(input(f'Introduce the term in the {i}, {j}  position and press Enter: ')))

#Para hacer la matrix tenemos que estar fuera del for, porque la queremos imprimir despues no a trozos :):
print('The matrix M2 is:')
for i in range(rows_m2):
    for j in range(columns_m2):
        print(m2[i][j], end = ' ')
    print('')
for i in range(rows_m2):
    for j in range(rows_m1):
        for k in range(columns_m1):
            if m1[j][k] in m2[i]:
                print(f'The term {m1[j][k]} is included in both matrixes')
