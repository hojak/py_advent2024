import sys, re

from vector_distance import distance

def readFromFile(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

def splitIntoPairs(textFileInput):
    return list(map(lambda line: [int(string) for string in re.split('\s+', line)], textFileInput.split('\n')))

def main(filename):
    textFileInput = readFromFile(filename)
    listOfPairs = splitIntoPairs(textFileInput)

    print ( distance ( listOfPairs ) )


if __name__ == "__main__":
    main(sys.argv[1])