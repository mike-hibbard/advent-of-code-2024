"""
--- Day 2: Red-Nosed Reports ---
Fortunately, the first location The Historians want to search isn't a long walk 
from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of
 the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, 
 they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help 
analyzing some unusual data from the Red-Nosed reactor. 

You turn to check if The Historians are waiting for you, but they seem to have already divided 
into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. 

Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. 
The Red-Nosed reactor safety systems can only tolerate levels that are either
 gradually increasing or gradually decreasing. So, a report only counts as safe 
 if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
"""

from pathlib import Path

"""PART 1"""

test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

# Read and extract input data
path = Path('input.txt')

# Parse into a list of lines
# lines = path.read_text().splitlines()
lines = test_data.splitlines()

# Convert to lists of lints
reports = []

for line in lines:
    chars = line.split()
    report = list(map(int, chars))
    reports.append(report)

# Test - print first line
# print(reports)


# Implement a function to determine if a line is sorted.
def Is_Sorted(report):
    """Returns true if a report is either in asc or desc order"""
    sorted_report = sorted(report)
    if report == sorted(report) or report == sorted(report, reverse=True):
        return True
    
    else:
        return False

# Test Is_Sorted
# print(reports[3])
# print(Is_Sorted(reports[3]))

sorted_reports = []
unsorted_reports = []

# Filter out anything that is not sorted asc or desc
for report in reports:
    if Is_Sorted(report):
        sorted_reports.append(report)

    else:
        unsorted_reports.append(report)
        
# Test Filtering
print(sorted_reports)


# Implement a boolean function to test if all numbers are > 0 and <= 3 apart

def abs(a, b):
    """Absolute function"""
    diff = a - b

    if diff < 0:
        diff = diff * -1

    return diff


def Is_Safe(report):
    """Returns true if report numbers are > 0 and <= 3 digits apart"""

    # Default to True
    is_safe = True

    # Check 'gaps', hence one less than len
    for i in range(0,len(report)-1):
        diff = abs(report[i], report[i+1])

        if diff > 3 or diff == 0:  # == 0 removes cases of repeating numbers.
            is_safe = False
    
    return is_safe

# Test Is_Safe
#print(Is_Safe(sorted_reports[0]))
#print(Is_Safe(sorted_reports[2]))


"""
PART 1 ANSWER
"""
# Count instances of lists that are True.
number_of_safe_reports = 0

for report in sorted_reports:
    if Is_Safe(report):
        number_of_safe_reports +=1

print("\nPART 1 ANSWER")
print("--------------")
print(f"Length of reports list: {len(reports)}")
print(f"Length of sorted reports list: {len(sorted_reports)}")
print(f"Number of safe reports: {number_of_safe_reports}")
print("--------------")


"""
PART 2 ANSWER
"""
# Implement Is_Safe with Problem Dampener Feature
# Split out ORIGINAL reports into safe reports and unsafe reports
# Apply sorting test afterwards

def Problem_Dampener(report):
    """Takes a report and checks if it is safe with any one item taken out"""

    # Default to False - we want to prove it is safe
    is_safe = False

    for i in range(0,len(report)):
        temp_report = report[:i] + report[i+1:]  # Builds a list by removing ith item
        if Is_Safe(temp_report) and Is_Sorted(report):
            is_safe = True
        print(temp_report, is_safe)
    
    return is_safe

# Test
#print(Problem_Dampener([1,3,2,4,5]))  # True
#print(Problem_Dampener([8,6,4,4,1]))  # True


safe_reports = []
unsafe_reports = []


# First get all the safe, sorted reports
for report in sorted_reports:  # Use original list, then need to sort both safe and unsafe lists after
    if Is_Safe(report):
        safe_reports.append(report)
    
    else:
        unsafe_reports.append(report)

# Next get all the unsorted reports - run through Problem Dampener, remove from unsorted, add to safe_reports
for report in unsorted_reports:
    if Problem_Dampener(report):
        safe_reports.append(report)



print("\nPART 2 ANSWER")
print("--------------")
print(f"Number of reports: {len(reports)}")
print(f"Number of safe reports: {len(safe_reports)}")
print(f"safe reports: {safe_reports}")
print(f"Number of unsafe reports: {len(unsafe_reports)}")
print(f"unsafe reports: {unsafe_reports}")
print("--------------")
