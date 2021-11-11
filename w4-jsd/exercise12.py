"""
@title: excercise 12.
    @author: Javier Sanz Diaz
    @date: 3 Oct 2021

    Create a program that receives as input a positive number, which will correspond to a
    quantity of money, and calculates and prints the minimum number of notes and coins for it. If the quantity of
    any coin or note is zero it must not be printed.
        ● Notes: 500, 200, 100, 50, 20, 10 and 5€
        ● Coins: 2, 1, 0.5, 0.20, 0.10, 0.05, 0.02 and 0.01€
    Example, if 348.07 is introduced it should print:
    200€: 1
    100€: 1
    20€: 2
    5€: 1
    2€: 1
    1€: 1
    0.05€: 1
    0.02€: 1
"""
money = float(input('Enter the cuantity of money: '))

#notes
notes500 = money // 500
money -= 500 * notes500
notes200 = money // 200
money -= 200 * notes200
notes100 = money // 100
money -= 100 * notes100
notes50 = money // 50
money -= 50 * notes50
notes20 = money // 20
money -= 20 * notes20
notes10 = money // 10
money -= 10 * notes10
notes5 = money // 5
money -= 5 * notes5

#coins
coins2 = money // 2
money -= 2 * coins2
coins1 = money // 1
money -= 1 * coins1
coins0_5 = money // 0.5
money -= 0.5 * coins0_5
coins0_2 = money // 0.2
money -= 0.2 * coins0_2
coins0_1 = money // 0.1
money -= 0.1 * coins0_1
coins0_05 = money // 0.05
money -= 0.05 * coins0_05
coins0_02 = money // 0.02
money -= 0.02 * coins0_02
coins0_01 = money // 0.01
money -= 0.01 * coins0_01

#Notes
if notes500 != 0:
    print('500€: %i'%int(notes500))
if notes200 != 0:
    print('200€: %i'%int(notes200))
if notes100 != 0:
    print('100€: %i'%int(notes100))    
if notes50 != 0:
    print('50€: %i'%int(notes50))
if notes20 != 0:
    print('20€: %i'%int(notes20))
if notes10 != 0:
    print('10€: %i'%int(notes10))
if notes5 != 0:
    print('5€: %i'%int(notes5))

#Coins
if coins2 != 0:
    print('2€: %i'%coins2)
if coins1 != 0:
    print('1€: %i'%coins1)
if coins0_5 != 0:
    print('0.5€: %i'%coins0_5)
if coins0_2 != 0:
    print('0.2€: %i'%coins0_2)
if coins0_1 != 0:
    print('0.1€: %i'%coins0_1)
if coins0_05 != 0:
    print('0.05€: %i'%coins0_05)
if coins0_02 != 0:
    print('0.02€: %i'%coins0_02)
if coins0_01 != 0:
    print('0.01€: %i'%coins0_01)

'''
Doubt: Why it only fails on 0.01 and 0.02???

Solution: Multiply by 100 so that we do not loose the decimals on the float, or
rounding the money to 2.
'''