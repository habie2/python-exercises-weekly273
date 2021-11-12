"""
@title: exercise1
@author: habi2
@date: 11/11/2021

Define a function combine (list1, list2), which given two lists returns a list that
combines both lists, but eliminates duplicates. Example:
list1: [1, 2, 3, 4, 5, 6]
list2: [4, 5, 6, 7, 8, 9]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
def merge(lista1: list, lista2: list):
    lista_def = []

    for i in lista1:
        if i not in lista_def:
            lista_def.append(i)
    for i in lista2:
        if i not in lista_def:
            lista_def.append(i)
    return lista_def

print(merge([1, 3, 3, 3, 3, 6],
[4, 5, 6, 7, 8, 9]))