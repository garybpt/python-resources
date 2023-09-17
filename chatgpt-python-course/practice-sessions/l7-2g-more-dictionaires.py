import json

def save_json():
    with open("student_dictionary.json", "w") as write_file:
        json.dump(student_dictionary, write_file)

def open_json():
    with open("student_dictionary.json", "r") as read_file:
        data = json.load(read_file)

# I think the user interface could be achieved using an if/elif/else statement

open_json # More needs to this to make it work

# Creating an empty dictionary
student_dictionary = {}

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

save_json(student_dictionary) # More needs to this to make it work