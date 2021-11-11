"""
@title: exercise5
@author: habi2
@date: 09/11/2021

Generate a function that allows you to correctly write uppercase letters in a given text: The first
character of the string must be written in uppercase; also the “i” letter when it is followed by a
blank space and the previous one is a blank space too. In addition, the first non-blank character
after a ".", "!" or "?" For example, if the function is provided with the string "what time do i
have to be there? what is the address?", Then it should return the string "What
time do I have to be there? What is the address?" Include a program that
reads a user string, capitalizes the appropriate letters using this function and displays the result
on the screen.

input('Introduce a text: ')
"""

def la_funsion_de_las_is(text_input = input('Introduce a text: ')):
    lista = []
    for i in text_input:
        lista.append(i)
    for _ in range(2):
        lista.append(' ') #we append to black spaces just in case th last cha
                            #characters is one of these: ".", "!" or "?" we do 
                            #not get an error becuase of the index

    lista[0] = lista[0].upper() #The first character of the string must be written in uppercase

    for i in range(len(lista)):
        if lista[i] == 'i' and lista[i - 1] == ' ' and  lista[i + 1] == ' ':
            lista[i] = 'I'
        if lista[i] == '.' or lista[i] == '!' or lista[i] == '?':
            lista[i + 2] = lista[i + 2].upper()
        
    for i in range(len(lista)):
        print(lista[i], end = '')

la_funsion_de_las_is()