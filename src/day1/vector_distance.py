from functools import reduce
from collections import defaultdict

def single_distance(a, b):
    return abs(a-b)

def do_sum ( a, b):
    return a+b

def distance(list_of_pairs):
    list_of_first_members = list(map(lambda pair: pair[0], list_of_pairs))
    list_of_second_members = list(map(lambda pair: pair[1], list_of_pairs))

    list_of_first_members.sort()
    list_of_second_members.sort()

    sorted_pairs = zip(list_of_first_members, list_of_second_members)
    list_of_distances = list(map(lambda pair: single_distance(pair[0], pair[1]), sorted_pairs))

    return reduce(do_sum, list_of_distances )


def similarity_score(list_of_pairs: list) -> int:
    list_of_first_members = list(map(lambda pair: pair[0], list_of_pairs))
    list_of_second_members = list(map(lambda pair: pair[1], list_of_pairs))
    
    number_of_occurences = count_number_of_occurences (list_of_second_members)

    list_of_scores = list(map(lambda number: number * number_of_occurences[number], list_of_first_members))

    return reduce(do_sum, list_of_scores )


def count_number_of_occurences(list_of_numnbers):
    result = defaultdict(int)
    for number in list_of_numnbers:
        result[number] +=1
    return result



