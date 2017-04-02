""" Solution to a problem """

def soln(T):
    """
    Solution to graph problem.
    Takes an array of ints and returns an array of ints

    want to return an array of the number of cities positioned at
    each distance 1, 2, ... , M-1 from the capital

    the input is an array of M integers s.th
    if T[P] = Q and P = Q then P is the capital
    if T[P] = Q and P != Q then there is a direct road between P and Q

    """
    M = len(T)
    # Find the capital
    capital = -1
    for i, city in enumerate(T):
        if city == i:
            capital = city
    # Check a capital actually exists...
    assert capital != -1

    # All I need is a dictionary that goes from
    # int i -> {int j s.th T[j] == i}
    dictionary = {k: [] for k in range(M)}
    for index, city in enumerate(T):
        if index == city: # ignore the capital
            continue
        dictionary[city].append(index)
    citiesAtDistance = {k: [] for k in range(1, M)}

    # Find distance 1 cities
    citiesAtDistance[1] = dictionary[capital]
    # Find distance 2 and above cities
    for k in range(1, M-1):
        for city in citiesAtDistance[k]:
            for neighbour in dictionary[city]:
                citiesAtDistance[k+1].append(neighbour)

    result = []
    for value in citiesAtDistance.values():
        result.append(len(value))

    return result

if __name__ == '__main__':
    # T[1] = 1 => 1 is the capital
    # T[9] = 1 => 9 is joined to 1
    # T[7] = T[3] = T[0] = 9 => 0, 7, 3 are joined to 9
    # etc...

    # expected output: [1, 3, 2, 3, 0 ,0, 0, 0, 0]
    print(soln([9, 1, 4, 9, 0, 4, 8, 9, 0, 1]))
