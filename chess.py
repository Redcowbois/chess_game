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

list_of_pieces = setup_chess_board(chess_board_model_2)
print(game_board)

###
#Game Loop
###

#initialize_game()

x = 0
y = 0
pressed = 0

test_piece = pygame.image.load('textures/pawn.jpg')
test_piece_rect = test_piece.get_rect(center = (x*100+50, y*100+50))

test_piece_dot = pygame.Surface((5, 5))
test_piece_dot_rect = test_piece_dot.get_rect(center = (150, 150))
test_piece_dot.fill("Red")

pawn = Pawn(1, 1)
print(pawn.id)


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
            for i in pawn.valid_movement(game_board):
                valid = pygame.Surface((50, 50))
                valid_rect = valid.get_rect(center = (i[0]*100+50, i[1]*100+50))
                valid.fill("Blue")
                window.blit(valid, valid_rect)
        else: 
            test_piece_rect.update((mouse_pos[0])//100*100+25, (mouse_pos[1])//100*100+25, 50, 50)
    
    window.blit(test_piece, test_piece_rect)
    window.blit(test_piece_dot, test_piece_dot_rect)

    for i in range(8):
        for j in range(8):
            if game_board[j][i] == 0:
                continue
            current_piece = str(game_board[j][i].id)

            if current_piece[6] == "1":
                if current_piece[0] == "1":
                    current_texture = pygame.image.load("textures/black_pawn.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))
                elif current_piece[0] == "5":
                    current_texture = pygame.image.load("textures/white_pawn.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))

            elif current_piece[6] == "5":
                if current_piece[0] == "1":
                    current_texture = pygame.image.load("textures/black_rook.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))
                elif current_piece[0] == "5":
                    current_texture = pygame.image.load("textures/white_rook.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))

            elif current_piece[6] == "3":
                if current_piece[0] == "1":
                    current_texture = pygame.image.load("textures/black_knight.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))
                elif current_piece[0] == "5":
                    current_texture = pygame.image.load("textures/white_knight.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))

            elif current_piece[6] == "4":
                if current_piece[0] == "1":
                    current_texture = pygame.image.load("textures/black_bishop.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))
                elif current_piece[0] == "5":
                    current_texture = pygame.image.load("textures/white_bishop.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))

            elif current_piece[6] == "9":
                if current_piece[0] == "1":
                    current_texture = pygame.image.load("textures/black_queen.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))
                elif current_piece[0] == "5":
                    current_texture = pygame.image.load("textures/white_queen.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))

            elif current_piece[6] == "2":
                if current_piece[0] == "1":
                    current_texture = pygame.image.load("textures/black_king.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))
                elif current_piece[0] == "5":
                    current_texture = pygame.image.load("textures/white_king.jpg")
                    window.blit(current_texture, current_texture.get_rect(topleft = (i*100, j*100)))

    pygame.display.update()
    clock.tick(144)
