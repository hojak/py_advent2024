import re
from functools import reduce

def find_mul_statements ( input: str ) -> list :
    return re.findall ( r'(mul\(\d{1,3},\d{1,3}\))', input)

def get_mul_result ( input:str )-> int :
    m = re.search(r'mul\((\d+),(\d+)\)', input)

    if m:
        return int(m.group(1)) * int(m.group(2))
    
    return 0

def get_program_result ( input: str) -> int:
    mul_statements = find_mul_statements(input)
    
    results = list(map(get_mul_result, mul_statements))

    return reduce ( lambda a,b : a+b, results)