# Part 1
with open('input.txt') as file:
    total_value = 0
    for line in file:
        win_nums, my_nums = line[10:40].split(), line[42:].split()
        total_matches = len(set(my_nums) & set(win_nums))
        if not total_matches: continue
        total_value += pow(2, (total_matches - 1))
    print(f"Part 1: {total_value}")

# Part 2
with open('input.txt') as file:
    total_cards = 0
    card_dict = {}
    lines = file.readlines()

    def proccess_card(card_number):
        global total_cards
        total_cards += 1

        matches = card_dict.get(card_number)
        if matches == None:
            line = lines[card_number - 1]
            win_nums, my_nums = line[10:40].split(), line[42:].split()
            matches = len(set(my_nums) & set(win_nums))
            card_dict[card_number] = matches
        
        for card in range(0, matches):
            proccess_card(card_number + card + 1)

    for card in range(len(lines)):
        proccess_card(card)

    print(f"Part 2: {total_cards}")