from pathlib import Path

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
# lines = path.read_text().splitlines()
lines = test_data.splitlines()
# print(lines)

"""PART 1"""

# Get horizontal text, store in a list
horizontals = lines
print(horizontals)

# Get vertical text, store in a list
verticals = []

for i, horizontal in enumerate(horizontals):
    vertical = ""
    for j, item in enumerate(horizontal):
        vertical += horizontals[j][i]
    verticals.append(vertical)
    print(vertical)

# print(verticals)


# Get diagonal text, store in a list
# Use regex FINDALL for 'XMAS' in string
# Run regex 6 times (forwards and backwards on each list)
# Count instances per list, sum up


print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")



print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")