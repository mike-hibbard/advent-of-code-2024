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
    """Gets the rules that apply to the update"""

    # Get relevant rules
    applicable_rules = []

    for item in update:
        for rule in rules:
            if item == rule[0]:
                applicable_rules.append(rule)
        
        print(f"item: {item}, rules: {applicable_rules}")

    return(applicable_rules)
    
    
# Test
#Get_Rules_For_update(updates[0], rules)


def Is_Update_In_Order(update):
    """Returns True if the order conforms to the rules"""

    is_ordered = True

    applicable_rules = Get_Rules_For_update(update, rules)

    for index, item in enumerate(update):
        
        # Check rules L->R
        items_to_right = update[index:]

        # Check rules R->L
        items_to_left = update[0:index+1]

        for rule in applicable_rules:
            
            # Handle vacuously true case
            if rule[1] not in items_to_right:
                continue
            
            # Error case; if this is false we know the update is not in order
            if rule[0] == item and rule[1] not in items_to_right:
                is_ordered = False
                break

            # Error case; if this is true we know the update is not in order
            if rule[1] == item and rule[0] not in items_to_left:
                is_ordered = False
                break


    print(is_ordered)
    return(is_ordered)
   

# Collect valid updates
valid_updates =[]

for update in updates:
    if Is_Update_In_Order(update):
        valid_updates.append(update)


print(f"Valid updates: {valid_updates}")

# Once done get all 'middle' values and sum them up.

sums = 0

for valid_update in valid_updates:
    middle = len(valid_update) // 2
    sums += valid_update[middle]


print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {sums}")
print("--------------")



print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")