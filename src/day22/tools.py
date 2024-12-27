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
        return str(self) == str(value)
    
    def __str__(self):
        return '/'.join( list(map(lambda i: str(i), self.sequence )))
    

class SequenceGains:
    def __init__(self):
        self.sequence_gains = {}

    def register_gain(self, sequence, price):
        index = str(sequence)
        if ( not index in self.sequence_gains):
            self.sequence_gains[index] = price
    
    def compute_possible_buyer_sequences(self, secret, steps):
        current_secret = secret
        price = get_price(current_secret)

        sequence = Sequence([0,0,0,0])
        for i in range(steps):
            last_price = price
            current_secret = next_secret_value(current_secret)
            price = get_price(current_secret)
            sequence = sequence.next(price - last_price)
            
            if (i>3):
                self.register_gain (sequence, price)


    def get_best_sequence(self):
        print (self.sequence_gains)
        stored_by_price = sorted(self.sequence_gains.items(), key=lambda x:x[1], reverse=True)
        (sequence, price) = stored_by_price[0]
        return sequence


    def get_gain_for_sequence(self, sequence):
        return self.sequence_gains[str(sequence)]
    

    def merge ( self, other_sequence_gain ):
        for key in other_sequence_gain.sequence_gains:
            if ( key in self.sequence_gains):
                self.sequence_gains[key] += other_sequence_gain.sequence_gains[key]
            else:
                self.sequence_gains[key] = other_sequence_gain.sequence_gains[key]


    def best_sequence_for_buyers ( buyer_secrets: list ):
        sequence_gain = SequenceGains()

        for secret in buyer_secrets:
            buyer_sequences = SequenceGains()
            buyer_sequences.compute_possible_buyer_sequences(secret, 2000)

            sequence_gain.merge ( buyer_sequences )

        best_sequence = sequence_gain.get_best_sequence()

        return ( best_sequence, sequence_gain.get_gain_for_sequence ( best_sequence ))

