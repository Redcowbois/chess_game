###
#Setup
###

import pygame
from sys import exit 
from chess_pieces import *
from chess_board import Chess_Board
from random import random
pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

###
#Initial Game State
###
class Player():
    def __init__(self, team):
        self.team = team
        self.moves = []

if random() < 0.5:
    player = Player("5")
    game_board = Chess_Board.setup_chess_board(Chess_Board.chess_board_model_1)
    turn = 0
else: 
    player = Player("1")
    game_board = Chess_Board.setup_chess_board(Chess_Board.invert_board(Chess_Board.chess_board_model_1))
    turn = 1

chess_board_image = pygame.image.load('textures/board.png')

###
#Game Loop
###

new_changes = True
been_pressed = False
first_press = True

white_movement_board = [[0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0]]

black_movement_board = [[0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]

while True:
    mouse_row, mouse_col = pygame.mouse.get_pos()[0]//100, pygame.mouse.get_pos()[1]//100
    pressed = pygame.mouse.get_pressed()[0]

    #Checks which teams turn it is
    if turn % 2 == 0:
        team_turn = "5"
    else:
        team_turn = "1"
    #---

    #Checks if a piece is pressed 
    if pressed and first_press and game_board[mouse_col][mouse_row] != 0:
        original_position = (mouse_row, mouse_col)
        hovered_piece = game_board[mouse_col][mouse_row]

        if team_turn == hovered_piece.id[0]:
            first_press = False
            been_pressed = True
    #---

    #Checks if a piece is released and changes turn 
    if been_pressed and not pressed:
        
        if (mouse_col, mouse_row) in hovered_piece.valid_movement:
            game_board[original_position[1]][original_position[0]] = 0
            game_board[mouse_col][mouse_row] = hovered_piece
            hovered_piece.position = (mouse_col, mouse_row)

            if type(hovered_piece) in [Pawn, Rook, King]:
                hovered_piece.moved = True

        print(original_position[1], original_position[0], mouse_col, mouse_row)

        if (original_position[1], original_position[0]) != (mouse_col, mouse_row):
            turn += 1

        been_pressed = False
        first_press = True
        new_changes = True
        
    #---

    #Shows the valid piece movements
    click_event = pygame.event.get(pygame.MOUSEBUTTONDOWN)
    if click_event != [] and click_event[0].button == 1 and game_board[mouse_col][mouse_row] != 0:

        check_piece = game_board[mouse_col][mouse_row]
        check_piece.get_valid_movement(game_board, type(check_piece).__name__)
        #TEST#############################
        # print("white")
        # for a in white_movement_board:
        #     print(a)
        # print("black")
        # for b in black_movement_board:
        #     print(b)

        if team_turn == check_piece.id[0]:
            for row, col in check_piece.valid_movement:
                allowed_tiles = pygame.image.load("textures/allowed.png")
                window.blit(allowed_tiles, allowed_tiles.get_rect(topleft = (col*100, row*100)))

        if type(check_piece) == King and check_piece.checked:
                    checked_tile = pygame.image.load("textures/checked.png")
                    window.blit(checked_tile, checked_tile.get_rect(topleft = (mouse_row*100, mouse_col*100)))
    
    #---

    #Generates the board again if there are new changes 
    if new_changes:
        print("new changes run")
        window.blit(chess_board_image, (0,0))
        white_movement_board = [[0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0]]
        black_movement_board = [[0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0]]
        for i in range(8):
            for j in range(8):
                if game_board[j][i] == 0:
                    continue
                current_piece = game_board[j][i]

                #Updating the valid movements
                current_piece.get_valid_movement(game_board, type(current_piece).__name__)

                for row, col in current_piece.valid_movement:
                    if str(current_piece.id)[0] == "1":
                        black_movement_board[row][col] += 1
                    elif str(current_piece.id[0]) == "5":
                        white_movement_board[row][col] += 1
                #---

                #Checking for checks

                #Drawing the board
                if current_piece.id[6] == "1": #Pawn
                    if current_piece.id[0] == "1":
                        current_texture = pygame.image.load("textures/black_pawn.jpg")
                    elif current_piece.id[0] == "5":
                        current_texture = pygame.image.load("textures/white_pawn.jpg")

                elif current_piece.id[6] == "5": #Rook
                    if current_piece.id[0] == "1":
                        current_texture = pygame.image.load("textures/black_rook.jpg")
                    elif current_piece.id[0] == "5":
                        current_texture = pygame.image.load("textures/white_rook.jpg")

                elif current_piece.id[6] == "3": #Knight
                    if current_piece.id[0] == "1":
                        current_texture = pygame.image.load("textures/black_knight.jpg")
                    elif current_piece.id[0] == "5":
                        current_texture = pygame.image.load("textures/white_knight.jpg")

                elif current_piece.id[6] == "4": #Bishop
                    if current_piece.id[0] == "1":
                        current_texture = pygame.image.load("textures/black_bishop.jpg")
                    elif current_piece.id[0] == "5":
                        current_texture = pygame.image.load("textures/white_bishop.jpg")

                elif current_piece.id[6] == "9": #Queen
                    if current_piece.id[0] == "1":
                        current_texture = pygame.image.load("textures/black_queen.jpg")
                    elif current_piece.id[0] == "5":
                        current_texture = pygame.image.load("textures/white_queen.jpg")

                elif current_piece.id[6] == "2": #King 
                    if current_piece.id[0] == "1":
                        current_texture = pygame.image.load("textures/black_king.jpg")
                    elif current_piece.id[0] == "5":
                        current_texture = pygame.image.load("textures/white_king.jpg")

                elif current_piece.id[6] == "6": #TestPiece
                    current_texture = pygame.image.load("textures/white_pawn.jpg")

                window.blit(current_texture, current_texture.get_rect(topleft = (i*100+25, j*100+25)))
                #---
        new_changes = False
    #---

    #Exits the window:
    if pygame.event.get(eventtype=pygame.QUIT) != []:
        pygame.quit()
        exit()
    #---

    pygame.event.pump()
    pygame.display.update()
    clock.tick(60)
