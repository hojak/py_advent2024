import sys, re

from vector_distance import distance, similarity_score

def read_from_file(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

def splitIntoPairs(text_file_input: str) -> list:
    return list(map(lambda line: [int(string) for string in re.split('\\s+', line)], text_file_input.split('\n')))

def main(filename: str) -> None:
    text_file_input = read_from_file(filename)
    list_of_pairs = splitIntoPairs(text_file_input)

    print ("Distance: ")
    print ( distance ( list_of_pairs ) )

    print ('\n\n');
    print ('similarity score')
    print (similarity_score ( list_of_pairs ))


if __name__ == "__main__":
    main(sys.argv[1])
