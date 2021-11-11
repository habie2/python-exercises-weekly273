"""
@title: excercise 8.
@author: Javier Sanz Diaz
@date: 17 Oct 2021

Write a program that asks the user to enter a sentence. Then, it introduces each character of the
sentence in a tuple, ignoring the repeated characters. The characters introduced in the tuple
should be capitalized (you can use the upper() method of strings). Finally, it prints the tuple.
For instance:
Write a sentence: Hi, how are you?
(’H’, ’I’, ’,’, ’ ’, ’O’, ’W’, ’A’, ’R’, ’E’, ’Y’, ’U’, ’?’)
"""
sentence_input = input('Enter a sentence: ').upper()
print(sentence_input)
list_letters = []

for i in range(len(sentence_input)):
    if sentence_input[i] not in list_letters:
        list_letters.append(sentence_input[i])
tuple_letters = tuple(list_letters)

print(tuple_letters)