# This is a programme which creates a valid chess board

# Setting up the starting chess board
chess_board =  {'a8': ' ', 'b8': ' ', 'c8': ' ', 'd8': ' ', 'e8': ' ', 'f8': ' ', 'g8': ' ', 'h8': ' ',
                'a7': ' ', 'b7': ' ', 'c7': ' ', 'd7': ' ', 'e7': ' ', 'f7': ' ', 'g7': ' ', 'h7': ' ',
                'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',
                'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',
                'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ',
                'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ',
                'a2': ' ', 'b2': ' ', 'c2': ' ', 'd2': ' ', 'e2': ' ', 'f2': ' ', 'g2': ' ', 'h2': ' ',
                'a1': ' ', 'b1': ' ', 'c1': ' ', 'd1': ' ', 'e1': ' ', 'f1': ' ', 'g1': ' ', 'h1': ' '}

chess_pieces =  {'black': {'b_king': 1, 'b_queen': 1, 'b_bishop': 2, 'b_rook': 2, 'b_knight': 2, 'b_pawn': 8},
                 'white': {'w_king': 1, 'w_queen': 1, 'w_bishop': 2, 'w_rook': 2, 'w_knight': 2, 'w_pawn': 8}}

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

