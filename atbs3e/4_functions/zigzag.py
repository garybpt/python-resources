import time, sys # Import the relevant libraries
indent = 0 # How many spaces to indent
indent_increasing = True # Whether the indentation is increasing or not

try:
    while True: # The main programme loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for the 1/10th of a second

        if indent_increasing:
            # Increase the number of spaces
            indent = indent + 1
            if indent == 20:
                # Change direction when indent gets to 20
                indent_increasing = False
        else:
                # Decrease the number of spaces
                indent = indent - 1
                if indent == 0:
                    # Change direction again when indent gets back to 0
                    indent_increasing = True
except KeyboardInterrupt:
    sys.ext()