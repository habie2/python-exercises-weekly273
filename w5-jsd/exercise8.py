"""
@title: exercise 8.
@author: Javier Sanz Diaz
@date: 7 Oct 2021

Create a program that plays "Twenty 0ne”, a simple dice version of Blackjack. For this game two
dices will be rolled. The points will be calculated as the sum of the rolls of the two dices.
Although the game can be played with several players, to simplify it we will play only with two.
The rules are as follows:
● Each player plays only once per game.
● The player can roll the dice as many times as desired and can stop at any time if the
score is no higher than 21. Numbers obtained in each roll are added to the previous in
order to establish the score.
● If a player reaches a score greater than 21 she loses immediately, so the other player is
automatically the winner.
● If no player has exceeded 21, the participant whose total is nearest to 21 points, wins. If
the two players reach the same score, then it will be declared a tie.
● The number of games to be played will be a value defined as a constant in the program.
Taking into account the specifications established and the example provided:
▪ Program the move corresponding to player 1 until she decides to stop, or the score is
higher than 21, in this last case player 1 has lost.
▪ Program also the move corresponding to player 2 and display the winner (or the tie)
▪ Modify the exercise to run multiple games as indicated in the statement.
"""
import random

NUM_GAMES = 3

for x in range(NUM_GAMES):
    acummulated1 = 0
    acummulated2 = 0

    #PLAYER 1
    print(f'\nGAME {x + 1} - PLAYER 1')
    dice1_player1 = random.randint(1, 6)
    dice2_player1 = random.randint(1, 6)
    acummulated1 += (dice1_player1 + dice2_player1) 
    print(f'''The number of points obteined are: {dice1_player1}, {dice2_player1}
The points accumulated are: {acummulated1}''')

    while acummulated1 <= 21 and input('Would you like to roll the dice again? (yes/no)') == 'yes':
        dice1_player1 = random.randint(1, 6)
        dice2_player1 = random.randint(1, 6)
        acummulated1 =acummulated1 + (dice1_player1 + dice2_player1) 
        print(f'''The number of points obteined are: {dice1_player1}, {dice2_player1}
The points accumulated are: {acummulated1}''')
    if acummulated1 > 21:
        print(f'Player 1 lost, the points have overcomed 21 ({acummulated1})')
        
    #PLAYER 2
    if acummulated1 <= 21:
        print(f'\nGAME {x + 1} - PLAYER 2')
        dice1_player2 = random.randint(1, 6)
        dice2_player2 = random.randint(1, 6)
        acummulated2 += (dice1_player2 + dice2_player2) 
        print(f'''The number of points obteined are: {dice1_player2}, {dice2_player2}
The points accumulated are: {acummulated2}''')

        while acummulated2 <= 21 and input('Would you like to roll the dice again? (yes/no)') == 'yes':
            dice1_player2 = random.randint(1, 6)
            dice2_player2 = random.randint(1, 6)
            acummulated2 =acummulated2 + (dice1_player2 + dice2_player2) 
            print(f'''The number of points obteined are: {dice1_player2}, {dice2_player2}
The points accumulated are: {acummulated2}''')
        if acummulated2 > 21:
            print(f'Player 2 lost, the points have overcomed 21 ({acummulated2})')

        #COMPARISON BETWEEN BOTH OF THE PLAYERS
        if acummulated2 <= 21:
            if acummulated1 > acummulated2:
                print('***********PLAYER 1 WINS***********')
            elif acummulated1 < acummulated2:
                print('***********PLAYER 2 WINS***********')
            else: #they are equal
                print('***********TIE***********')
