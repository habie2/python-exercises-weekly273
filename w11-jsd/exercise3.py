"""
@title: exercise3
@author: habi2
@date: 21/11/2021

Create a Dice class with fields name and rolls, to simulate a dice game. The rolls field
must be a list. Create an init method that receives the name of the player and an integer n,
which represents the number of rolls. It must assign the name to the corresponding field and
create a list of n elements randomly filled with numbers from 1 to 6. Create a two-player game
asking each player his/her name. It must print the results for each one and calculate the winner,
which will be the one with the highest number of equal dice. In case of a tie, the one with the
highest total score will win.
"""
from exercise3class import Dice

player1 = Dice(input('Name player 1: '), int(input('Number of throws player 1: ')))
player2 = Dice(input('Name player 2: '), int(input('Number of throws player 2: ')))

print(player1, player2)
print(player1 == player2)
