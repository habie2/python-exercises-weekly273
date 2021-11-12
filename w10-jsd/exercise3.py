"""
@title: exercise1
@author: habi2
@date: 11/11/2021

Create a function that receives as parameters a list and an element and returns a tuple with the
positions of the element in the list, or the empty tuple if the element is not in the list. Invoking
this function, create another one that receives two lists and an element and returns if any of the
appearances of the element is at the same position in both lists.
"""

def list_search(lista: list, searched_element: int):
    n = 0
    pos_lista = []
    while searched_element in lista[n:]:
        # By using the second parameter of index, we declare the position we
        # would like to start to search that element in the list. We could also 
        # declare and end parameter, but in this case is not practical. 
        index_num = lista.index(searched_element, n) 
        pos_lista.append(index_num)
        n = index_num + 1
    return tuple(pos_lista)

def list2_searchs(lista1: list, lista2: list, searched_element: int):
    # List to store the positions of the repeated elements (starting by zero)
    pos_repeated = []

    result1 = list_search(lista1, searched_element)
    result2 = list_search(lista2, searched_element)
    if len(result1) <= len(result2):
        for i in range(len(result1)):
            if result1[i] in result2:
                pos_repeated.append(result1[i])
    else:
        for i in range(len(result2)):
            if result2[i] in result1:
                pos_repeated.append(result2[i])
    return pos_repeated, searched_element

lista_def , searched_elem = list2_searchs([2, 3, 4, 2, 6], [2, 6], 2)

print(lista_def, searched_elem)

if lista_def == []:
    print(f'There is no {searched_elem} at the same position')
else:
    print(f'The number {searched_elem} is repeated at positions:')
    for i in lista_def[:-1]:
        print(i , end= ', ')
    print(lista_def[-1])