from random import randint

squares = ["GO", 
"Med Av", 
"Chest 1", 
"Baltic avenue", 
"Tax", 
"Reading Train", 
"Oriental Av", 
"Chance 1",
"Vermont Av",
"Connenticut Av",
"Jail", # TODO make it so we can get stuck here...
"St charles place",
"Elec Utility",
"States av",
"Virginia av",
"Penn Train",
"St James",
"Chest 1",
"Tennessee av",
"NY Av",
"Free parking",
"Kentucky av",
"Chance 2",
"Indiana av",
"Illinois",
"B&O Train",
"Atl av",
"Ventnor av",
"Water Utility",
"Marvin gardens",
"Go to prison",
"Pacific avenue",
"North carolina av",
"Chest 2",
"Penn av",
"Short Train",
"Chance 3",
"park place",
"luxury tax",
"Broadwalk"]


board = {}
locations = {}


for i, name in enumerate(squares):
    board[i] = name
    locations[name] = i

def go_to_nearest(start_pos, destination):
    while True:
        if destination in board[start_pos]:
            return start_pos
        start_pos += 1
        start_pos = start_pos % len(squares)
    

def roll():
    return (randint(1, 6), randint(1, 6))

def move(visits, position, n_rolls_this_turn):
    die = roll()
    distance = die[0] + die[1]
    if n_rolls_this_turn == 3:
        position = locations["Jail"]
    else:
        position += distance
        position = position % len(squares)

    if "Go to prison" in board[position]:
        visits[board[position]] += 1
        position = locations["Jail"]
    
    if "Chest" in board[position]:
        card = randint(1,16)
        visits[board[position]] += 1
        if (card == 1):
            position = locations["Jail"]
        if (card == 2):
            position = locations["GO"]

    if "Chance" in board[position]:
        card = randint(1,16)
        visits[board[position]] += 1
        if card == 1:
            position = locations["Jail"]
        if card == 2:
            position = locations["GO"]
        if card == 3:
            position = locations["Illinois"]
        if card == 4:
            # go to nearest utility
            position = go_to_nearest(position, "Utility")
        if card == 5:
            # go to nearest train station
            position = go_to_nearest(position, "Train")
        if card == 6:
            position -= 3
            position = position % len(squares)
        if card == 7:
            position = locations["Jail"]
        if card == 8:
            position = locations["Reading Train"]
        if card == 9:
            position = locations["Broadwalk"]
    visits[board[position]] += 1

    if die[0] == die[1] & position != locations["Jail"]:
        position = move(visits, position, n_rolls_this_turn+1)

    return position

def main():
    position = 0

    visits = {}
    for square in squares:
        visits[square] = 0

    for _ in xrange(200):
        position = move(visits, position, 0)

    print visits


if __name__ == '__main__':
    main()



