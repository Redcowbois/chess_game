from dev_settings import *

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
class Player(): #Class for players
    def __init__(self, team):
        self.team = team
        self.moves = []

###########TESTING########
if white_side: #Original Board
    player = Player("5")
    enemy = Player("1")
    game_board = Chess_Board.setup_chess_board(BOARD) 

elif black_side:  #Inverted Board
    player = Player("1")
    enemy = Player("5")
    game_board = Chess_Board.setup_chess_board(Chess_Board.invert_board(BOARD))
###############
else: 
    if random() < 0.5: #Original Board
        player = Player("5")
        enemy = Player("1")
        game_board = Chess_Board.setup_chess_board(BOARD) 

    else:  #Inverted Board
        player = Player("1")
        enemy = Player("5")
        game_board = Chess_Board.setup_chess_board(Chess_Board.invert_board(BOARD))

turn = 0
chess_board_image = pygame.image.load('textures/board.png')

class Move(): #Class to keep track of past moves
    def __init__(self, before, after, piece_type, captured_piece): 
        self.before = before
        self.after = after
        self.type = piece_type
        self.captured = captured_piece
    
    def __str__(self):
        col_dict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
        start_coords = str(col_dict[self.before[1]]) + str(8-self.before[0])
        end_coords = str(col_dict[self.after[1]]) + str(8-self.after[0])
        if self.captured == 0:
            captured = "nothing"
        else: 
            captured = type(self.captured).__name__

        return "Moved " + type(self.type).__name__ + start_coords + "->" + end_coords +", took " + captured

    def undo_move(board, history): #Undos last move
        if history != []:
            move = history[-1]
            board[move.before[0]][move.before[1]] = move.type
            board[move.after[0]][move.after[1]] = move.captured
            history.pop(-1)

move_history = []


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

        if team_turn == hovered_piece.id[0] or not has_turns:
            first_press = False
            been_pressed = True
    #---

    #Checks if a piece is released and changes turn 
    if been_pressed and not pressed:
        
        if (mouse_col, mouse_row) in hovered_piece.valid_movement:
            game_board[original_position[1]][original_position[0]] = 0
            taken_piece = game_board[mouse_col][mouse_row]
            game_board[mouse_col][mouse_row] = hovered_piece
            hovered_piece.position = (mouse_col, mouse_row)

            if type(hovered_piece) in [Pawn, Rook, King]:
                hovered_piece.moved = True

        if (original_position[1], original_position[0]) != (mouse_col, mouse_row) and (mouse_col, mouse_row) in hovered_piece.valid_movement:
            turn += 1
            move_history.append(Move((original_position[1], original_position[0]), (mouse_col, mouse_row), hovered_piece, taken_piece))
        ###########
        # print("move history", move_history)

        # for i in move_history:
        #     print(i.__str__())
        ########
        been_pressed = False
        first_press = True
        new_changes = True
        
    #---

    #Shows the valid piece movements
    click_event = pygame.event.get(pygame.MOUSEBUTTONDOWN)
    if click_event != [] and click_event[0].button == 1 and game_board[mouse_col][mouse_row] != 0:

        check_piece = game_board[mouse_col][mouse_row]

        #TEST#############################
        # print("white board")
        # print_board(white_movement_board)
        print("black board")
        print_board(black_movement_board)
        print("---------")
        print(check_piece.__str__(), "movement", check_piece.valid_movement)
        print(check_piece.__str__(), "attack", check_piece.valid_attack)

        if type(check_piece) == Test:
            for i in move_history:
                print(i.__str__())
        
        if type(check_piece) == Test2:
            Move.undo_move(game_board, move_history)
        ################

        if team_turn == check_piece.id[0] or not has_turns:
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
                
                if type(current_piece) != King:
                    current_piece.get_valid_movement(game_board, type(current_piece).__name__)

                for row, col in current_piece.valid_attack: #Drawing movement board
                    if str(current_piece.id)[0] == "1":
                        black_movement_board[row][col] += 1
                    elif str(current_piece.id[0]) == "5":
                        white_movement_board[row][col] += 1
                
                if type(current_piece) == King and current_piece.id[0] == "5":
                    white_king_pos = (j, i)
                if type(current_piece) == King and current_piece.id[0] == "1":
                    black_king_pos = (j, i)
            
                #---

                #Checking for checks

        if white_king_pos != -1:
            game_board[white_king_pos[0]][white_king_pos[1]].get_valid_movement(game_board, "King", black_movement_board)
        if black_king_pos != -1:      
            game_board[black_king_pos[0]][black_king_pos[1]].get_valid_movement(game_board, "King", white_movement_board)
        
        #Loading Piece Textures/Redrawing the board
        for i in range(8):
            for j in range(8):
                    
                if game_board[j][i] == 0:
                    continue
                current_piece = game_board[j][i]

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
