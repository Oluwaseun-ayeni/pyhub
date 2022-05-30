import random
import time


def display_board(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[1], board[2], board[3]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[4], board[5], board[6]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(board[7], board[8], board[9]))
    print("\t     |     |")
    print("\n")


def player_input():
    marker = 'wrong'
    while marker not in ['X', 'O']:
        marker = input(" Player1,Choose what code you will love to use X or O:").upper()

    player1 = marker
    if player1 == 'X':
        player2 = 'O'

    else:
        player2 = 'X'

    return player1, player2


count_second = 5
for i in reversed(range(count_second + 1)):
    if i > 0:
        print(i, end='>>>')
        time.sleep(1)
    else:
        print('Start!')


def place_maker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

        return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').upper().startswith('Y')


print('Welcome to Tic Tac Toe')

while True:

    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play y? or n?').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':

            display_board(the_board)

            position = player_choice(the_board)

            place_maker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won! ')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                else:
                    turn = 'Player2'


        else:
            display_board(the_board)

            position = player_choice(the_board)

            place_maker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won! ')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                else:
                    turn = 'Player1'

    if not replay():
        break
