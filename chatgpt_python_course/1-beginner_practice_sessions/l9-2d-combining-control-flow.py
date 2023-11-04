number = input("Please enter any number. ")
number = int(number)

result = "Even" if number % 2 == 0 else "Odd"

if result == "Even":
    print("This is an even number")

else:
    print("This is an odd number")