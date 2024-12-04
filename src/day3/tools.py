import re

def find_mul_statements ( input: str ) -> list :
    return re.findall ( r'(mul\(\d{1,3},\d{1,3}\))', input)