"""
Part One
"""
total = 0
with open("input.txt", "r") as file:
    for line in file:
        first = last = None
        for char in line:
            if char.isdigit():
                last = char
                if first is None:
                    first = char
        total += int(first + last)
print(total)

"""
Part Two
"""
