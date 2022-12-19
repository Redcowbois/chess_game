class Piece():
    def __init__(self):
        self.id = "piece"

class Pawn(Piece):
    def __init__(self, team, number, position):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 1
        self.id = str(self.team + self.number + self.piece_type)

        self.moved = False
        self.position = position
        self.valid_movement = []
    
    def __str__(self):
        __str__ = ""
        if self.id[0] == "5":
            __str__ += "White "
        else:
            __str__ += "Black "
    
        return __str__ + "Pawn" + str(self.id[-3])
    
    def get_valid_movement(self, board_matrix):
        self.valid_movement = []
        row, col = self.position

        if self.id[0] == "1": #Black
            if board_matrix[row+1][col] == 0:
                self.valid_movement += [(row + 1, col)]

            if col + 1 <= 7 and isinstance(board_matrix[row+1][col+1], Piece)\
            and board_matrix[row+1][col+1].id[0] == "5":
                self.valid_movement += [(row + 1, col + 1)]
            
            if col - 1 >= 0 and isinstance(board_matrix[row+1][col-1], Piece)\
            and board_matrix[row+1][col-1].id[0] == "5":
                self.valid_movement += [(row + 1, col - 1)]

            if not self.moved and board_matrix[row+1][col] == 0:
                self.valid_movement += [(row + 2, col)]

        elif self.id[0] == "5": #White
            if board_matrix[row - 1][col] == 0:
                self.valid_movement += [(row - 1, col)]
            
            if col + 1 <= 7 and isinstance(board_matrix[row-1][col+1], Piece)\
            and board_matrix[row-1][col+1].id[0] == "1":
                    self.valid_movement += [(row - 1, col + 1)]

            if col - 1 >= 0 and isinstance(board_matrix[row-1][col-1], Piece)\
            and board_matrix[row-1][col-1].id[0] == "1":
                    self.valid_movement += [(row - 1, col - 1)]

            if not self.moved and board_matrix[row-1][col] == 0:
                self.valid_movement += [(row - 2, col)]
            
class Rook(Piece): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 5
        self.id = str(self.team + self.number + self.piece_type)

    def __str__(self):
        __str__ = ""
        if self.id[0] == "5":
            __str__ += "White "
        else:
            __str__ += "Black "
            
        return __str__ + "Rook" + str(self.id[-3])
    
    def get_valid_movement(self, board_matrix):
        self.valid_movement = []
        row, col = self.position
        

class Knight(Piece): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 3
        self.id = str(self.team + self.number + self.piece_type)

    def __str__(self):
        __str__ = ""
        if self.id[0] == "5":
            __str__ += "White "
        else:
            __str__ += "Black "
            
        return __str__ + "Knight" + str(self.id[-3])

class Bishop(Piece): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 4
        self.id = str(self.team + self.number + self.piece_type)
    
    def __str__(self):
        __str__ = ""
        if self.id[0] == "5":
            __str__ += "White "
        else:
            __str__ += "Black "
            
        return __str__ + "Bishop" + str(self.id[-3])
class Queen(Piece): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 9
        self.id = str(self.team + self.number + self.piece_type)
    
    def __str__(self):
        __str__ = ""
        if self.id[0] == "5":
            __str__ += "White "
        else:
            __str__ += "Black "
            
        return __str__ + "Queen" + str(self.id[-3])

class King(Piece): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 2
        self.id = str(self.team + self.number + self.piece_type)

        self.checked = False
        self.moved = False
    
    def __str__(self):
        __str__ = ""
        if self.id[0] == "5":
            __str__ += "White "
        else:
            __str__ += "Black "
            
        return __str__ + "King" + str(self.id[-3])
