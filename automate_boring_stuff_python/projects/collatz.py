def collatz(number):
    if number % 2 == 0: # The % is a modulus/remainder operator. It will work out whether an integer is odd or even by calculating the remainder by dividing one number by the other and presenting what is left. For example 7 / 2 = 3 + 1 
        result = number // 2
    else:
        result = 3 * number + 1 # If there is a number left after the modulos/remainder then it is an odd number 

    print(result)
    return result


input_number = int(input("Enter a number: "))

try:
    while input_number != 1: # When the sum value is greater than 1 the loop will continue. It will only stop when 1 is achieved 
        input_number = collatz(input_number)

except ValueError:
    print("You must enter a number.")