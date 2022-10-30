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
                window.blit(current_piece, (col*100, row*100))

#initialize_game()

x = 0
y = 0
pressed = 0

test_piece = pygame.image.load('textures/pawn.jpg')
test_piece_rect = test_piece.get_rect(center = (x+50, y+50))

test_piece_dot = pygame.Surface((5, 5))
test_piece_dot_rect = test_piece_dot.get_rect(center = (150, 150))
test_piece_dot.fill("Red")

while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    test_piece_dot_rect.update(mouse_pos[0]-2.5, mouse_pos[1]-2.5, 10, 10)

    if test_piece_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            test_piece_rect.update(mouse_pos[0]-25, mouse_pos[1]-25, 50, 50)
        else: 
            test_piece_rect.update((mouse_pos[0])//100*100+25, (mouse_pos[1])//100*100+25, 50, 50)
    
    window.blit(chess_board_image, (0,0))
    window.blit(test_piece, test_piece_rect)
    window.blit(test_piece_dot, test_piece_dot_rect)

    pygame.display.update()
    clock.tick(60)
