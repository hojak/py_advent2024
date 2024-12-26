import math

def mix_in ( a: int, b: int) -> int:
    return a ^ b

def prune ( value: int) -> int:
    return value % 16777216

def next_secret_value ( current: int ) -> int:
    return step3 ( step2 ( step1 ( current )))

def step1 ( current: int ) -> int:
    return prune ( mix_in ( current * 64, current))

def step2 ( current: int ) -> int :
    return prune ( mix_in (  math.floor(current / 32), current ))

def step3 ( current: int ) -> int :
    return prune ( mix_in ( current * 2048, current))

def apply_n_secret_steps ( base: int, steps: int ) -> int :
    result = base
    for step in range(steps):
        result = next_secret_value(result)
    return result

def sum_for_buyers ( list_of_secreats: list ) -> int:
    result = 0
    for secret in list_of_secreats:
        result += apply_n_secret_steps(secret, 2000)
    return result

def get_price ( value: int) -> int : 
    return value % 10


class Sequence:
    def __init__(self, sequence : list):
        self.sequence = sequence

    def next(self, value):
        return Sequence(self.sequence[1:] + [value])
    
    def __eq__(self, value):
        return self.sequence == value.sequence
    
    def __str__(self):
        return '/'.join( list(map(lambda i: str(i), self.sequence )))