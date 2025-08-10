import logging # This is the package the supports debugging

logging.basicConfig(filename='myProgrammeLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') # Sets the layout of debug messages
logging.debug('Start of programme')

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    # for i in range(n + 1): - This was the original, which presented an error. The range automatically starts at 0, which can't be used in multiplication
    for i in range(1, n + 1): # This is the updated code, which starts at 1
        total *= i # 1 × 2 × 3 × 4 × 5
        logging.debug('i is ' + str(i) + ', total is ' + str(total)) # Latter part to the message
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5)) # This value is assigned to 'n'
logging.debug('End of programme')