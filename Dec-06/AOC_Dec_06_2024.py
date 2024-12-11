from pathlib import Path

test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

#  Test Result:

# Read and extract input data
path = Path('input.txt')


# Parse into a list of lines
# lines = path.read_text().splitlines()
lines = test_data.splitlines()
# print(lines[0])

"""PART 1"""

# Split input text into an array (numpy?)
grid =[]
for line in lines:
    grid.append(list(line))

def print_grid(grid):
    for row in grid:
        print(row)

print_grid(grid)

# Get start point
def find_start_position(grid):
    
    start_row = 0
    start_col = 0

    for i, row in enumerate(grid):
        if '^' in row:
            start_row = i

    for j, col in enumerate(grid[start_row]):
        if col == '^':
            start_col = j

    return (start_row, start_col)

print(f"start position: {find_start_position(grid)}")

def take_step(row, col, direction):

    # Walk East
    if direction == 'E':
        col +=1

    if direction == 'W':
        col -=1

    if direction == 'S':
        row +=1
    
    if direction == 'N':
        row -=1
    
    return(row, col)

# Identify blocks
def obstacle_found(grid, row, col, direction):
    if direction == 'E':
        if grid[row][col+1] == '#':
            return True

    if direction == 'W':
        if grid[row][col-1] == '#':
            return True

    if direction == 'S':
        if grid[row+1][col] == '#':
            return True
    
    if direction == 'N':
        if grid[row-1][col] == '#':
            return True
    
    else:
        return False

# Logic to turn right
def get_next_direction(direction):
    if direction == 'E':
        return 'S'

    if direction == 'W':
        return 'N'

    if direction == 'S':
        return 'W'
    
    if direction == 'N':
        return 'E'
    

# Start walking

# Get direction

# Logic to write X in prior space after every move


print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")



print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")