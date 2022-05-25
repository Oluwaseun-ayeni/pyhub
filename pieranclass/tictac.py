def display_board(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("\t     |     |")
    print("\n")


test_board = [' '] * 10
display_board(test_board)


def player_input():
    marker = 'wrong'
    while marker not in ['X', 'O']:
        marker = input(" Player1,Choose what code you will love to use X or O:")

    player1 = marker
    if player1 == 'X':
        player2 = 'O'

    else:
        player2 = 'X'

    return player1, player2


player1_marker, player2_marker = player_input()

player_input()


def place_maker(board, marker, position):
    values = [' ' for x in range(9)]




#     marker = {'X': [], 'O': []}
#
#     while True:
#         display_board(board)
#
#
#         try:
#             print("Player",marker,"turn. Which box? : ", end="")
#             marker = int(input())
#
#
#         except ValueError:
#             print("Wrong input !!! Try again")
#             continue
#
#         if marker < 1 or marker > 9:
#             print("Wrong input!!! Try again")
#             continue
#
#         if board[marker-1] != ' ':
#             print("Place already filled. Try again !!")
#             continue
