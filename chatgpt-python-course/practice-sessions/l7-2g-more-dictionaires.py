import json
import os

# Define a filename for the user student record JSON file
# os.path.isfile = 
STUDENT_RECORD = "chatgpt-python-course/practice-sessions/l7-2g-student-dictionary.json"

# Check if the JSON file already exists and load its contents
if os.path.isfile(STUDENT_RECORD):
    with open(STUDENT_RECORD, "r") as file:
        student_dictionary = json.load(file)
else:
    student_dictionary = {}

def save_json(student_dictionary):
    with open(STUDENT_RECORD, "w") as file:
        json.dump(student_dictionary, file, indent=4) # indent=4 prints entries on new lines in the json file

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

# open_json() # More needs to this to make it work

# Ask the user what they would like to do
ask = int(input("What would you like to do?\n\n(1) Add a student record\n(2) Search for a student record\n(3) List all records\n(4) Update student record\n(5) Delete student record\n(6) Exit\n\nPlease select an option: "))

if ask == 1: # Add a student record
    print("You picked to add a student record")

    # Ask the user for their student id
    id = input("What is your Student ID? ")
    id = int(id)  # Convert the input to an integer

    # Ask the user for their name
    name = input("What is your full name? ")
    name = str(name)  # Convert the input to an integer

    # Ask the user for their age
    age = input("How old are you? ")
    age = int(age)  # Convert the input to an integer

    # Ask the user for their subject
    subject = input("What are you studying? ")
    subject = str(subject)  # Convert the input to an integer

     # Create a dictionary for the new student
    student = {
        "id": id,
        "name": name,
        "age": age,
        "subject": subject
    }
    
    # Add the new student to the student dictionary
    student_dictionary[id] = student

    # Save the updated student dictionary to the JSON file
    save_json(student_dictionary)

    print("You have successfully added:\n\n", id, "\n", name, "\n", age, "\n", subject)
    save_json(student_dictionary) # More needs to this to make it work

elif ask == 2: # Search for a student record
    print("You picked to search for a student record")

    # Ask the user for their student id
    id = input("What Student ID would you like to search for? ")
    id = int(id)  # Convert the input to an integer

    if student in student_dictionary

    else:
        print("No sydent record exists.")

elif ask == 3: # List all records
    print("You picked to list all a student records")
    print(student_dictionary)

elif ask == 4: # Update student record
    print("You picked to update a student record")

elif ask == 5: # Delete student record
    print("You picked to delete a student record")

else: # Exit
    print("You chose to exit")