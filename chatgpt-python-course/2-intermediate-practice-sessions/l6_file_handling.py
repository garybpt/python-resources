with open("chatgpt-python-course/2-intermediate-practice-sessions/l6_sample.txt", "r") as file:
    input = file.read()  # Read the entire file as a string
    print(input) # Print the file's contents

with open("chatgpt-python-course/2-intermediate-practice-sessions/l6_output.txt", "w") as file:  # Open the file in write mode
    output = file.write("This Thursday, Gary and Alex are buying a house")  # Write data to the file
    print("Update complete")