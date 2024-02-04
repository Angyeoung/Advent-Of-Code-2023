with open("input.txt") as file:
    lines = [line.split() for line in file.readlines()]

TEN_BIL = 10000000000
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def hand_type(hand):
    counts = {}
    for card in hand:
        if counts.get(card) == None:
            counts[card] = hand.count(card)
    
    vals = list(counts.values())
    rank = 0
    if 5 in vals: 
        rank = 6
    elif 4 in vals: 
        rank = 5
    elif 3 in vals and 2 in vals: 
        rank = 4
    elif 3 in vals: 
        rank = 3
    elif vals.count(2) == 2:
        rank = 2 
    elif 2 in vals:
        rank = 1 
    
    return rank

def type_value(hand):
    return hand_type(hand) * TEN_BIL

def hand_value(hand):
    digit_strings = [str(ranks.index(card)).rjust(2, "0") for card in hand]
    return int("".join(digit_strings))

def best_joker_hand(hand: str):
    if "J" not in hand:
        return hand
    max_value, best_hand = 0, None
    for card in ranks:
        # Temp hand with jokers replaced
        temp_hand = hand.replace("J", card)
        # Value of that hand
        temp_value = type_value(temp_hand) + hand_value(hand)
        # If the value is greater
        if temp_value > max_value:
            # Update best hand and max value
            max_value = temp_value
            best_hand = temp_hand
    return best_hand

def part1():
    result = {}
    for line in lines:
        [hand, bid] = line
        value = type_value(hand) + hand_value(hand)
        result[value] = bid

    total = 0
    for i, val in enumerate(sorted(result)):
        total += int(result[val]) * (i + 1)
    return total

def part2():
    global ranks
    ranks = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    result = {}
    for line in lines:
        [hand, bid] = line
        best_hand = best_joker_hand(hand)
        best_hand_value = type_value(best_hand) + hand_value(hand)
        result[best_hand_value] = bid

    total = 0
    for i, value in enumerate(sorted(result)):
        total += int(result[value]) * (i + 1)
    return total

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")