# Basically the minesweeper game without the thrill of clicking stuff

# --- Import modules ---
import copy
import random

grid_template = [
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
]

# --- Define Functions ---

def load_grid():
    '''
    Return a grid from the template with randomised bombs in random positions.
    Could add difficulty as a future feature (take user input to adjust the top 
    range of the randomisation)
    '''
    new_grid = copy.deepcopy(grid_template)
    # Enumerate to get index positions of elements
    for row_i, new_row in enumerate(new_grid):
        for col_i in range(len(new_row)):
            random_int = random.randint(0, 4)
            if random_int == 2:
                new_grid[row_i][col_i] = "#"

    return new_grid


def check_bomb(row_start, col_start):
    '''
    Starts at the input index row and column position in the grid and counts 
    all bombs in the surrounding 8 spaces, returning the number of bombs in 
    string format 
    '''
    bomb_count = 0
    for i in range(-1, 2):
        row = row_start
        row += i
        # If the row is -1, it will count backwards - the last row in the grid
        # To bypass this, skip index -1 since it is out of bounds
        if row < 0:
            continue
        for ii in range(-1, 2):
            col = col_start
            col += ii
            # Once again, to avoid backwards iteration of the column, ignore
            # index -1
            if col < 0:
                continue
            try:
                checked = grid[row][col]
                if checked == "#":
                    bomb_count += 1
            # Avoiding code breaks due to indexing errors
            except IndexError:
                continue

    return str(bomb_count)

def get_bombs():
    '''
    Returns the numbered grid after calling the check_bombs() function internally.
    '''
    number_grid = copy.deepcopy(grid)
    # Enumerate to get index position of element in grid
    for row_index, row in enumerate(grid, 0):
        for col_index, col in enumerate(row, 0):
            # Skip all the bombs
            if col != "#":
                col = check_bomb(row_index, col_index)
                # Replace the '-' in the number_grid with the number of bombs
                # surrounding it
                number_grid[row_index][col_index] = col

    return number_grid

# --- Functional Program code ---

grid = load_grid()
uncover_grid = get_bombs()

print("Buried bombs:")
for row_g in grid:
    print(row_g)

print("\nUncovered bombs:")
for row_u in uncover_grid:
    print(row_u)
