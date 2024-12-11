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

        if '.' not in disk:
            next_free_block_index = -1   # Handle case of no free blocks
            break

        if (disk[next_free_block_index]) == '.':
            not_found = False

        else:
            next_free_block_index += 1


    return next_free_block_index


# Test
#print(find_next_free_block([0, '.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]))
#print(find_next_free_block(['.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]))
#print(find_next_free_block([1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]))
#print(find_next_free_block([1, 1, 1, 2, 2, 2, 2, 2]))


def run_amphipod(disk):
    """Fills empty spaces on left starting with righter-most disk blocks"""

    # A counter to find and store the next free space
    #next_free_block = next_free_block + find_next_free_block(disk) 

    # A variable to build output
    # optimized_disk = optimized_disk.append(disk) # initialise to == disk

    # A while loop to pop() and push() from the end of the list

    disk_optimized = False

    while not disk_optimized:
        block = disk.pop()

        # Find index of first available 
        try:
            next_free_block = next((index for index, item in enumerate(disk) if item == '.'))
        
        except:
            StopIteration
            disk_optimized = True
        
        else:
            # Replace free block with block
            disk[next_free_block] = block

        # Check if list contains any more spare blocks, break if none found
        if '.' not in disk:
            disk_optimized = True

    return(disk)
            
# Test
#disk_map = '12345'
disk_map = test_data
print(disk_map)
disk = generate_disk_blocks(disk_map)
print(disk)
optimized_disk = run_amphipod(disk)
print(optimized_disk)


# Calculate checksum

print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")



print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")