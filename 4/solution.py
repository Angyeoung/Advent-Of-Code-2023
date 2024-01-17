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
    # For each key (card number), store the number of cards it wins
    # Ex: `1: 2`
    card_dict = {}
    total_cards = 0
    lines = file.readlines()

    def proccess_card(card_number: int):
        # Increment cards as we have won this card
        global total_cards
        total_cards += 1
        # Check for the card in card_dict, process won cards
        total_matches = card_dict.get(card_number)
        if total_matches != None:
            cards_won = range(card_number + 1, card_number + total_matches + 1)
            print(f"Card: {card_number} | Matches: {total_matches} | In dict?: Y | Total cards: {total_cards} | Processing: {list(cards_won)}")
            for card in cards_won:
                proccess_card(card)
        else:
            # At this point, the card isn't in the card_dict, so calculate the winners and proccess them
            line = lines[card_number - 1]
            win_nums, my_nums = line[10:40].split(), line[42:].split()
            total_matches = len(set(my_nums) & set(win_nums))
            card_dict[card_number] = total_matches
            cards_won = range(card_number + 1, card_number + total_matches + 1)
            print(f"Card: {card_number} | Matches: {total_matches} | In dict?: N | Total cards: {total_cards} | Processing: {list(cards_won)}")
            for card in cards_won:
                proccess_card(card)
        return
    proccess_card(1)
    print(f"Part 2: {total_cards}")
# lines = file.seek(118 * lineIndex)