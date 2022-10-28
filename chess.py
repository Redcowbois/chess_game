###
#Setup
###

import pygame
from sys import exit 
from chess_pieces import *
pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess")

###
#Game Loop
###

def initialize_game():
    """() -> Nonetype
    Initializes the chess pieces
    """
    for row in range(8):
        for col in range(8):
            if chess_board[row][col] != 0: 
                current_piece = pygame.Surface((50, 50))
                current_piece.fill((58,171,137))
                window.blit(current_piece, (25+col*100, 25+row*100))

chess_board_image = pygame.image.load('textures/board.png')
window.blit(chess_board_image, (0, 0))
# initialize_game()

test_piece = pygame.image.load('textures/pawn.jpg')
test_piece_rect = test_piece.get_rect(topleft = (25, 25))
window.blit(test_piece, test_piece_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()

