from pathlib import Path
import itertools
import math

test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

#  Test Result:

# Read and extract input data
path = Path('input.txt')


# Parse into a list of lines
# lines = path.read_text().splitlines()
lines = test_data.splitlines()
#print(lines[0])

"""PART 1"""

# Parse each line into a tuple:  (result, (tuple of terms))
calibrations = []
for line in lines:
    result = int(line.split(":")[0])
    terms = line.split(":")[1]
    terms_as_list = terms.split(" ")
    terms_as_list.pop(0)    # Get rid of leading space
    terms_as_ints = [int(x) for x in terms_as_list] # Convert to ints
    calibrations.append((result, terms_as_ints))

print(calibrations)


# Define a function that determines all possible combos of + and * for a tuple of terms
# Use Cartesian Product for this
# https://docs.python.org/3/library/itertools.html

def build_operators_list (list_length):
    """Returns a list of all combinations of + and *, for a given list length."""

    # We can represent '+' as 0 and '*' as 1
    # print(list(itertools.product(range(2),repeat=6)))
    combos = list(itertools.product(range(2),repeat=list_length))

    return combos


# Test
print(build_operators_list(3))




# Define a function that takes a list of possible operator combos...and works applies them somehow?!


print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")



print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")