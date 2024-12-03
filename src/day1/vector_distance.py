from functools import reduce

def single_distance(a, b):
    return abs(a-b)


def do_sum ( a, b):
    return a+b

def distance(listOfPairs):
    listOfFirstMembers = list(map(lambda pair: pair[0], listOfPairs))
    listOfSecondMembers = list(map(lambda pair: pair[1], listOfPairs))

    listOfFirstMembers.sort
    listOfSecondMembers.sort

    sortedPairs = zip(listOfFirstMembers, listOfSecondMembers)
    listOfDistances = list(map(lambda pair: single_distance(pair[0], pair[1]), sortedPairs))

    return reduce(do_sum, listOfDistances )


