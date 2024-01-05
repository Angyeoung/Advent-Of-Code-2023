import re

INPUT = "input.txt"

# Part 1
arr = []
with open(INPUT, "r") as file:
    for line in file:
        arr.append(line.rstrip())

print(f"Arr width: {len(arr[1])}\nArr height: {len(arr)}")

symbols = "-+*&/@%=$#"
for line in arr:
    print(line.rstrip())


total = 0
numbers = []
for x in range(len(arr)):
    line = arr[x]
    i = 0
    while i < len(line):
        if line[i].isdigit():
            j = i
            while j < len(line) and line[j].isdigit():
                j += 1

            line[i:j]

            v_range = range(max(0, x-1), min(len(arr), x+2))
            h_range = range(max(0, i-1), min(len(line), j+1))

            isPartNumber = False
            for row_j in v_range:
                for col_j in h_range:
                    char = arr[row_j][col_j]
                    if char in symbols:
                        numbers.append(int(line[i:j]))
                        total += int(line[i:j])
                        isPartNumber = True
                        break
                if isPartNumber:
                    break
            i = j
        i += 1

print(numbers)
print(total)