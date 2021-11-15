"""
@title: exercise5
@author: habi2
@date: 12/11/2021

Create a program that creates functions which are your own versions of the list methods. Do not
make use of any built-in list methods to implement them. Your program must do all the
necessary checks to make sure that all the functions work. For functions modifying the original
list, the list must no be changed, but a modified version of it must be returned.

count(list1, x): returns the number of elements with the specified value.
index(list1, x): returns the index of the first element with the specified value. If the value
does not exist, the function returns None.
append(list1, x): adds an element at the end of the list.
insert(list1, x, index): adds an element at the specified position.
remove(list1, x): removes the first element in the list with the specified value.
removeAll(list1, x): removes all the elements in the list with the specified value.
clear(list1): removes all the elements from the list.
pop(list1): removes the last element of the list and returns its value.
"""
general_list = [3, 45, 25, 12, 43, 21, 12, 12, 26, 4, 38, 6, 39, 33, 28]

def verify(fun1, fun2):
    if fun1 == fun2:
        return print('[OK]')
    else:
        return print('[FAIL]')

def own_count(lista: list, num: int):
    count = 0
    for i in range(len(lista)):
        if lista[i] == num:
            count += 1
    return count

def own_index(lista: list, num: int):
    check = True
    count = 0
    while check == True and count < len(lista):
        if lista[count] == num:
            return count
        else:
            count += 1
    return None

def own_append(lista: list, num: int):
    lista += [num]
    return lista
 
def own_insert(lista: list, num: int, num_index: int):
    new_list = lista[:num_index] + [num] + lista[num_index:]
    return new_list


print('count:')
print(own_count(general_list, 43))
verify(own_count(general_list, 43), general_list.count(43))

print('index:')
print(own_index(general_list, 12))
verify(own_index(general_list, 12), general_list.index(12))

print('append:')
lista_append1, lista_append2, lista_append3 = general_list, general_list, general_list
'''Try lista_append1 = lista_append2 = lista_append3 = general_list'''
print(own_append(lista_append1, 1))
lista_append3.append(1)
verify(own_append(lista_append2, 1),lista_append3 )

print('insert:')
lista_insert1, lista_insert2, lista_insert3 = general_list, general_list, general_list
list_insert = own_insert(lista_insert1, 9, 7)
print(list_insert)
lista_insert3.insert(7, 9)
verify(list_insert,lista_insert3)
'''
Hay quer resolver el problema de que las listas al declararlas con igual, 
se van actualizando infinitamente en el tiempo :) 
'''
