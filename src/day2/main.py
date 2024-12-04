import sys

from day2.report_checks import count_save_reports, count_save_reports_with_dampener
from adv24_tools.tools import read_from_file, split_lines_into_numbers

def main(filename) -> None:
    text_file_input = read_from_file(filename)
    list_of_reports = split_lines_into_numbers(text_file_input)

    print ("Number of Save Reports:")
    print (count_save_reports(list_of_reports))

    print ("\nNumber of Save Reports with Dampener:")
    print (count_save_reports_with_dampener(list_of_reports))


if __name__ == "__main__":
    main(sys.argv[1])
