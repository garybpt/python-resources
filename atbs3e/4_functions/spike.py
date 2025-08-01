import time, sys # Imports the time and sys standard python libraries

try:
    while True: # The main programme loop which will run indefinitely
        for i in range(1, 9): # Draw lines with increasing length working up
            print('-' * (i * i)) # 1 x 1, 2 x 2, 3 x 3 etc. until it reaches 8 x 8
            time.sleep(0.1) # Sleeps for 0.1 seconds between loops
        
        for i in range(7, 1, -1): # Draw lines decreasing in length working down
            print('-' * (i * i)) # 7 x 7, 6 x 6, 5 x 5 etc. until it reaches 2 x 2
            time.sleep(0.1)
        
except KeyboardInterrupt:
    sys.exit()