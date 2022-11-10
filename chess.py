###
#Setup
###

import pygame
from sys import exit 
from chess_pieces import *
pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess")

clock = pygame.time.Clock()

chess_board_image = pygame.image.load('textures/board.png')
window.blit(chess_board_image, (0, 0))


###
#Initial Game Pieces
###

class Pawn():
    def __init__(self, team, number):
        self.team = 1000000*team 
        self.number = 70000 + number*100
        self.piece_type = 1
        self.id = self.team + self.number + self.piece_type
    
    def valid_movement(self, board_matrix):
        valid_mouvement = []
        for row in range(len(board_matrix)):
            for col in range(len(board_matrix[row])):
                if self.id == board_matrix[row][col]:
                    if str(self.id)[0] == "1":
                        valid_mouvement.append((row-1, col))
        
        return valid_mouvement


###
#Game Loop
###

def initialize_game():
    """() -> Nonetype
    Initializes the chess pieces
    """
    for row in range(8):
        for col in range(8):
            if chess_board_model[row][col] != 0: 
                current_piece = pygame.Surface((50, 50))
                current_piece.fill((58,171,137))
                window.blit(current_piece, (col*100, row*100))

#initialize_game()

x = 0
y = 1
pressed = 0

test_piece = pygame.image.load('textures/pawn.jpg')
test_piece_rect = test_piece.get_rect(center = (x*100+50, y*100+50))

test_piece_dot = pygame.Surface((5, 5))
test_piece_dot_rect = test_piece_dot.get_rect(center = (150, 150))
test_piece_dot.fill("Red")

pawn = Pawn(1, 1)
print(pawn.id)

# for i in pawn.valid_movement(chess_board):
#         print(i)
#         valid = pygame.Surface((50, 50))
#         valid_rect = valid.get_rect(center = (i[0]*50, i[1]*50))
#         valid.fill("Blue")
#         window.blit(valid, valid_rect)

# print(pawn.valid_movement(chess_board))
# print((i[0]*100+50, i[1]*100+50))
# valid = pygame.Surface((50, 50))
# valid_rect = valid.get_rect(center = (i[0]*100+50, i[1]*100+50))
# valid.fill("Blue")
# window.blit(valid, valid_rect)

while True:
    window.blit(chess_board_image, (0,0))
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    test_piece_dot_rect.update(mouse_pos[0]-2.5, mouse_pos[1]-2.5, 10, 10)

    if test_piece_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            test_piece_rect.update(mouse_pos[0]-25, mouse_pos[1]-25, 50, 50)
            for i in pawn.valid_movement(chess_board_model):
                valid = pygame.Surface((50, 50))
                valid_rect = valid.get_rect(center = (i[0]*100+50, i[1]*100+50))
                valid.fill("Blue")
                window.blit(valid, valid_rect)
        else: 
            test_piece_rect.update((mouse_pos[0])//100*100+25, (mouse_pos[1])//100*100+25, 50, 50)
    
    window.blit(test_piece, test_piece_rect)
    window.blit(test_piece_dot, test_piece_dot_rect)

    pygame.display.update()
    clock.tick(144)
