'''
@title: exercise6
@author: habi2
@date: 24/10/2021

Given the following dictionary:
toyShop = {
 'dolls': 500
 'games': ['Guess who?', 'Clue', 'Battleship']
 'puzzles': ['Star Wars', 'Batman', 'Ironman']
}
Add a key to toyShop called ’fluffyToy’ and set its value as a list consisting of the strings
’bear’, ’dog’, and ’cat’. Remove ’Batman’ from the list of items stored under the
’puzzles’ key. Add 100 to the number stored under ’dolls’ key. 
'''

toyShop = {
'dolls': 500,
'games': ['Guess who?', 'Clue', 'Battleship'],
'puzzles': ['Star Wars', 'Batman', 'Ironman']
}

toyShop['fluffyToy'] = ['bear', 'dog', 'cat']
del(toyShop['puzzles'][1])
toyShop['dolls'] += 100

print(toyShop)
