import json

# Creating an empty dictionary
my_dict = {}

# Creating a dictionary for a student register
student = {
    "id": "",
    "name": "",
    "age": "",
    "subject": ""
}

# Ask the user for their student id
id = input("What is your Student ID? ")
id = int(id)  # Convert the input to an integer

# Ask the user for their name
name = input("What is your full name? ")
name = str(name)  # Convert the input to a string

# Ask the user for their age
age = input("How old are you? ")
age = int(age)  # Convert the input to an integer

# Ask the user for their subject
subject = input("What are you studying? ")
subject = str(subject)  # Convert the input to a string

print("You have inputted: ", id, name, age, subject)