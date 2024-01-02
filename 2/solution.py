import re

# Returns 0 if the game is impossible, or the ID of the game if possible
def game_is_possible(line = ""):
    max_red = 12
    max_green = 13
    max_blue = 14

    game_id = int(re.search("(?<=Game ).+(?=:)", line)[0])
    game_info = re.sub("Game.+: ", "", line).rstrip()
    game_parts = re.split(";", game_info)
    
    for game_part in game_parts:
        colors_revealed = re.split(",", game_part)
        for color_revealed in colors_revealed:
            number = int(re.search("\d+", color_revealed)[0])
            if ("red" in color_revealed and number > max_red):
                return 0
            if ("green" in color_revealed and number > max_green):
                return 0
            if ("blue" in color_revealed and number > max_blue):
                return 0
    return game_id

INPUT = "input.txt"
total = 0
with open(INPUT, "r") as file:
    for line in file:
        total += game_is_possible(line)
print(total)

