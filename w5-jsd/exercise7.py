"""
@title: exercise 7.
@author: Javier Sanz Diaz
@date: 11 Oct 2021

Create a program which plays "Rock, paper, scissors", with the next specifications:
● There will be one player who plays against the machine.
● The number of games will be a constant in the program. The game will be repeated the
number of times indicated in this constant.
● The following message will be shown in order to ask the user for the move:
ROCK, PAPER OR SCISSORS?
● The program will randomly obtain the move (rock, paper or scissors). The program will show
the winner according to the following rules:
▪ Rock crushes scissors (Rock wins)
▪ Scissors cuts paper (Scissors wins)
▪ Paper wraps stone (Paper wins)
▪ In case of tie, the message “TIE” will be shown.
"""
import random

NUM_GAMES = 3

print(f'{NUM_GAMES} games will be run')

for x in range(NUM_GAMES):
    user_choose = input('ROCK, PAPER OR SCISSORS?')

    computer_randomnum_choose = random.randint(1,3)
    if computer_randomnum_choose == 1:
        computer_choose = 'PAPER'
        print('Computer chooses paper')
    elif computer_randomnum_choose == 2:
        computer_choose = 'ROCK'
        print('Computer chooses rock')
    elif computer_randomnum_choose == 3:
        computer_choose = 'SCISSORS'
        print('Computer chooses scissors')

    #PLAYER WINS
    if user_choose == 'ROCK' and computer_choose == 'SCISSORS':
        print('*****PLAYER WINS*****')
    elif user_choose == 'SCISSORS' and computer_choose == 'PAPER':
        print('*****PLAYER WINS*****')
    elif user_choose == 'PAPER' and computer_choose == 'ROCK':
        print('*****PLAYER WINS*****')

    #COMPUTER WINS
    elif user_choose == 'SCISSORS' and computer_choose == 'ROCK':
        print('*****COMPUTER WINS*****')
    elif user_choose == 'PAPER' and computer_choose == 'SCISSORS':
        print('*****COMPUTER WINS*****')
    elif user_choose == 'ROCK' and computer_choose == 'PAPER':
        print('*****COMPUTER WINS*****')

    #TIE
    elif user_choose == 'PAPER' and computer_choose == 'PAPER':
        print('*****TIE*****')
    elif user_choose == 'ROCK' and computer_choose == 'ROCK':
        print('*****TIE*****')
    elif user_choose == 'SCISSORS' and computer_choose == 'SCISSORS':
        print('*****TIE*****')
