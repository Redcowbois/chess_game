class Piece():
    def __init__(self, team, number, piece_type, position):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = piece_type
        self.id = str(self.team + self.number + self.piece_type)

        self.position = position
        self.valid_movement = []
    
    def __str__(self):
        type_dict = {"1": "Pawn", "2": "King", "3": "Knight", 
                    "4": "Bishop", "5": "Knight", "9": "Queen", "6": "Test"}
        __str__ = ""

        if self.id[0] == "5":
            __str__ += "White "
        else:
            __str__ += "Black "
    
        return __str__ + type_dict[self.id[-1]] + str(self.id[-4:-2])

class Pawn(Piece):
    def __init__(self, team, number, position):
        super().__init__(team, number, 1, position)
        self.moved = False
    
    def get_valid_movement(self, board_matrix):
        self.valid_movement = []
        row, col = self.position

        if self.id[0] == "1": #Black
            if row+1 <= 7 and board_matrix[row+1][col] == 0:
                self.valid_movement += [(row + 1, col)]

            if col + 1 <= 7 and row+1 <= 7 and isinstance(board_matrix[row+1][col+1], Piece)\
            and board_matrix[row+1][col+1].id[0] == "5":
                self.valid_movement += [(row + 1, col + 1)]
            
            if col - 1 >= 0 and row+1 <= 7 and isinstance(board_matrix[row+1][col-1], Piece)\
            and board_matrix[row+1][col-1].id[0] == "5":
                self.valid_movement += [(row + 1, col - 1)]

            if not self.moved and board_matrix[row+1][col] == 0:
                self.valid_movement += [(row + 2, col)]

        elif self.id[0] == "5": #White
            if row - 1 >= 0 and board_matrix[row - 1][col] == 0:
                self.valid_movement += [(row - 1, col)]
            
            if col + 1 <= 7 and row - 1 >= 0 and isinstance(board_matrix[row-1][col+1], Piece)\
            and board_matrix[row-1][col+1].id[0] == "1":
                    self.valid_movement += [(row - 1, col + 1)]

            if col - 1 >= 0 and row - 1 >= 0 and isinstance(board_matrix[row-1][col-1], Piece)\
            and board_matrix[row-1][col-1].id[0] == "1":
                    self.valid_movement += [(row - 1, col - 1)]

            if not self.moved and board_matrix[row-1][col] == 0:
                self.valid_movement += [(row - 2, col)]

class Rook(Piece): 
    def __init__(self, team, number, position):
        super().__init__(team, number, 5, position)

    def get_valid_movement(self, board_matrix):
        self.valid_movement = []
        row, col = self.position

        check_direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i, j in check_direction:
            row, col = self.position
            while row + i >= 0 and row + i <= 7 and col + j >= 0 and col + j <= 7:
                row += i
                col += j
                next_piece = board_matrix[row][col]

                if next_piece == 0:
                    self.valid_movement += [(row, col)]
                elif next_piece.id[0] != self.id[0]:
                    self.valid_movement += [(row, col)]
                    break
                elif next_piece.id[0] == self.id[0]:
                    break
        
class Knight(Piece): 
    def __init__(self, team, number, position):
        super().__init__(team, number, 3, position)

    def get_valid_movement(self, board_matrix):
        self.valid_movement = []
        row, col = self.position
        check_direction = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, -2), (-1, -2), (1, 2), (-1, 2)]

        for i, j in check_direction:
            row, col = self.position
            if row + i >= 0 and row + i <= 7 and col + j >= 0 and col + j <= 7:
                row += i
                col += j
                next_piece = board_matrix[row][col]
                
                if next_piece == 0:
                    self.valid_movement += [(row, col)]
                elif next_piece.id[0] != self.id[0]:
                    self.valid_movement += [(row, col)]

class Bishop(Piece): 
    def __init__(self, team, number, position):
        super().__init__(team, number, 4, position)
    

    def get_valid_movement(self, board_matrix):
        self.valid_movement = []
        row, col = self.position
        check_direction = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for i, j in check_direction:
            row, col = self.position
            while row + i >= 0 and row + i <= 7 and col + j >= 0 and col + j <= 7:
                row += i
                col += j
                next_piece = board_matrix[row][col]

                if next_piece == 0:
                    self.valid_movement += [(row, col)]
                elif next_piece.id[0] != self.id[0]:
                    self.valid_movement += [(row, col)]
                    break
                elif next_piece.id[0] == self.id[0]:
                    break

class Queen(Piece): 
    def __init__(self, team, number, position):
        super().__init__(team, number, 9, position)
    def get_valid_movement(self, board_matrix):
        self.valid_movement = []
        row, col = self.position
        check_direction = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]

        for i, j in check_direction:
            row, col = self.position
            while row + i >= 0 and row + i <= 7 and col + j >= 0 and col + j <= 7:
                row += i
                col += j
                next_piece = board_matrix[row][col]
                
                if next_piece == 0:
                    self.valid_movement += [(row, col)]
                elif next_piece.id[0] != self.id[0]:
                    self.valid_movement += [(row, col)]
                    break
                elif next_piece.id[0] == self.id[0]:
                    break

class King(Piece): 
    def __init__(self, team, number, position):
        super().__init__(team, number, 2, position)
        self.checked = False
        self.moved = False
    
    
    def get_valid_movement(self, board_matrix):
        self.valid_movement = []
        row, col = self.position
        check_direction = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]

        for i, j in check_direction:
            row, col = self.position
            if row + i >= 0 and row + i <= 7 and col + j >= 0 and col + j <= 7:
                row += i
                col += j
                next_piece = board_matrix[row][col]
                
                if next_piece == 0:
                    self.valid_movement += [(row, col)]
                elif next_piece.id[0] != self.id[0]:
                    self.valid_movement += [(row, col)]

class Test(Piece):
    def __init__(self, team, number, position):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 6
        self.id = str(self.team + self.number + self.piece_type)
        self.position = position
        self.valid_movement = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
    
    def get_valid_movement(self, game_board):
        return 0