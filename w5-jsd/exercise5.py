"""
@title: exercise 5.
@author: Javier Sanz Diaz
@date: 7 Oct 2021

Define a program that allows simulating the behavior of an ATM. The program must meet the
following requirements
- Randomly create a 4-digits PIN number and the account balance, which must be in the range
50 to 5,000 Euros. Notice that the PIN must be stored as string, otherwise any leading zero it
may have will be lost.
- Request the corresponding PIN code to the user, giving up to three attempts to enter the
correct number. In case of failing three times the program will show a message on the screen
and finish.
- If the pin is correct it must show a menu with the different operations that the ATM allows, as
seen in the next example:
Welcome
------------------------
1- Deposit
2- Cash withdrawal
3- Exit
Choose the operation:
After each operation, indicate on the screen the available balance in the account. If the cash
withdrawal operation exceeds the amount available in the bank account, the operation will be
denied and the corresponding message will be displayed.
"""
import random

PIN = str(1234)
account_balance = random.randrange(50.00, 5000.00)
num_tries = 3

print('''
WWSY's Bank
-------------------------''')#WWSYM stands for: we will not steal you

while num_tries != 0:
    pin_try = str(input(f'PIN (left tries {num_tries}): '))
    
    if PIN == pin_try:
        print('''Welcome to WWSY's Bank
-------------------------
1- Deposit
2- Cash withdrawal
3- Exit
Choose the operation:''')
        op_decision = int(input())
        if op_decision == 1:
            print(f'''
Deposit
-------------------------
Actual balance: {account_balance} €
How many do you want to add?''')
            
            money_deposit = float(input())
            
            print(f'''
Succesfull operation  
-------------------------
Actual balance: {float(account_balance) + money_deposit} €
Thanks for trusting WWSY''')
        if op_decision == 2:
            print(f'''
Cash withdrawal
-------------------------
Actual balance: {account_balance} €
How many do you want?''')
            
            money_withdrawal = input()
            if int(money_withdrawal) > account_balance:
                print('Operation denied: not enough money')
            else:
                print(f'''
Succesfull operation  
-------------------------
Actual balance: {account_balance - int(money_withdrawal)} €
Thanks for trusting WWSY''')
        if op_decision == 3:
            print(f'''
Exit
-------------------------
Thanks for trusting WWSY''')
        break
    else:
        print('Wrong PIN entered')
        num_tries -= 1

if num_tries == 0:
    print('Fuiste baneao :(')
