INPUT = "input.txt"
# Part One
total = 0
with open(INPUT, "r") as file:
    for line in file:
        first = last = None
        for char in line:
            if char.isdigit():
                last = char
                if first is None:
                    first = char
        total += int(first + last)
print(f"Part 1: {total}")


# Part Two
digits = {
    "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6",
    "7": "7", "8": "8", "9": "9",
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}


total = 0
with open(INPUT, "r") as file:
    for line in file:
        firstDigit = lastDigit = None
        firstIndex = lastIndex = -1
        for [string, value] in digits.items():
            index = line.find(string)
            rindex = line.rfind(string)
            if index == -1 and rindex == -1:
                continue
            if firstDigit is None or index < firstIndex:
                firstDigit = string
                firstIndex = index
            if lastDigit is None or index > lastIndex:
                lastDigit = string
                lastIndex = index
            if firstDigit is None or rindex < firstIndex:
                firstDigit = string
                firstIndex = rindex
            if lastDigit is None or rindex > lastIndex:
                lastDigit = string
                lastIndex = rindex
        total += int(digits[firstDigit] + digits[lastDigit])
print(f"Part 2: {total}")