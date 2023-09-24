import json
import os

# Define a filename for the user student record JSON file
STUDENT_RECORD = "/Users/garybutterfield/python-tutorial/chatgpt-python-course/practice-sessions/l7-2g-student-dictionary.json"

def save_json():
    with open(STUDENT_RECORD, "w") as file:
        json.dump(student_dictionary, file)

def open_json():
    if os.path.exists(STUDENT_RECORD):
        with open(STUDENT_RECORD, "r") as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                # Handle the case where the file is empty or contains invalid JSON
                return {}
    else:
        return {}

open_json() # More needs to this to make it work

# Open dictionary
student_dictionary = open_json()

# Creating a dictionary for a student register
student = {
    "id": "",
    "name": "",
    "age": "",
    "subject": ""
}

# I think the user interface could be achieved using an if/elif/else statement

# Ask the user what they would like to do
ask = input("What would you like to do?/n/n(1) Add a student record/n(2)Seaarch for a student record/n(3)List all records/n(4)Update student record/n(5)Delete student record/n(6)Exit/n/nPlease select and option ")
ask = int(ask)  # Convert the input to an integer

if ask == 1:
    print("You picked to add a student record")
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
    print("You have added: ", id, name, age, subject)
    save_json(student_dictionary, id, name, age, subject) # More needs to this to make it work

elif ask == 2:
    print("You picked to search for a student record")

elif ask == 3:
    print("You picked to list all a student records")

elif ask == 4:
    print("You picked to update a student record")

elif ask == 5:
    print("You picked to delete a student record")

else:
    print("You chose to exit")