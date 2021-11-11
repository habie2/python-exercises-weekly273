"""
@title: exercise4
@author: habi2
@date: 09/11/2021

Create a function to convert currencies in an exchange office. It will have a local constant
containing a nested tuple with the exchange rates for the desired currencies (euro, yen, dollar
and sterling pound). It will receive the original currency, the target currency and the quantity to
change and will return the quantity of money in the target currency.
"""

def exchange_office(curr1, curr2, quantity):
    currecies =  ('euro', (1), '€',  'yen', (131), '¥', 'dollar', (1.16), '$', 'pound', (0.85), '£') #we are going to pass it to euros
    current_cuurency_exchange = currecies.index(curr1) + 1
    target_cuurency_exchange = currecies.index(curr2) + 1

    target_quant = quantity * 1/currecies[current_cuurency_exchange] * currecies[target_cuurency_exchange]
    str_target_quant = str(round(target_quant, 2)) + ' ' + currecies[target_cuurency_exchange + 1]

    return str_target_quant

print(exchange_office('yen', 'pound', 45))