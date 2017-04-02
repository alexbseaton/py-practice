squares = [x ** 2 for x in range(600)]

assert 144 in squares
assert 143 not in squares

def leads_to_triplet(a, b):
    return a ** 2 + b ** 2 in squares

def sum_of_triplet_is_thousand(a, b):
    return (1000 - a - b) ** 2 == a ** 2 + b ** 2

assert leads_to_triplet(3, 4) == True
assert leads_to_triplet(3, 1) == False

lower = 0
higher = 1
for a in range(1, 500):
    for b in range(a, 501):
        if sum_of_triplet_is_thousand(a, b):
            lower = a
            higher = b

assert lower == 200
assert higher == 375

c_squared = lower ** 2 + higher ** 2

assert c_squared in squares

c = 0
for index, square in enumerate(squares):
    if square == c_squared:
        c = index

print(lower * higher * c)

