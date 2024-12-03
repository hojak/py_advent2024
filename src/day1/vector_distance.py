def single_distance(a, b):
    return abs(a-b)


def distance(listOfPairs):
    listOfFirstMembers = []
    listOfSecondMembers = []
    
    for pair in listOfPairs:
        listOfFirstMembers.append(pair[0])
        listOfSecondMembers.append(pair[1])

    listOfFirstMembers.sort
    listOfSecondMembers.sort

    result = 0
    for i in range(len(listOfFirstMembers)):
        result += single_distance(listOfFirstMembers[i], listOfSecondMembers[i])

    return result