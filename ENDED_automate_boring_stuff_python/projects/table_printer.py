# Python3
# A simple programme that takes a list of lists of strings and displays them in a well-organised table with each column right-justified

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table():
    # Step 1 - Initialise column_widths to store the maximum column widths of each column
    column_widths = [0] * len(table_data)

    # Step 2 - Finding the maximum width of each culumn
    for i in range(len(table_data)): # Iterates over each inner list
        for j in range(len(table_data[i])): # Iterates over each element in the inner lists
            if len(table_data[i][j]) > column_widths[i]: # Check if the length of the current elemenent is greater than the stored width
                column_widths[i] = len(table_data[i][j]) # Update the width if the currrent element is wider
            
    # Step 3 - Printing the table
    for i in range(len(table_data[0])): # Iterate over each row
        for j in range(len(table_data)): # Iterate over each column
            print(table_data[j][i].rjust(column_widths[j]), end=' ') # Print each element right-justified with the appropriate width
        print() # Move to the next line after printing each row

print_table()