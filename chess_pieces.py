import pygame
pygame.init()

chess_board =  [[5,3,4,9,2,4,3,5],
                [1070101,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,1,1,1079901,1,1,1,1],
                [5,3,4,9,2,4,3,5],]

# class Pawn():
#     def __init__(self, team, number):
#         self.team = 1000000*team 
#         self.number = 70000 + number*100
#         self.piece_type = 1
#         self.id = self.team + self.number + self.piece_type
    
#     def valid_movement(self, board_matrix):
#         for row in range(len(board_matrix)):
#             for col in range(len(board_matrix[row])):
#                 if self.id == board_matrix[row][col]:
#                     if str(self.id)[0] == "1":
#                         allowed_mouvement = pygame.Surface(((row + 1)*100,(col + 1)*100))
#                         window.blit(allowed_mouvement, ((row + 1)*100,(col + 1)*100))

# pawn = Pawn(1, 99)
# print(pawn.id)
# pawn.valid_movement(chess_board)

# print(len(chess_board))
# print(len(chess_board[0]))

