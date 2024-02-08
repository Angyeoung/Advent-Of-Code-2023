with open("input.txt") as file:
    # All the lines in the file (stripped)
    _lines = [line.strip() for line in file]
    # The first line, which are the left-right instructions
    INSTS = _lines[0]
    # Total number of instructions, allows for modulation, precalculate this because it's used a lot
    INSTS_TOTAL = len(INSTS)
    # All location strings as 2d array
    LOCATION_STRINGS = [[line[0:3], line[7:10], line[12:15]] for line in _lines[2:]]
    LOCS = dict([(l[0], l[1:]) for l in LOCATION_STRINGS])

def part1():
    # Number of steps taken
    total_steps = 0
    # Current location
    loc = "AAA"
    # Current instruction index
    inst = 0
    while True:
        # Get the index of the direction to go in. Left = 0, Right = 1
        left_right = 0 if INSTS[inst] == "L" else 1
        # Update the location to the new location after following instruction
        loc = LOCS[loc][left_right]
        # Increment total steps
        total_steps += 1
        # Check if we're at the end, return total steps if so
        if loc == "ZZZ": return total_steps
        # Increment to the next instruction
        inst = (inst + 1) % INSTS_TOTAL

def part2():
    start_locs = list(filter(lambda a: a[-1] == "A", LOCS.keys()))
    print(start_locs)
    

    return 1

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")

"""
Number of locations that end with (letter) in input
{
    'A': 1, 'B': 35, 'C': 37, 'D': 35, 'E': 0, 'F': 29, 
    'G': 27, 'H': 30, 'I': 0, 'J': 42, 'K': 42, 'L': 41, 
    'M': 40, 'N': 33, 'O': 0, 'P': 48, 'Q': 39, 'R': 44, 
    'S': 43, 'T': 33, 'U': 0, 'V': 36, 'W': 0, 'X': 42, 
    'Y': 0, 'Z': 1
}
"""
