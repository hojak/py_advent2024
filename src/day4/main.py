import sys

from day4.word_riddle import WordRiddle
from adv24_tools.tools import read_from_file, split_lines_into_numbers

def main(filename) -> None:
    text_file_input = read_from_file(filename)
    xmas_finder = WordRiddle ( text_file_input )

    print ("Found XMASes: " + str(xmas_finder.number_of_occurences('XMAS')))


if __name__ == "__main__":
    main(sys.argv[1])
