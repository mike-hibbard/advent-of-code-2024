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
# Get direction
# Start walking
# Identify blocks
# Logic to turn right
# Logic to write X in prior space after every move

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


print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")



print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")