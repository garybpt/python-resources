age = input("How old are you? ")
age = int(age)

if age < 18:
    print("You are a minor.")

elif age == 18:
    print("You are 18.")

else:
    print("You are an adult.")