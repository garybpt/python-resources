# This is a programme which creates a valid chess board


# Setting up the starting chess board
chess_board =  {'a8': 'b_rook', 'b8': 'b_knight', 'c8': 'b_bishop', 'd8': 'b_queen', 'e8': 'b_king', 'f8': 'b_bishop', 'g8': 'b_knight', 'h8': 'b_rook',
                'a7': 'b_pawn', 'b7': 'b_pawn', 'c7': 'b_pawn', 'd7': 'b_pawn', 'e7': 'b_pawn', 'f7': 'b_pawn', 'g7': 'b_pawn', 'h7': 'b_pawn',
                'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',
                'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',
                'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ',
                'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ',
                'a2': 'w_pawn', 'b2': 'w_pawn', 'c2': 'w_pawn', 'd2': 'w_pawn', 'e2': 'w_pawn', 'f2': 'w_pawn', 'g2': 'w_pawn', 'h2': 'w_pawn',
                'a1': 'w_rook', 'b1': 'w_knight', 'c1': 'w_bishop', 'd1': 'w_king', 'e1': 'w_queen', 'f1': 'w_bishop', 'g1': 'w_knight', 'h1': 'w_rook'}


# Keeping this here just in case I need it (I don't think it will be needed)
chess_pieces =  {'black': 'b_king': {1, 'e8'}, 'b_queen': {1, 'd8'}, 'b_bishop': {2, 'c8', 'f8'}, 'b_rook': {2, 'a8', 'h8'}, 'b_knight': {2, 'b8', 'g8'}, 'b_pawn': {8, 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'},
                'white': 'w_king': {1, 'd1'}, 'w_queen': {1, 'e1'}, 'w_bishop': {2, 'c1', 'f1'}, 'w_rook': {2, 'a1', 'h1'}, 'w_knight': {2, 'b1', 'g1'}, 'w_pawn': {8, 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'}


# Printing the starter chess board just in case I need it (I don't think it will be needed)
def print_board(board):
    print(board['a8'] + '|' + board['b8'] + '|' + board['c8'] + '|' + board['d8'] + '|' + board['e8'] + '|' + board['f8'] + '|' + board['g8'] + '|' + board['h8'])
    print('-+-+-+-+-+-+-+-')
    print(board['a7'] + '|' + board['b7'] + '|' + board['c7'] + '|' + board['d7'] + '|' + board['e7'] + '|' + board['f7'] + '|' + board['g7'] + '|' + board['h7'])
    print('-+-+-+-+-+-+-+-')
    print(board['a6'] + '|' + board['b6'] + '|' + board['c6'] + '|' + board['d6'] + '|' + board['e6'] + '|' + board['f6'] + '|' + board['g6'] + '|' + board['h6'])
    print('-+-+-+-+-+-+-+-')
    print(board['a5'] + '|' + board['b5'] + '|' + board['c5'] + '|' + board['d5'] + '|' + board['e5'] + '|' + board['f5'] + '|' + board['g5'] + '|' + board['h5'])
    print('-+-+-+-+-+-+-+-')
    print(board['a4'] + '|' + board['b4'] + '|' + board['c4'] + '|' + board['d4'] + '|' + board['e4'] + '|' + board['f4'] + '|' + board['g4'] + '|' + board['h4'])
    print('-+-+-+-+-+-+-+-')
    print(board['a3'] + '|' + board['b3'] + '|' + board['c3'] + '|' + board['d3'] + '|' + board['e3'] + '|' + board['f3'] + '|' + board['g3'] + '|' + board['h3'])
    print('-+-+-+-+-+-+-+-')
    print(board['a2'] + '|' + board['b2'] + '|' + board['c2'] + '|' + board['d2'] + '|' + board['e2'] + '|' + board['f2'] + '|' + board['g2'] + '|' + board['h2'])
    print('-+-+-+-+-+-+-+-')
    print(board['a1'] + '|' + board['b1'] + '|' + board['c1'] + '|' + board['d1'] + '|' + board['e1'] + '|' + board['f1'] + '|' + board['g1'] + '|' + board['h1'])


# Function to assess whether the chess board and pieces are valid
def is_valid_chess_board():
    # First - Need assess whether the chess board dimensions are correct
    # Second - Need to make sure that the total number of pieces per player are correct (16)
    # Third - Need to make sure that the correct number of each piece is given to the player
    # Fourth - The programme needs to detect whether a piece is off the board