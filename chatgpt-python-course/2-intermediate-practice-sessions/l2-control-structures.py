loops = input("For how many people would you like to check the voting age? ") # How many repetitions of questions does the user want
loops = int(loops) # Convert the number into an integer

age = input("How old are you? ") # Ask the user how old they are
age = int(age) # Convert the number into an integer

if age < 18: # The user is under 18
    print("You are not old enough to vote.")

elif age == 18: # The user is 18
    print("You are now old enough to vote")

else: # The user is older than 18
    print("You are old enough to vote")