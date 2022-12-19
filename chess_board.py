from chess_pieces import *

chess_board_model_0 = [[0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0]]

chess_board_model_1 = [[15,13,14,19,12,14,13,15],
                    [11,11,11,11,11,11,11,11],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [51,51,51,51,51,51,51,51],
                    [55,53,54,59,52,54,53,55],]

chess_board_model_2 = [[0,52,0,0,0,0,12,0],
                        [11,0,0,11,0,0,0,0],
                        [0,0,19,0,0,11,0,0],
                        [0,0,0,0,0,51,0,0],
                        [0,0,52,0,0,0,0,0],
                        [0,0,0,0,0,0,0,12],
                        [51,11,0,0,0,0,0,0],
                        [0,0,0,0,0,0,11,0]]

def setup_chess_board(board_template):
    game_board = [[],[],[],[],[],[],[],[]]

    pawn_number, pawn_list = 1, []
    rook_number, rook_list = 1, [] 
    knight_number, knight_list = 1, [] 
    bishop_number, bishop_list = 1, [] 
    queen_number, queen_list = 1, []
    king_number, king_list = 1, []

    for row in range(8):
        for col in range(8):
            game_board[row].append(board_template[row][col])  

    for row in range(8):
        if sum(board_template[row]) == 0:
            game_board[row] = ([0,0,0,0,0,0,0,0])
            # print(game_board[row])
            continue

        for col in range(8):
            piece = board_template[row][col]

            if piece == 0:
                game_board[row][col] = 0

            elif str(piece)[1] == "1":
                game_board[row][col] = Pawn(piece//10, pawn_number, (row, col))
                # pawn_list.append(new_piece)
                pawn_number += 1

            
            elif str(piece)[1] == "5":
                game_board[row][col] = Rook(piece//10, rook_number)
                # rook_list.append(new_piece)
                rook_number += 1

            elif str(piece)[1] == "3":
                game_board[row][col] = Knight(piece//10, knight_number)
                # knight_list.append(new_piece)
                knight_number += 1

            elif str(piece)[1] == "4":
                game_board[row][col] = Bishop(piece//10, bishop_number)
                # bishop_list.append(new_piece)
                bishop_number += 1
            
            elif str(piece)[1] == "9":
                game_board[row][col] = Queen(piece//10, queen_number)
                # queen_list.append(new_piece)
                queen_number += 1
            
            elif str(piece)[1] == "2":
                game_board[row][col] = King(piece//10, king_number)
                # king_list.append(new_piece)
                king_number += 1

            col += 1
        # print(game_board[row])
    return game_board

def get_id_board(board):
    id_board = []
    for i in range(8):
        id_board.append([])
        for j in range(8):
            if board[i][j] != 0:
                id_board[i].append(board[i][j].id)
            else: 
                id_board[i].append(0)
        print(id_board[i])

def get_name_board(board):
    name_board = []
    for i in range(8):
        name_board.append([])
        for j in range(8):
            if board[i][j] != 0:
                name_board[i].append(board[i][j].__str__())
            else: 
                name_board[i].append(0)
        print(name_board[i])

if __name__ == "__main__":
    list_of_pieces = setup_chess_board(chess_board_model_1)
    get_id_board(list_of_pieces)
    get_name_board(list_of_pieces)