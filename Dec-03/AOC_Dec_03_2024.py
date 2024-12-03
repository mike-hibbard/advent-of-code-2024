from pathlib import Path
import re

test_data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

# Test Result = 161 (2*4 + 5*5 + 11*8 + 8*5)

# Read and extract input data
path = Path('input.txt')

# Parse into a list of lines
# lines = path.read_text().splitlines()
lines = test_data.splitlines()
# print(lines[0])

"""PART 1"""

# Create a regex for the pattern
def mul_regex(input_text):
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    return pattern.findall(input_text)

# Tests
test_string = "mul(1,234)"
print(mul_regex(test_string))
print(mul_regex(test_data))

# Parse input string, build a list of tuples (discard 'mul')
# Write a multiply function that takes in a tuple as an arg
# Write a loop to call multiply and sum up a total




print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")




print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")