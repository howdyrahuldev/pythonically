'''
This project is about creating a electronic Tic-Tac-Toe game.

1. Defined multiple functions to achieve different pieces of the game.
2. Handled exception for wrong entries
3. Binded all the functions by calling those inside a function
'''


#importing all the function from features_module module in same location
from features_module import *

print('Welcome!!! Let\'s play Tic Tac Toe')

player1 = input('Enter player 1 name: ')
player2 = input('Enter player 2 name: ')

while True:
    the_board = [i for i in range(0, 10)]
    if choose_first() == 'player1':
        my_turn = player1
    else:
        my_turn = player2

    print(f'Congratulation {my_turn}!!! You have the chance to choose first.')
    #assign markers to both the players
    if my_turn == player1:
        player1_marker, player2_marker = player_input(my_turn)
    else:
        player2_marker, player1_marker = player_input(my_turn)
    game = True

    while game:
        if my_turn == player1:

            display_board(the_board)
            position = player_choice(player1, the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print(f'Congratulation {player1}!!!! You have won the game...')
                game = False
            else:
                if full_board_check(the_board):
                    print('This match has been drawn....')
                    break
                else:
                    my_turn = player2

        else:
            display_board(the_board)
            position = player_choice(player2, the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print(f'Congratulation {player2}!!!! You have won the game...')
                game = False
            else:
                if full_board_check(the_board):
                    print('This match has been drawn....')
                    break
                else:
                    my_turn = player1

    if replay().lower()[0] != 'y':
        print('Thank You!!! Exiting the game.')
        break
    else:
        print('All Right!!! Arranging  rematch for you.')