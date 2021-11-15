"""
@title: exercise6
@author: habi2
@date: 12/11/2021

Implement again the functions of the former exercise that modify the list (append, insert, etc.)
but in this case modifications must be done to the original list.
"""

general_list = [3, 45, 25, 12, 43, 21, 12, 12, 26, 4, 38, 6, 39, 33, 28]
    
def own_count(lista: list, num: int):
    count = 0
    for i in range(len(lista)):
        if lista[i] == num:
            count += 1
    return count

def own_index(lista: list, num: int):
    count = 0
    while count < len(lista):
        if lista[count] == num:
            return count
        else:
            count += 1
    return None

def own_append(lista: list, num: int):
    lista += [num]
    return lista
 
def own_insert(lista: list, num: int, num_index: int):
    lista = lista[:num_index] + [num] + lista[num_index:]
    return lista

def own_remove(lista: list, num: int):
    count = 0
    while count < len(lista):
        if lista[count] == num:
            lista = lista[:count] + lista[count + 1:]
            return lista
        else:
            count += 1
    return lista

def own_removeAll(lista: list, num: int):
    count = 0
    while count < len(lista):
        if lista[count] == num:
            lista = lista[:count] + lista[count + 1:]
            count -= 1
        count += 1
    return lista

def own_clear(lista:list):
    lista = None
    return lista

def own_pop(lista: list):
    value = lista[-1]
    lista = lista[:-1]
    return value

print(general_list, end='\n\n')

print('count:', own_count(general_list, 43))

print('index:', own_index(general_list, 12))

print('append:', own_append(general_list, 1))
general_list = own_append(general_list, 1)

print('insert:', own_insert(general_list, 9, 7))
general_list = own_insert(general_list, 9, 7)

print('remove:', own_remove(general_list, 12))
general_list = own_remove(general_list, 12)

print('removeAll:', own_removeAll(general_list, 12))
general_list = own_removeAll(general_list, 12)

print('pop:', own_pop(general_list))
general_list = own_pop(general_list)

print('clear:', own_clear(general_list))
general_list = own_clear(general_list)