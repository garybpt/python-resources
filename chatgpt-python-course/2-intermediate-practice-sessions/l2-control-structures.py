# TASK - Ask the user how old they are to test whether they're eligable to vote, then modify the script to loop it a desired number of times set by the user

count = input("For how many people would you like to check the voting age? ") # How many repetitions of questions does the user want
count = int(count) # Convert the number into an integer

for i in range(count): # "i" mean "iteration"
    eligibility = input("How old are you? ") # Ask the user how old they are
    eligibility = int(eligibility) # Convert the number into an integer

    if eligibility < 18: # The user is under 18
        print("You are not old enough to vote.")

    elif eligibility == 18: # The user is 18
        print("You are now old enough to vote")

    else: # The user is older than 18
        print("You are old enough to vote")