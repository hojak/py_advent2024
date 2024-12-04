import re

def read_from_file(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

def split_lines_into_numbers(text_file_input: str) -> list:
    return list(map(lambda line: [int(string) for string in re.split('\\s+', line)], text_file_input.split('\n')))
