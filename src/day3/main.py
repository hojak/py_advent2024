import sys

from day3.tools import get_program_result
from adv24_tools.tools import read_from_file

def main(filename: str) -> None:
    text_file_input = read_from_file(filename)

    print ("Result: ")
    print ( get_program_result(text_file_input) )


if __name__ == "__main__":
    main(sys.argv[1])
