# Ask the user for the temperature
temp = input("What temperature is it where you are? ")
temp = int(temp)  # Convert the input to an integer

# Determine if it is cold, moderate, or hot
if temp < 0:
    print("It's Baltic!")
elif temp in range(0, 25 + 1):
    print("It's quite pleasent")
else:
    print("You must be melting!")