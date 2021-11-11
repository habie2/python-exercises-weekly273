"""
@title: excercise 11.
@author: Javier Sanz Diaz
@date: 19 Oct 2021

Create a list of 100 integer numbers in the range 1 to 1000 and print it. Next remove from it all
the even (par) numbers and print it again.
"""
import random
lista = []
n = 0

for _ in range(100):
    lista.append(random.randrange(1, 1001))
print(lista)
      
for _ in range(100):
    if lista[n] % 2 == 0:
        del(lista[n])#lista.pop(n) #Mejor usar del() en vez de pop()
    else:
        n += 1

print(lista)