# The collatz sequence will work any number down to a value of 1

def collatz():
    try:
        num = int(input('Please type a whole number > '))
        print(num) # PRints the starting num first
        while num != 1: # Loops whilst num is greater than 1
            if num % 2 == 0:
                result = num // 2 # If an even number the function will divide it until it get to 1
                num = result # Updates the num variable
                    
            else:
                result = 3 * num + 1 # If an even number the function will times it by 3 then add 1 to make it even
                num = result

            print(result)

    except ValueError:
        print('Enter a whole number please.')

collatz()