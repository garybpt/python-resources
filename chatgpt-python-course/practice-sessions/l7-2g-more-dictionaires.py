import json
import os

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

# Define a filename for the user student record JSON file
STUDENT_RECORD = "chatgpt-python-course/practice-sessions/l7-2g-student-dictionary.json"

ID = int()  # Convert the input to an integer
NAME = str()  # Convert the input to an integer
AGE = int()  # Convert the input to an integer
SUBJECT = str()  # Convert the input to an integer

# Check if the JSON file already exists and load its contents
if os.path.isfile(STUDENT_RECORD):
    with open(STUDENT_RECORD, "r") as file:
        student_dictionary = json.load(file)
else:
    student_dictionary = {}

# Ask the user what they would like to do
ask = int(input("What would you like to do?\n\n(1) Add a student record\n(2) Search for a student record\n(3) List all records\n(4) Update student record\n(5) Delete student record\n(6) Exit\n\nPlease select an option: "))

if ask == 1: # Add a student record
    print("You picked to add a student record")

    # Ask the user for their student id
    id = input("What is your Student ID? ")

    # Ask the user for their name
    name = input("What is your full name? ")

    # Ask the user for their age
    age = input("How old are you? ")

    # Ask the user for their subject
    subject = input("What are you studying? ")

     # Create a dictionary for the new student
    student = {
        "ID": id,
        "NAME": name,
        "AGE": age,
        "SUBJECT": subject
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
    student_id = input("What Student ID would you like to search for? ")

    if student_id in student_dictionary:
        student = student_dictionary[student_id]
        print("ID: ", student["ID"])
        print("Name: ", student["NAME"])
        print("Age: ", student["AGE"])
        print("Subject: ", student["SUBJECT"])

    else:
        print("No student record exists.")

elif ask == 3: # List all records
    print("You picked to list all a student records")
    print(student_dictionary)

elif ask == 4: # Update student record
    print("You picked to update a student record")

    # Ask the user for their student id
    student_id = input("What is the Student ID of the student you would like to update? ")

    if student_id in student_dictionary: # Checking whether the student ID is in the dictionary and asking what they would like to update
        student = student_dictionary[student_id]

        choice = int(input("What would you like to update?\n\n(1) Name\n(2) Age\n(3) Subject\n"))

        if choice == 1:
            new_name = input("Enter the new name: ")
            student["NAME"] = new_name
        elif choice == 2:
            new_age = input("Enter the new age: ")
            student["AGE"] = new_age
        elif choice == 3:
            new_subject = input("Enter the new subject: ")
            student["SUBJECT"] = new_subject
        else:
            print("Invalid")

        # Update the student dictionary with the modified information
        student_dictionary[student_id] = student

        # Save the updated student dictionary to the JSON file
        save_json(student_dictionary)

        print("Student record updated successfully.")
    else:
        print("Student ID not found. Cannot update the record.")

elif ask == 5: # Delete student record
    print("You picked to delete a student record")

else: # Exit
    print("You chose to exit")