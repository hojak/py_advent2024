from adv24Tools.Coordinates import Coordinates
import re

class Roboter:
    position: Coordinates
    velocity: Coordinates

    def parse_line (line : str):
        result = Roboter()

        match = re.match(r'^p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)$', line)
        if ( not match):
            raise Exception('Illegal roboter line: ' + line)
        
        result.position = Coordinates(int(match.group(1)),int(match.group(2)))
        result.velocity = Coordinates(int(match.group(3)),int(match.group(4)))
        return result
    
    def next_position(self, max_size) -> Coordinates:
        result = self.position.add ( self.velocity)
        result.x = result.x % max_size.x
        result.y = result.y % max_size.y
        return result
    