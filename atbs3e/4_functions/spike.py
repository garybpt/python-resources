import time, sys # Imports the time and sys standard python libraries

try:
    while True: # The main programme loop
        for i in range(1, 9): # Draw lines with increasing length
            print('-' * (i * i))
            time.sleep(0.1)
        
        for i in range(7, 1, -1): # Draw lines decreasing in length
            print('-' * (i * i))
            time.sleep(0.1)
        
except KeyboardInterrupt:
    sys.exit()