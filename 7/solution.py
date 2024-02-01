# Part 1
with open("input.txt") as file:
    lines = [line.split() for line in file.readlines()]

# To get the count
[hand, bid] = lines[0]
counts = {}
for card in hand:
    if counts.get(card) != None:
        counts[card] = hand.count(card)



"""
    Find a way to actually calculate a winner,
    Find a way to store the rankings
    Find a way to sort the rankings and/or place them in order

"""