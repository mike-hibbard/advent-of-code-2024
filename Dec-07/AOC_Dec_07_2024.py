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

    # Convert 0/1 to +/*
    operator_combos = []

    for combo in combos:

        operator_combo = ""

        for item in combo:
            if item == 0:
                operator_combo += '+'
            elif item == 1:
                operator_combo += '*'
    
        operator_combos.append(operator_combo)
        
    return operator_combos


# Test
# print(build_operators_list(2))

# Use 'eval' to evaluate the string
"""
print(eval('10*19'))
print(f"81+40*27 = {eval('81+40*27')}")
print(f"81*40+27 = {eval('81*40+27')}")
print(f"(81+40)*27 = {eval('(81+40)*27')}")
"""

"""
3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27
"""



def build_expression(factors, operator_combo):
    """Returns a string built from the factors + operators"""

    operator_combo += " " # Number of combos is 1 less than the number of factors

    string = ""
    
    for i in range(len(factors)):
        string += str(factors[i])
        string += operator_combo[i]
    
    return string[:-1]   # Remove trailing space
    #print(string)

# Test
build_expression([81, 40, 27], '+*')

# TODO add in parentheses



# Define a function that takes a list of possible operator combos...and works applies them somehow?!
def calculate_answers(factors):
    """Returns the list of possible answers for the factors"""


    operator_combos = list(build_operators_list(len(factors)-1))
    #operator_combos += " " # Number of combos is 1 less than the number of factors

    expressions = []
    
    for i in range(len(factors)):
        expressions.append(build_expression(factors, operator_combos[i]))
    
    print(expressions)
    return expressions
    


# Test
answers = calculate_answers([81, 40, 27])
for answer in answers:
    print(f"{answer} = {eval(answers[0])}")



print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")



print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")