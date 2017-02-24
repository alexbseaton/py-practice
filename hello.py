from random import randint
import time
import draw_graph
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
"Chest 2",
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
"Chest 3",
"Penn av",
"Short Train",
"Chance 3",
"park place",
"luxury tax",
"Broadwalk"]

# maps positions to namess of squares
name_of_posn = {}
# maps names of squares to positions
posn_of_name = {}
for i, name in enumerate(squares):
    name_of_posn[i] = name
    posn_of_name[name] = i

# returns the position nearest to start_pos that has destination in its name
def go_to_nearest(start_pos, destination):
    while True:
        if destination in name_of_posn[start_pos]:
            return start_pos
        start_pos += 1
        start_pos = start_pos % len(squares)
    

def roll():
    return (randint(1, 6), randint(1, 6))

def move(visits, position, n_rolls_this_turn):
    die = roll()
    distance = die[0] + die[1]
    if n_rolls_this_turn == 3:
        position = posn_of_name["Jail"]
    else:
        position += distance
        position = position % len(squares)

    if "Go to prison" in name_of_posn[position]:
        visits[name_of_posn[position]] += 1
        position = posn_of_name["Jail"]
    
    if "Chest" in name_of_posn[position]:
        card = randint(1,16)
        visits[name_of_posn[position]] += 1
        if (card == 1):
            position = posn_of_name["Jail"]
        if (card == 2):
            position = posn_of_name["GO"]

    if "Chance" in name_of_posn[position]:
        card = randint(1,16)
        visits[name_of_posn[position]] += 1
        if card == 1:
            position = posn_of_name["Jail"]
        if card == 2:
            position = posn_of_name["GO"]
        if card == 3:
            position = posn_of_name["Illinois"]
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
            position = posn_of_name["Jail"]
        if card == 8:
            position = posn_of_name["Reading Train"]
        if card == 9:
            position = posn_of_name["Broadwalk"]
    visits[name_of_posn[position]] += 1

    if die[0] == die[1] & position != posn_of_name["Jail"]:
        position = move(visits, position, n_rolls_this_turn+1)

    return position

def main():
    start_time = time.time()
    visits = {}
    for square in squares:
        visits[square] = 0

    n_games = 10
    for _ in xrange(n_games):
        position = 0
        for _ in xrange(50):
            position = move(visits, position, 0)

    total_visits = sum(visits.values())
    for square in squares:
        visits[square] *= 100.0/float(total_visits)

    draw_graph.draw(visits, n_games)

    
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
