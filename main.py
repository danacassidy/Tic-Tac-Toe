
def display_board(board):
     print('   |   |')
     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
     print('   |   |')


def player_input():
  marker = ' '
  while not (marker == 'X' or marker == 'O'):
          marker = input('Player 1: Do you want to be X or O? ').upper()

  if marker == 'X':
      return('X','O')
  else:
      return('O','X')

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def place_marker(board, marker, position):
    board[position] = marker
    print(display_board(board))
    pass

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose your next position: (1-9)'))

    return position




def full_board_check(board):

    for i in range(1,10):
            if space_check(board,i):
                return False
    return True


def space_check(board, position):
    return board[position] == ' '


def win_check(board, mark):
    return( board[1]== mark and board[2]== mark and board[3]== mark or
    board[4]== mark and board[5]== mark and board[6]== mark or
    board[7]== mark and board[8]== mark and board[9]== mark or
    board[1]== mark and board[5]== mark and board[9]== mark or
    board[3]== mark and board[5]== mark and board[7]== mark or
    board[1]== mark and board[4]== mark and board[7]== mark or
    board[2]== mark and board[5]== mark and board[8]== mark or
    board[3]== mark and board[6]== mark and board[9]== mark )


def replay():
    return input('Would you like to play again? Yes or No').lower().startswith('y')

test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

print('Welcome to Tic Tac Toe!')

while True:
    #reset the board
    theBoard = [' ']*10
    player1_marker,player2_marker = player_input()
    turn= choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            display_board(theBoard)
            position= player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'



        else:
            #player2 turn

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'















        # Player2's turn.

            #pass

    if not replay():
        break