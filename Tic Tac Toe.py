board = [' ']*10

from IPython.display import clear_output

def display(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-|-|-")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-|-|-")
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1 enter your marker (X or O):")
        if not (marker == 'X' or marker == 'O'):
            print("Sorry, I don't understand. Please enter a valid choice:")
    player1 = marker
    if marker == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)

def space_check(board,position):
    if board[position] == ' ':
        return True
    else:
        return False

def assignment(board,position,marker):
    
    board[position] = marker

def win_check(board,marker):
        return (board[1] == board[2] == board[3] == marker) or (board[4] == board[5] == board[6] == marker) or (board[7] == board[8] == board[9] == marker) or (board[1] == board[4] == board [7] == marker) or (board[2] == board[5] == board [8] == marker) or (board[3] == board[6] == board [9] == marker) or (board[3] == board[5] == board [7] == marker) or (board[1] == board[5] == board [9] == marker)

import random

def choose_first():
    flip = random.randint(1,2)
    if flip == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def full_board_check(board):
    for i in list(range(1,10)):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = int(input("Enter position:"))
    while not space_check(board,position) or position not in [1,2,3,4,5,6,7,8,9]:
        position = int(input("Please enter a free and valid position:"))
    return position

def replay():
    choice = input("Do you wanna play again? (Yes/No)")
    while choice != "Yes" and choice != "No":
        choice=input("Enter a valid response:")
    return choice == "Yes"

print("Welcome to TIC TAC TOE!!")
while True:
    board = [' ']*10
    marker_1,marker_2 = player_input()
    
    turn = choose_first()
    print(f'{turn} goes first')
    
    play_game = input("Ready to play? (Y/N)")
    if play_game == "Y":
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            display(board)
            position = player_choice(board)
            assignment(board,position,marker_1)
            if win_check(board,marker_1):
                display(board)
                print("Player 1 is the WINNER")
                game_on = False
                
            else:
                if full_board_check(board):
                    display(board)
                    print("Game is a TIE")
                    game_on = False
                    
                else:
                    turn = "Player 2"
                
        else:
            display(board)
            position = player_choice(board)
            assignment(board,position,marker_2)
            if win_check(board,marker_2):
                display(board)
                print("Player 2 is the WINNER")
                game_on = False
                
            else:
                if full_board_check(board):
                    display(board)
                    print("Game is a TIE")
                    game_on = False
                    
                else:
                    turn = "Player 1"
                
    if not replay():
            break