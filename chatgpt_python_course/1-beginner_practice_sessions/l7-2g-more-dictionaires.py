import json
import os

# Function to save the student dictionary to a JSON file
def save_json(student_dictionary):
    with open(STUDENT_RECORD, "w") as file:
        json.dump(student_dictionary, file, indent=4)

# Function to load the student dictionary from a JSON file
def open_json():
    if os.path.exists(STUDENT_RECORD):
        with open(STUDENT_RECORD, "r") as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return {}
    else:
        return {}

# Define a filename for the student record JSON file
STUDENT_RECORD = "/Users/garybutterfield/GitHub/python-resources/chatgpt_python_course/1-beginner_practice_sessions/l7-2g-student-dictionary.json"

# Load the existing student dictionary or create an empty one
student_dictionary = open_json()

while True:
    print("\nWelcome to the Student Database!\n")
    print("1. Add Student\n2. Search Student\n3. List Students\n4. Update Student\n5. Delete Student\n6. Exit\n")

    choice = input("Please select an option: ")

    if choice == "1": # Add a student record
        print("\nYou chose to add a student record\n")

        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        subject = input("Enter Student Subject: ")

        student = {
            "ID": student_id,
            "NAME": name,
            "AGE": age,
            "SUBJECT": subject
        }

        student_dictionary[student_id] = student
        save_json(student_dictionary)

        print("Student record added successfully.")

    elif choice == "2": # Search for a student record
        print("\nYou chose to search for a student record\n")

        student_id = input("Enter Student ID to search: ")

        if student_id in student_dictionary:
            student = student_dictionary[student_id]
            print("ID:", student["ID"])
            print("Name:", student["NAME"])
            print("Age:", student["AGE"])
            print("Subject:", student["SUBJECT"])
        else:
            print("Student record not found.")

    elif choice == "3": # List all records
        print("\nYou chose to list all student records\n")

        for student_id, student in student_dictionary.items():
            print(f"ID: {student_id}, Name: {student['NAME']}, Age: {student['AGE']}, Subject: {student['SUBJECT']}")

    elif choice == "4": # Update student record
        print("\nYou chose to update a student record\n")

        student_id = input("Enter Student ID to update: ")

        if student_id in student_dictionary:
            student = student_dictionary[student_id]

            print("What would you like to update?")
            print("1. Name\n2. Age\n3. Subject")
            update_choice = input("Enter your choice: ")

            if update_choice == "1":
                new_name = input("Enter the new name: ")
                student["NAME"] = new_name
            elif update_choice == "2":
                new_age = input("Enter the new age: ")
                student["AGE"] = new_age
            elif update_choice == "3":
                new_subject = input("Enter the new subject: ")
                student["SUBJECT"] = new_subject
            else:
                print("Invalid choice.")

            student_dictionary[student_id] = student
            save_json(student_dictionary)
            print("Student record updated successfully.")
        else:
            print("Student ID not found. Cannot update the record.")

    elif choice == "5": # Delete student record
        print("\nYou chose to delete a student record\n")

        student_id_to_delete = input("Enter Student ID to delete: ")

        if student_id_to_delete in student_dictionary:
            del student_dictionary[student_id_to_delete]
            save_json(student_dictionary)
            print(f"Student record with ID {student_id_to_delete} has been deleted.")
        else:
            print("Student ID not found. Cannot delete the record.")

    elif choice == "6": # Exit
        print("\nExiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")