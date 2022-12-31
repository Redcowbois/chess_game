from chess_board import Chess_Board

BOARD = [[15,14,14,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,13],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,52,0,0,0]]

# BOARD = Chess_Board.chess_board_model_1

has_turns = False

white_side = True
black_side = False

white_king_pos = -1
black_king_pos = -1

def print_board(board):
    for row in board:
        print(row)