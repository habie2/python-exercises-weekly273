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

def verify(name_fun:str, fun1, fun2):
    print(name_fun)
    print(fun1)
    if fun1 == fun2:
        return print('[OK]\n')
    else:
        return print('[FAIL]\n')

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

verify('count:', own_count(general_list, 43), general_list.count(43))

verify('index:', own_index(general_list, 12), general_list.index(12))

lista_append1, lista_append2 = general_list[:],  general_list[:]
lista_append2.append(1)
verify('append:', own_append(lista_append1, 1),lista_append2 )

lista_insert1, lista_insert2 = general_list[:],  general_list[:]
lista_insert2.insert(7, 9)
verify('insert:', own_insert(lista_insert1, 9, 7),lista_insert2)

lista_remove1, lista_remove2 = general_list[:],  general_list[:]
lista_remove2.remove(12)
verify('remove:', own_remove(lista_remove1, 12),lista_remove2)

lista_removeAll1  = general_list[:]
verify('removeAll:', own_removeAll(lista_removeAll1, 12), [3, 45, 25, 43, 21, 26, 4, 38, 6, 39, 33, 28])

lista_clear1, lista_clear2 = general_list[:],  general_list[:]
verify('clear:', own_clear(lista_clear1), lista_clear2.clear())

lista_pop1, lista_pop2 = general_list[:],  general_list[:]
verify('pop:', own_pop(lista_pop1), lista_pop2.pop())