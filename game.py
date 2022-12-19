###
#Setup
###

import pygame
from sys import exit 
from chess_pieces import *
from chess_board import *
pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

###
#Initial Game State
###
chess_board_image = pygame.image.load('textures/board.png')
game_board = setup_chess_board(chess_board_model_1)
# print(game_board)


###
#Game Loop
###

new_changes = True
been_pressed = False
first_press = True

while True:
    mouse_row, mouse_col = pygame.mouse.get_pos()[0]//100, pygame.mouse.get_pos()[1]//100
    pressed = (True in pygame.mouse.get_pressed())

    #Checks if a piece is pressed 
    if pressed and first_press and game_board[mouse_col][mouse_row] != 0:
        original_position = (mouse_row, mouse_col)
        hovered_piece = game_board[mouse_col][mouse_row]
        first_press = False
        been_pressed = True
    #---

    #Checks if a piece is released 
    if been_pressed and not pressed:
        
        game_board[original_position[1]][original_position[0]] = 0
        game_board[mouse_col][mouse_row] = hovered_piece
        hovered_piece.position = (mouse_col, mouse_row)

        if type(hovered_piece) == Pawn and original_position != (hovered_piece.position[1], hovered_piece.position[0]):
            hovered_piece.moved = True

        been_pressed = False
        first_press = True
        new_changes = True
        new_changes_for_hover = True
    #---

    #Shows the valid piece movements
    if pygame.event.get(pygame.MOUSEBUTTONDOWN) != []:
        if game_board[mouse_col][mouse_row] != 0:
            check_piece = game_board[mouse_col][mouse_row]
            check_piece.get_valid_movement(game_board)
            
            for row, col in check_piece.valid_movement:
                test = pygame.Surface((50, 50))
                test.fill('Red')
                window.blit(test, test.get_rect(topleft = (col*100+25, row*100 + 25)))
    #---

    #Generates the board again if there are new changes 
    if new_changes:
        window.blit(chess_board_image, (0,0))
        for i in range(8):
            for j in range(8):
                if game_board[j][i] == 0:
                    continue
                current_piece = str(game_board[j][i].id)

                if current_piece[6] == "1": #Pawn
                    if current_piece[0] == "1":
                        current_texture = pygame.image.load("textures/black_pawn.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))
                    elif current_piece[0] == "5":
                        current_texture = pygame.image.load("textures/white_pawn.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))

                elif current_piece[6] == "5": #Rook
                    if current_piece[0] == "1":
                        current_texture = pygame.image.load("textures/black_rook.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))
                    elif current_piece[0] == "5":
                        current_texture = pygame.image.load("textures/white_rook.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))

                elif current_piece[6] == "3": #Knight
                    if current_piece[0] == "1":
                        current_texture = pygame.image.load("textures/black_knight.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))
                    elif current_piece[0] == "5":
                        current_texture = pygame.image.load("textures/white_knight.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))

                elif current_piece[6] == "4": #Bishop
                    if current_piece[0] == "1":
                        current_texture = pygame.image.load("textures/black_bishop.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))
                    elif current_piece[0] == "5":
                        current_texture = pygame.image.load("textures/white_bishop.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))

                elif current_piece[6] == "9": #Queen
                    if current_piece[0] == "1":
                        current_texture = pygame.image.load("textures/black_queen.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))
                    elif current_piece[0] == "5":
                        current_texture = pygame.image.load("textures/white_queen.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))

                elif current_piece[6] == "2": #King 
                    if current_piece[0] == "1":
                        current_texture = pygame.image.load("textures/black_king.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))
                    elif current_piece[0] == "5":
                        current_texture = pygame.image.load("textures/white_king.jpg")
                        window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))
        new_changes = False
    #---

    #Exits the window:
    if pygame.event.get(eventtype=pygame.QUIT) != []:
        pygame.quit()
        exit()
    #---

    pygame.display.update()
    clock.tick(60)
