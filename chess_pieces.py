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

chess_board_model_2 = [[0,0,0,0,0,0,0,0],
                        [0,0,0,11,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,51,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [51,11,0,0,0,0,0,0],
                        [0,0,0,0,0,0,11,0]]

class Pawn():
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 1
        self.id = self.team + self.number + self.piece_type
    
    def valid_movement(self, board_matrix):
        for row in range(len(board_matrix)):
            for col in range(len(board_matrix[row])):
                if self.id == board_matrix[row][col]:
                    if str(self.id)[0] == "1":
                        return row+1
                    if str(self.id)[0] == "5":
                        return row-1
class Rook(): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 5
        self.id = self.team + self.number + self.piece_type

class Knight(): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 3
        self.id = self.team + self.number + self.piece_type

class Bishop(): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 4
        self.id = self.team + self.number + self.piece_type
class Queen(): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 9
        self.id = self.team + self.number + self.piece_type

class King(): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 2
        self.id = self.team + self.number + self.piece_type

game_board = [[],[],[],[],[],[],[],[]]
def setup_chess_board(board_template):

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

        col = 0
        for piece in board_template[row]:
            if piece == 0:
                game_board[row][col] = 0

            elif str(piece)[1] == "1":
                new_piece = Pawn(piece//10, pawn_number)
                game_board[row][col] = new_piece.id
                pawn_list.append(new_piece)
                pawn_number += 1

            
            elif str(piece)[1] == "5":
                new_piece = Rook(piece//10, rook_number)
                game_board[row][col] = new_piece.id
                rook_list.append(new_piece)
                rook_number += 1

            elif str(piece)[1] == "3":
                new_piece = Knight(piece//10, knight_number)
                game_board[row][col] = new_piece.id
                knight_list.append(new_piece)
                knight_number += 1

            elif str(piece)[1] == "4":
                new_piece = Bishop(piece//10, bishop_number)
                game_board[row][col] = new_piece.id
                bishop_list.append(new_piece)
                bishop_number += 1
            
            elif str(piece)[1] == "9":
                new_piece = Queen(piece//10, queen_number)
                game_board[row][col] = new_piece.id
                queen_list.append(new_piece)
                queen_number += 1
            
            elif str(piece)[1] == "2":
                new_piece = King(piece//10, king_number)
                game_board[row][col] = new_piece.id
                king_list.append(new_piece)
                king_number += 1

            col += 1
        # print(game_board[row])
    return {"pawn": pawn_list, "rook": rook_list, "knight": knight_list, 
            "bishop": bishop_list, "queen": queen_list, "king": king_list}

if __name__ == "__main__":
    list_of_pieces = setup_chess_board(chess_board_model_1)
    for i in game_board:
        print(i)
    print(list_of_pieces)


