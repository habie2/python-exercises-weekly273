# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:23:09 2019

@author: Hashim Mahmood
@author:  Modified by Angel Garcia Olaya. PLG-UC3M
@version: 1.0

Exercise 12. Create a program that receives as input a positive number,
 which will correspond to a quantity
of money, and calculates and prints the minimum number of notes and coins
for it. If the quantity of any coin or note is zero it must not be printed.
 Notes: 500, 200, 100, 50, 20, 10 and 5€
 Coins: 2, 1, 0.5, 0.20, 0.10, 0.05, 0.02 and 0.01€
Example, if 348.07 is introduced it should print:
200€: 1
100€: 1
20€: 2
5€: 1
2€: 1
1€: 1
0.05€: 1
0.02€: 1"""

mon = float(input("Enter the amount of money: "))
if mon < 0.01:
    print("Sorry this amount is too low to be printed")
if mon >= 500:
    n500 = mon//500
    mon = mon-n500*500
    print("500€: ", int(n500))
if mon >= 200:
    n200 = mon//200
    mon = mon-n200*200
    print("200€: ", int(n200))
if mon >= 100:
    n100 = mon//100
    mon = mon-n100*100
    print("100€: ", int(n100))
if mon >= 50:
    n50 = mon//50
    mon = mon-n50*50
    print("50€: ", int(n50))
if mon >= 20:
    n20 = mon//20
    mon = mon-n20*20
    print("20€: ", int(n20))
if mon >= 10:
    n10 = mon//10
    mon = mon-n10*10
    print("10€: ", int(n10))
if mon >= 5:
    n5 = mon//5
    mon = mon-n5*5
    print("5€: ", int(n5))
if mon >= 2:
    n2 = mon//2
    mon = mon-n2*2
    print("2€: ", int(n2))
if mon >= 1:
    n1 = mon//1
    mon = mon-n1*1
    print("1€: ", int(n1))

# With the decimal part we can have precision issues, so we will convert it
# to cents and round it
mon = round(mon * 100, 0)
if mon >= 50:
    n050 = mon//50
    mon = mon-n050*50
    print("0.50€: ", int(n050))
if mon >= 20:
    n020 = mon//20
    mon = mon-n020*20
    print("0.20€: ", int(n020))
if mon >= 10:
    n010 = mon//10
    mon = mon-n010*10
    print("0.10€: ", int(n010))
if mon >= 5:
    n05 = mon//5
    mon = mon-n05*5
    print("0.05€: ", int(n05))
if mon >= 2:
    n02 = mon//2
    mon = mon-n02*2
    print("0.02€: ", int(n02))
# If we have something here it will be 1 cent
if mon > 0:
    print("0.01€: ", 1)
