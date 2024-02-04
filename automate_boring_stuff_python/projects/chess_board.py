# A function named is_valid_chess_board() that takes a dictionary argument and returns True or False depending on if the board is valid

def is_valid_chess_board(board):
    # Dictionary to keep track of the count of pieces for each player
    piece_count = {'bking': 0, 'wking': 0, 'bpawn': 0, 'wpawn': 0,
                   'bknight': 0, 'wknight': 0, 'bbishop': 0, 'wbishop': 0,
                   'brook': 0, 'wrook': 0, 'bqueen': 0, 'wqueen': 0}

    # Valid chess board positions
    valid_positions = set([f"{i}{j}" for i in range(1, 9) for j in 'abcdefgh'])

    for position, piece in board.items():
        # Check if the piece is in a valid position
        if position not in valid_positions:
            return False

        # Extract player colour and piece type
        colour, ptype = piece[0], piece[1:]

        # Check if the piece name is valid
        if colour not in ('b', 'w') or ptype not in ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king'):
            return False

        # Increment the piece count for the current player
        piece_count[f"{colour}{ptype}"] += 1

    # Check if each player has at most 16 pieces and at most 8 pawns
    for colour in ('b', 'w'):
        if sum(piece_count[f"{colour}{ptype}"] for ptype in ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king')) > 16:
            return False
        if piece_count[f"{colour}pawn"] > 8:
            return False

    # Check if exactly one black king and one white king are present
    if piece_count['bking'] != 1 or piece_count['wking'] != 1:
        return False

    # If all checks pass, the board is valid
    return True

# Example usage:
chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
result = is_valid_chess_board(chess_board)
print(result)