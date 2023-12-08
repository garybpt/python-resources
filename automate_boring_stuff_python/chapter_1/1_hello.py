# This programme says hello and asks for your name

print("Hello, World")
print("What is your name?")

my_name = input()

print("It's great to meet you, " + my_name)

print("The length of your name is: ")
print(len(my_name))

# Ask for the user's age

print("What is your age?")

my_age = input()

print("You will be " + str(int(my_age) + 1) + " in 1 year.")

# Consolidating learning by adding my own section

print("Where are you from, " + my_name + "?")

my_location = input()

# Working with len()

print(len("Hello, World")) # 12

print(len("My very energetic monster just scarfed nachos.")) # 46

print(len("")) # 0