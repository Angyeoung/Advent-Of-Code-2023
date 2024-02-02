# Part 1
with open("input.txt") as file:
    lines = [line.split() for line in file.readlines()]

BIL = 1000000000
CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
result = {}
for line in lines:
    [hand, bid] = line
    cardValue = 0
    counts = {}
    for card in hand:
        if counts.get(card) == None:
            counts[card] = hand.count(card)
    
    vals = list(counts.values())
    if 5 in vals: cardValue = 60 * BIL
    elif 4 in vals: cardValue = 50 * BIL
    elif 3 in vals and 2 in vals: cardValue = 40 * BIL
    elif 3 in vals: cardValue = 30 * BIL
    elif vals.count(2) == 2: cardValue = 20 * BIL
    elif 2 in vals: cardValue = 10 * BIL

    cardValue += int("".join([str(CARDS.index(c)).rjust(2, "0") for c in hand]))
    if result.get(cardValue) != None:
        print(cardValue)
    result[cardValue] = bid

total = 0
for i, val in enumerate(sorted(result)):
    total += int(result[val]) * (i + 1)

print(f"Part 1: {total}")