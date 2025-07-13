import sys

while True:
    print('Type exit to exit.')
    response = input() # If anything other than "exit" is inputted then the loop will always continue
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')