from pathlib import Path
import numpy as np
import re

test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

#  Test Result:

# Read and extract input data
path = Path('input.txt')


# Parse into a list of lines
lines = path.read_text().splitlines()
# lines = test_data.splitlines()
# print(lines)




"""PART 1"""

# Create a numpy array

# Force the strings to lists
data = []
for line in lines:
    data.append(list(line))
#print(data)

# Creat numpy array from the list of lists
arr = np.array(data)
#print(f"arr = \n{arr}")

"""
Source:  https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
"""
# Get the diagonals (NW -> SE)
diags = [arr[::-1,:].diagonal(i) for i in range(-arr.shape[0]+1,arr.shape[1])]


# Add the diagonals (NE -> SW)
diags.extend(arr.diagonal(i) for i in range(arr.shape[1]-1,-arr.shape[0],-1))

# Get diagonal text, store in a list

diagonals = []
for diag in diags:
    s = "".join(diag.tolist())
    diagonals.append(s)

print(f"Diagonals:\n {diagonals}")

# Get horizontal text, store in a list
horizontals = lines
print(f"Horizontals: \n{horizontals}")

# Get vertical text, store in a list
verticals = []

for i, horizontal in enumerate(horizontals):
    vertical = ""
    for j, item in enumerate(horizontal):
        vertical += horizontals[j][i]
    verticals.append(vertical)
    #print(vertical)

print(f"Verticals: \n{verticals}")

# Use regex FINDALL for 'XMAS' in string
pattern = re.compile(r'XMAS')

# Make an uber list of all strings
all_strings = []
all_strings.extend(verticals)
all_strings.extend(horizontals)
all_strings.extend(diagonals)

# print(all_strings)

xmases = 0

for string in all_strings:
    xmases += len(pattern.findall(string))
    xmases += len(pattern.findall((string[::-1]))) # Reverse string

# print(xmases)

# Run regex 6 times (forwards and backwards on each list)
# Count instances per list, sum up


print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {xmases}")
print("--------------")



print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")