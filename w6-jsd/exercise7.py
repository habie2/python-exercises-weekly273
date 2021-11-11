"""
@title: excercise 7.
@author: Javier Sanz Diaz
@date: 17 Oct 2021

Write a program that receives as input a positive number, which will correspond to a quantity of
money, and calculates and prints the minimum number of notes and coins for it, as in a previous
exercise Use a tuple to store the different types of notes and coins that exist.
"""
money = float(input("Enter the amount of money: "))
types_notes = ('500', '200', '100', '50', '20', '10', '5', '2', '1', '0.5', '0.20', '0.10', '0.05', '0.02', '0.01')
notes = []

#Solucion:
for note in types_notes:
    while money >= note:
        Money= money - note
        notes_500 += 1
    print('notes500:', notes_500)

#Seria algo asi 
"""
money = float(input("Enter the amount of money: "))
if money < 0.01:
    print("Sorry this amount is too low to be printed")
if money >= 500:
    n500 = money//500
    money = money-n500*500
    print(f'{notes[0]}: {int(n500)}')
if money >= 200:
    n200 = money//200
    money = money-n200*200
    print(f'{notes[1]}: {int(n200)}')
if money >= 100:
    n100 = money//100
    money = money-n100*100
    print(f'{notes[2]}: {int(n100)}')
if money >= 50:
    n50 = money//50
    money = money-n50*50
    print(f'{notes[3]}: {int(n50)}')
if money >= 20:
    n20 = money//20
    money = money-n20*20
    print(f'{notes[4]}: {int(n20)}')
if money >= 10:
    n10 = money//10
    money = money-n10*10
    print(f'{notes[5]}: {int(n10)}')
if money >= 5:
    n5 = money//5
    money = money-n5*5
    print(f'{notes[6]}: {int(n5)}')
if money >= 2:
    n2 = money//2
    money = money-n2*2
    print(f'{coins[0]}: {int(n2)}')
if money >= 1:
    n1 = money//1
    money = money-n1*1
    print(f'{coins[1]}: {int(n1)}')

# With the decimal part we can have precision issues, so we will convert it
# to cents and round it
money = round(money * 100, 0)
if money >= 50:
    n050 = money//50
    money = money-n050*50
    print(f'{coins[2]}: {int(n050)}')
if money >= 20:
    n020 = money//20
    money = money-n020*20
    print(f'{coins[3]}: {int(n020)}')
if money >= 10:
    n010 = money//10
    money = money-n010*10
    print(f'{coins[4]}: {int(n010)}')
if money >= 5:
    n05 = money//5
    money = money-n05*5
    print(f'{coins[5]}: {int(n05)}')
if money >= 2:
    n02 = money//2
    money = money-n02*2
    print(f'{coins[6]}: {int(n02)}')
# If we have something here it will be 1 cent
if money > 0:
    print("%t: "%coins[7], 1)
"""