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
    Points system?:
        J = 11, Q = 12, K = 13, A = 1
        AAAAA = 1414141414
        22222 = 0202020202
        Should work for all hands and allow easy comparisons (Higher number wins)
        Could possible add incrememnts of 10 billion to denote hand rank too,
        grouping the entire hand score into one number

    If two hands have the same type, a second ordering rule takes effect. 
    Start by comparing the first card in each hand. If these cards are different, 
    the hand with the stronger first card is considered stronger. If the first 
    card in each hand have the same label, however, then move on to considering 
    the second card in each hand. If they differ, the hand with the higher 
    second card wins; otherwise, continue with the third card in each hand, 
    then the fourth, then the fifth.

    1. Use card counts to classify the type of hand
        Five of a kind:
            { A: 5 }
        Four of a kind:
            { A: 4, K: 1}
        Full house:
            { A: 3, K: 2}
        Three of a kind:
            { A: 3, K: 1, Q: 1 }
        Two pair:
            { A: 2, K: 2, Q: 1 }
        One pair:
            { A: 2, K: 1, Q: 1, J: 1 }
        High Card:
            { A: 1, K: 1, Q: 1, J: 1, T: 1 }

    2. Use point system to classify card score (Read above)
    3. Efficiently sort the hands by their score and give them their ranks
    4. Do the final math to calculate result 
        

"""