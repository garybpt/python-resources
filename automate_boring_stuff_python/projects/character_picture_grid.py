# This is a script which prints a heart using the 'O' and '.' symbols. 


# Define a 2D list (grid) representing a pattern or shape
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Iterate over the columns of the grid
for i in range(len(grid[0])):
    # Iterate over the rows of the grid
    for j in range(len(grid)):
        # Print the element at row j and column i without moving to the next line
        print(grid[j][i], end='')
    # Move to the next line after printing all elements in a column
    print()
