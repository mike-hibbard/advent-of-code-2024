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

generate_disk_blocks('12345')        

# Run amphipod to move blocks left into free spaces

# Calculate checksum

print("\nPART 1 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")



print("\nPART 2 ANSWER")
print("--------------")
print(f"Answer: {None}")
print("--------------")