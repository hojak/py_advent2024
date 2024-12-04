from functools import reduce
from collections import defaultdict

def single_distance(a, b):
    return abs(a-b)


def do_sum ( a, b):
    return a+b

def distance(listOfPairs):
    listOfFirstMembers = list(map(lambda pair: pair[0], listOfPairs))
    listOfSecondMembers = list(map(lambda pair: pair[1], listOfPairs))

    listOfFirstMembers.sort()
    listOfSecondMembers.sort()

    sortedPairs = zip(listOfFirstMembers, listOfSecondMembers)
    listOfDistances = list(map(lambda pair: single_distance(pair[0], pair[1]), sortedPairs))

    return reduce(do_sum, listOfDistances )


def similarityScore(listOfPairs):
    listOfFirstMembers = list(map(lambda pair: pair[0], listOfPairs))
    listOfSecondMembers = list(map(lambda pair: pair[1], listOfPairs))
    
    numberOfOccurences = countNumberOccurences (listOfSecondMembers)

    listOfScores = list(map(lambda number: number * numberOfOccurences[number], listOfFirstMembers))

    return reduce(do_sum, listOfScores )


def countNumberOccurences(listOfNumnbers):
    result = defaultdict(int)
    for number in listOfNumnbers:
        result[number] +=1
    return result



