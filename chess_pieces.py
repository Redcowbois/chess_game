class Pawn():
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 1
        self.id = str(self.team + self.number + self.piece_type)
    
    def __str__(self):
        __str__ = ""
        if self.id[0] == 1:
            __str__ += "White "
        else:
            __str__ += "Black "

        return __str__ + "Pawn" + str(self.id[-3])
    
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
        self.id = str(self.team + self.number + self.piece_type)

    def __str__(self):
        __str__ = ""
        if self.id[0] == 1:
            __str__ += "White "
        else:
            __str__ += "Black "
            
        return __str__ + "Rook" + str(self.id[-3])
    
class Knight(): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 3
        self.id = str(self.team + self.number + self.piece_type)

    def __str__(self):
        __str__ = ""
        if self.id[0] == 1:
            __str__ += "White "
        else:
            __str__ += "Black "
            
        return __str__ + "Knight" + str(self.id[-3])

class Bishop(): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 4
        self.id = str(self.team + self.number + self.piece_type)
    
    def __str__(self):
        __str__ = ""
        if self.id[0] == 1:
            __str__ += "White "
        else:
            __str__ += "Black "
            
        return __str__ + "Bishop" + str(self.id[-3])
class Queen(): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 9
        self.id = str(self.team + self.number + self.piece_type)
    
    def __str__(self):
        __str__ = ""
        if self.id[0] == 1:
            __str__ += "White "
        else:
            __str__ += "Black "
            
        return __str__ + "Queen" + str(self.id[-3])

class King(): 
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 2
        self.id = str(self.team + self.number + self.piece_type)
    
    def __str__(self):
        __str__ = ""
        if self.id[0] == 1:
            __str__ += "White "
        else:
            __str__ += "Black "
            
        return __str__ + "King" + str(self.id[-3])
