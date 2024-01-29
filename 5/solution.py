# Part 1
with open("input.txt") as file:
    seeds = [int(x) for x in file.readline()[6:].split()]
    check = [False for _ in seeds]
    for line in file.readlines():
        if not line[0].isdigit(): 
            check = [False for _ in seeds]; continue
        [dest, source, length] = [int(x) for x in line.split(" ")]
        for i, seed in enumerate(seeds):
            if check[i]: continue
            if not source <= seed < source + length: continue
            seeds[i] += dest - source
            check[i] = True
    print(f"Part 1: {min(seeds)}")

# Part 2
# Calculate ranges as parts instead of seeds individually,
# This may require splitting a range into parts