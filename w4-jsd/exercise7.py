"""
@title: excercise 7.
@author: Javier Sanz Diaz
@date: 2 Oct 2021

Create a program receiving by keyboard a number of seconds and converting it to its hours
equivalent (for example 3680 seconds are 1 hour, 1 minute and 20 seconds and will be printed like
01:01:20). Notice the leading zeros.
"""

sec = int(input('Seconds: '))

min = sec // 60 
secdef = sec % 60
houdef = min // 60
mindef = min % 60

print('%s:%s:%s'%(str(houdef).zfill(2), str(mindef).zfill(2), str(secdef).zfill(2)))

'''
To put the leading zeros we use the method '.zfill(number of digits you want)
and we convert the variables to str.

Correción:
No se pueden usar metodos :). Se puede hace con if's y añadiendo ceros delante.
O tmb con el %02d
'''


