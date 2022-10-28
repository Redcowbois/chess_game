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