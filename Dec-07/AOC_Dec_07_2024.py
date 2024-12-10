from pathlib import Path
import itertools
import math
import re

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

# Test
# print(calibrations)


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
    
    string =  string[:-1]   # Remove trailing space

    #TODO Handle parentheses - only needed if both + and * present
    #if '+' in string and '*' in string:
        

    return string   
    #print(string)

# Test
# build_expression(lines[1][1], '+*')


def build_expression_as_list(factors, operator_combo):
    """Returns a list built from the factors + operators"""

    operator_combo += " " # Number of combos is 1 less than the number of factors

    expression_as_list = []
    
    for i in range(len(factors)):
        expression_as_list.append(str(factors[i]))
        expression_as_list.append(operator_combo[i])
    
    expression_as_list.pop()  # Remove trailing space

    #TODO Handle parentheses - only needed if both + and * present
    #if '+' in string and '*' in string:
        
    print(expression_as_list)
    return expression_as_list   

# Test
build_expression_as_list(calibrations[1][1],'**')

# Define a function that does eval L -> R
def evaluate_expression_left_to_right(expression_as_list):
    """Returns the answer of the expression with left-to-right calcuation"""

    total = 0
    term = ""

    while len(expression_as_list) >= 0:
        term_pattern = re.compile(r"[0-9]*[+*]{1}[0-9]+")
        if re.match(term_pattern, term):
            if total == 0:
                total = eval(term)
            else:
                total += eval(f'{total}{term}')
            term = ""
        
        elif len(expression_as_list) == 0:
            break
        
        else:
            term += expression_as_list.pop(0)

    print(total)

# Test
evaluate_expression_left_to_right(['81', '*', '40', '*', '27'])
evaluate_expression_left_to_right(['11', '+', '6', '*', '16', '+', '20'])


# Define a function that takes a list of possible operator combos...and works applies them somehow?!
def calculate_answers(factors):
    """Returns the list of possible answers for the factors"""


    operator_combos = list(build_operators_list(len(factors)-1))
    #operator_combos += " " # Number of combos is 1 less than the number of factors

    expressions = []
    
    for i in range(len(operator_combos)):
        expressions.append(build_expression(factors, operator_combos[i]))
    
    print(expressions)
    return expressions
    


# Test
"""
answers = calculate_answers([81, 40, 27])
for answer in answers:
    print(f"{answer} = {eval(answer)}")
"""

# Define a function to take in a tuple, calc expressions and check if answer exists
def check_answers(calibration):
    """Returns true if the stated answer is found in the list of calculated answers"""

    stated_answer = calibration[0] # Parse our the stated answer
    factors = calibration[1]    # Parse out the factors
    #print(stated_answer)
    #print(factors)

    expressions = calculate_answers(factors)
    answers = [eval(expression) for expression in expressions]

    if stated_answer in answers:
        return True
    
    else:
        return False

# Test
#print(f"{calibrations[0]}: {check_answers(calibrations[0])}")
#print(f"{calibrations[1]}: {check_answers(calibrations[1])}")
print(f"{calibrations[-1]}: {check_answers(calibrations[-1])}")


# Sum up all 'True' answers
"""
true_calibrations_sum = 0

for calibration in calibrations:
    if check_answers(calibration):
        true_calibrations_sum += calibration[0]


print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {true_calibrations_sum}")
print("--------------")
"""


print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")