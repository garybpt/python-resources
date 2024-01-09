print('How many cats do you have?')
num_cats = input()

try:
    if int(num_cats) >= 4:
        print("That's a whole lot of cats!")
    elif int(num_cats) <=0:
        print("Why don't you have any cats?")
    else:
        print("That's not many cats.")
except ValueError:
    print("You need to use numbers.")