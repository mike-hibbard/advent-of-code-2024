from pathlib import Path
import re

test_data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

# Test Result = 161 (2*4 + 5*5 + 11*8 + 8*5)

# Read and extract input data
path = Path('input.txt')

# Parse into a list of lines
lines = path.read_text()
# lines = test_data
# print(lines[0])

"""PART 1"""

# Create a regex for the pattern
def mul_regex(input_text):
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    return pattern.findall(input_text)

# Parse input string, build a list of tuples (discard 'mul')
# Create a regex to turn 'mul(x, y)' into a tuple (x, y)
def tuple_regex(input_text):
    pattern = re.compile(r'\d+')
    factors = pattern.findall(input_text)
    return (int(factors[0]), int(factors[1]))


# Tests
#test_string = "mul(1,234)"
#test_tuple_string = '(11,8)'
# muls = (mul_regex(test_data))
# print(muls)

muls = (mul_regex(lines))

tuples = []
for mul in muls:
    tuples.append(tuple_regex(mul))

print(tuples)


# Write a multiply function that takes in a tuple as an arg
def multiply(tuple):
    return tuple[0] * tuple[1]

# print(multiply((11, 8)))

# Write a loop to call multiply and sum up a total
part_one_total = 0

for tuple in tuples:
    product = multiply(tuple)
    part_one_total += product


print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {part_one_total}")
print("--------------")


"""PART 2"""
test_data2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# Test result = 48 (2*4 + 8*5)


# Implement a regex that matches don't*do  
# Use re.sub to replace matches with 'do' (in effect, removing the don't muls)
def remove_dont_muls(input_text):
    return re.sub(r"don't(.)*do(?!n't)", "do", input_text)

# Test

print(test_data2)
test_data2_donts_removed = remove_dont_muls(test_data2)
print(test_data2_donts_removed)

# muls2 = (mul_regex(test_data2_donts_removed))
muls2 = (mul_regex(remove_dont_muls(lines)))

tuples = []
for mul in muls2:
    tuples.append(tuple_regex(mul))

# print(tuples)


# Re-run the sum of muls on the resulting string
part_two_total = 0

for tuple in tuples:
    product = multiply(tuple)
    part_two_total += product

print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {part_two_total}")
print("--------------")