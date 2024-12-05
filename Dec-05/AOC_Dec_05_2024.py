from pathlib import Path

test_rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
"""

test_updates = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

#  Test Result:

# Read and extract input data
path = Path('input.txt')


# Parse into a list of lines
# lines = path.read_text().splitlines()
raw_rules = test_rules.splitlines()
raw_updates = test_updates.splitlines()
print(raw_rules)

"""PART 1"""

# Store rules in a data type that is easily referenced - list of tuples.
rules = []

for rule in raw_rules:
    rules.append((int(rule[:2]),int(rule[3:5])))

print(rules)


# Use the LH value in the rules dict as the key.
# Store updates as a list of lists.
updates = []

for update in raw_updates:
    raw_numbers = update.split(",")
    numbers = []
    for raw_number in raw_numbers:
        numbers.append(int(raw_number))
    updates.append(numbers)

print(updates)
# Store an update as a list.
# Iterate over the list
#   - first select the rules for the item in the list.
#   - assume the update is in correct order.
#   - test each rule in turn - we need only test to the RHS.
#   - if any test is false, break the loop and pop the update from the list

def Get_Rules_For_update(update, rules):
    """checks if the list is conformant to the rules"""

    # Get relevant rules
    applicable_rules = []

    for item in update:
        for rule in rules:
            if item == rule[0]:
                applicable_rules.append(rule)
        
        print(f"item: {item}, rules: {applicable_rules}")
    
    
# Test
Get_Rules_For_update(updates[0], rules)

# Once done get all 'middle' values and sum them up.





print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")



print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")