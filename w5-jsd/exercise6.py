"""
@title: exercise 6.
@author: Javier Sanz Diaz
@date: 7 Oct 2021

Define a program which requests the mark of the exam for each student in a class and
calculates the highest mark, the lowest, the average and the number of students attending the
exam. The data input must finish when a negative number is introduced.
"""
list = []
a = float(input('Enter your mark:'))
max_num = 0
min_num = 10
acum_sum = 0

while a >= 0.0:
    list.append(float(input('Enter your mark:')))
    a = float(input('Enter your mark:'))

#Obteining the max number
for x in range(len(list)):
    if list[x] > max_num:
        max_num = list[x]
    if list[x] < min_num:
        min_num = list[x]
    acum_sum += list[x]


print(f'''
Min mark: {min_num}

Max mark: {max_num}

Average mark: {acum_sum / len(list)}
''')