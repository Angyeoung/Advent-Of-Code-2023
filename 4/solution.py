# Part 1

with open('input.txt') as file:
    total_value = 0
    for line in file:
        nums = line.split(": ")[1].split(" | ")
        win_nums, my_nums = nums[0].split(), nums[1].split()
        total_matches = len(set(my_nums) & set(win_nums))
        if not total_matches: continue
        total_value += pow(2, (total_matches - 1))
    print(f"Part 1: {total_value}")

# Part 2
