from chess_pieces import *

#Class for the chess_board
class Chess_Board(): 
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
                    [55,53,54,59,52,54,53,55]]

    chess_board_model_2 = [[0,52,0,0,0,0,12,0],
                        [11,0,0,11,0,0,0,0],
                        [0,0,19,0,0,11,0,0],
                        [0,0,0,0,0,51,0,0],
                        [0,0,52,0,0,0,0,0],
                        [0,0,0,0,0,0,0,12],
                        [51,11,0,0,0,0,0,0],
                        [0,0,0,0,0,0,11,0]]

    chess_board_model_3 = [[15,0,0,0,12,0,0,15],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,16,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [55,0,0,0,52,0,0,55]]
    
    chess_board_model_4 = [[0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,25,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,12,0,0,0,0]]

    #Sets up the chess board with the Piece objects
    def setup_chess_board(board_template): 
        game_board = [[],[],[],[],[],[],[],[]]

        pawn_number = 1
        rook_number = 1 
        knight_number = 1 
        bishop_number = 1 
        queen_number = 1
        king_number = 1
        king_list = []

        for row in range(8):
            for col in range(8):
                game_board[row].append(board_template[row][col])  

        for row in range(8): #If row only has 0, skip.
            if sum(board_template[row]) == 0:
                game_board[row] = ([0,0,0,0,0,0,0,0])
                continue

            for col in range(8):
                piece = board_template[row][col]

                if piece == 0:
                    game_board[row][col] = 0

                elif str(piece)[1] == "1":
                    game_board[row][col] = Pawn(piece//10, pawn_number, (row, col))
                    if row < 4:
                        game_board[row][col].white_side = False
                    else: 
                        game_board[row][col].white_side = True
                    pawn_number += 1

                elif str(piece)[1] == "5":
                    game_board[row][col] = Rook(piece//10, rook_number, (row, col))
                    rook_number += 1

                elif str(piece)[1] == "3":
                    game_board[row][col] = Knight(piece//10, knight_number, (row, col))
                    knight_number += 1

                elif str(piece)[1] == "4":
                    game_board[row][col] = Bishop(piece//10, bishop_number, (row, col))
                    bishop_number += 1
                
                elif str(piece)[1] == "9":
                    game_board[row][col] = Queen(piece//10, queen_number, (row, col))
                    queen_number += 1
                
                elif str(piece)[1] == "2":
                    game_board[row][col] = King(piece//10, king_number, (row, col))
                    king_list.append(game_board[row][col])
                    king_number += 1
                
                elif str(piece)[1] == "6":
                    game_board[row][col] = Test(piece//10, king_number, (row, col))

                col += 1
        return game_board

    #Changes the side facing the player
    def invert_board(board):
        return board[-1::-1]
    
    #Get a matrix with all the ids of the pieces
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

    #Get a matrix with all the names of the pieces
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
    list_of_pieces = Chess_Board.setup_chess_board(Chess_Board.invert_board(Chess_Board.chess_board_model_1))
    Chess_Board.get_id_board(list_of_pieces)
    Chess_Board.get_name_board(list_of_pieces)