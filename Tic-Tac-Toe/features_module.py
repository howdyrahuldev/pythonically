# defining module for multiple functions

# importing random module for generating random number
import random


# Display_Board for Tic-Tac-Toe
def display_board(board):
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('---*---*---')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('---*---*---')
    print(f' {board[7]} | {board[8]} | {board[9]}')


# Selection of player marker
def player_input(player):
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input(f'{player}: Choose your marker: ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# Place marker to the position
def place_marker(board, marker, position):
    board[position] = marker


# Checking all the eight possibilities of winning the game
def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or (board[9] == board[5] == board[1] == mark))


# Chosing who will play first
def choose_first():
    if random.randint(0, 1) == 0:
        return "player1"
    else:
        return "player2"


# checks if the position has number or not
def num_check(board, position):
    return str(board[position]).isnumeric()


# checks the full board, if there's any numeric position left
def full_board_check(board):
    for i in range(1, 10):
        if num_check(board, i):
            return False
    return True


# validate the player's choice of position
def player_choice(player, board):
    position = 0
    while position not in range(1, 10) or not num_check(board, position):
        while True:
            try:
                position = int(input(f'{player}, please choose your next position: '))
            except:
                print('Please select a valid choice.')
            else:
                break
    return position


# takes choice for a rematch
def replay():
    print('Do you want to play again?')
    repl = input('Your answer is ')
    return repl
