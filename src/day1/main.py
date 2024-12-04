import sys

from day1.analyze_coordinates import distance, similarity_score
from adv24_tools.tools import read_from_file, split_lines_into_numbers

def main(filename: str) -> None:
    text_file_input = read_from_file(filename)
    list_of_pairs = split_lines_into_numbers(text_file_input)

    print ("Distance: ")
    print ( distance ( list_of_pairs ) )

    print ('\n\n');
    print ('similarity score')
    print (similarity_score ( list_of_pairs ))


if __name__ == "__main__":
    main(sys.argv[1])
