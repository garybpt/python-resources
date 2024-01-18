# This is a tac-tac-toe game

the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# ChatGPT function to check it there is a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    # Rows
    for row in ['top', 'mid', 'low']:
        if board[row + '-L'] == board[row + '-M'] == board[row + '-R'] == player:
            return True
    # Columns
    for col in ['L', 'M', 'R']:
        if board['top-' + col] == board['mid-' + col] == board['low-' + col] == player:
            return True
    # Diagonals
    if board['top-L'] == board['mid-M'] == board['low-R'] == player or \
       board['top-R'] == board['mid-M'] == board['low-L'] == player:
        return True
    return False

turn = 'X'

for i in range(9):
    # Prints out the board at the start of each new turn
    print_board(the_board)
    print('Turn for ' + turn + '. Move on which space?')

    # Gets the active player’s move
    move = input()

    # Updates the game board accordingly
    the_board[move] = turn

    # Check for a winner - ChatGPT addition
    if check_winner(the_board, turn):
        print('Player ' + turn + ' wins!')
        break

    # Swaps the active player
    if turn == 'X':
        turn = 'O'
    
    else:
        turn = 'X'

print_board(the_board)