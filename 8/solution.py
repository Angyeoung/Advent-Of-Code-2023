with open("input.txt") as file:
    # All the lines in the file (stripped)
    _lines = [line.strip() for line in file]
    # The first line, which are the left-right instructions
    INSTS = _lines[0]
    # Total number of instructions, allows for modulation, precalculate this because it's used a lot
    INSTS_TOTAL = len(INSTS)
    # Creates a dictionary formatted like so: { LOCATION: (LEFT_LOCATION, RIGHT_LOCATION), ...}
    LOCS = dict([(line[0:3], [line[7:10], line[12:15]]) for line in _lines[2:]])

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
        # Increment to the next instruction
        inst = (inst + 1) % INSTS_TOTAL
        # Increment total steps
        total_steps += 1
        # Check if we're at the end, return total steps if so
        if loc == "ZZZ": return total_steps

def part2():
    return

print(f"Part 1: {part1()}")