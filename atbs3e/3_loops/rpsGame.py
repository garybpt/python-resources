import random, sys

print('ROCK', 'PAPER', 'SCISSORS')

# These variables keep track of the number of wins, losses, and draws

wins = 0
losses = 0
draws = 0

while True: # The main game loop
    print('%s Wins, %s Losses, %s Draws' % (wins, losses, draws))
    while True: # The player input loop - keeps looping until the player chooses r, p, s, or q
        print('Enter your move: (r)ock, (s)cissors, (p)aper, or (q)uit.')
        player_move = input('>')
        if player_move == 'q':
            sys.exit() # Quits the programme
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break #Break out of the player input loop and continue to comparison
        print('Type one of r, p, s, or q.')

    # Display what the player chose
    if player_move == 'r':
        print('ROCK versus... ')
    elif player_move == 'p':
        print('PAPER versus... ')
    elif player_move == 's':
        print('SCISSORS versus... ')

    # Display what the computer choses
    move_number = random.randint(1, 3) # The computer chooses a random integer between 1-3
    if move_number == 1:
        computer_move = 'r' # The integer is turned into a string for comparison later
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display and record the win\loss\draw
    if player_move == computer_move: # The two strings are compared with one another
        print('It is a draw!')
        draws = draws + 1 # A score is added to the appropriate counter based upon the comparison
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1