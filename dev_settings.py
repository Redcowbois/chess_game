from chess_board import Chess_Board

BOARD = [[15,0,0,0,0,0,0,16],
        [0,0,0,11,11,11,0,17],
        [0,0,0,0,51,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,12,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,52,0,0,0]]

# BOARD = Chess_Board.chess_board_model_1

has_turns = False
turn = 10

white_side = True
black_side = False

white_king_pos = -1
black_king_pos = -1

def print_board(board):
    for row in board:
        print(row)