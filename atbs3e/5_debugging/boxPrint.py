def box_print(symbol, width, height):
    if len(symbol) != 1: # The programme tests whether the symbol is one character or more
        raise Exception('Symbol must be single character.')
    if width <= 2: # The programme tests whether the width value is equal to or below 2, and if so, present an exception
        raise Exception('Width must be greater than 2.')
    if height <= 2: # The programme tests whether the height value is equal to or below 2, and if so, present an exception
        raise Exception('Height must be greater than 2.')
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

try:
    box_print('*', 4, 4)
    box_print('0', 20, 5)
    box_print('x', 1, 3)
    box_print('ZZ', 3, 3)
except Exception as err:
    print('An exception happened: ' + str(err))
try:
    box_print('ZZ', 3, 3)
except Exception as err:
    print('An exception happened: ' + str(err))