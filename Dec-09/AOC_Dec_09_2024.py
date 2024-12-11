from pathlib import Path

test_data = """2333133121414131402"""

#  Test Result:

# Read and extract input data
path = Path('input.txt')


# Parse into a list of lines
# lines = path.read_text().splitlines()
lines = test_data.splitlines()
# print(lines[0])

"""PART 1"""

# Decode disk map into actul disk representation
# Turn 12345 into 0..111....22222
def generate_disk_blocks(disk_map):
    """Returns the actual blocks, spaced out, as a list"""

    disk = []
    block_symbol = 0
    space_symbol = '.'

    for index, item in enumerate(disk_map):

        counter = int(item)
        symbol = None
        if index %2 == 0:
            symbol = block_symbol
            block_symbol += 1
        else:
            symbol = space_symbol


        while counter > 0:
            disk.append(symbol)
            counter -= 1

    print(disk)
    return(disk)

# Test
# generate_disk_blocks('12345')       
# generate_disk_blocks(test_data) 



# Run amphipod to move blocks left into free spaces

def find_next_free_block(disk):
    """Takes in a disk and returns the index of the first occurence of '.'"""

    not_found = True

    next_free_block_index = 0

    while not_found:

        if (disk[next_free_block_index]) == '.':
            not_found = False

        else:
            next_free_block_index += 1


    return next_free_block_index


# Test
#print(find_next_free_block([0, '.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]))
#print(find_next_free_block(['.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]))
#print(find_next_free_block([1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]))


def run_amphipod(disk):
    """Fills empty spaces on left starting with righter-most disk blocks"""

    # A counter to find and store the next free space

    # A while loop to pop() and push() from the end of the list

    """
      Pseudo code:
        pop last item
        if last item == '.' then continue
        else if last item in [0-9] update list with item at next free counter.
      
    """



# Calculate checksum

print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")



print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")