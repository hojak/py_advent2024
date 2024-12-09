import math
import re
from adv24Tools.Coordinate import Coordinate

class AntennaMap:
    content: str
    frequencies : list
    antenna_locations: dict
    width: int
    heigth: int

    def __init__(self, map : str ):
        self.content = map

        self.init_map (map)

        self.init_frequencies()
        self.init_antenna_locations()

    def init_map(self, init_str):
        self.content = init_str.replace('\n', '')
        found = init_str.find('\n')
        if (found >= 0):
            self.width = found
        else:
            self.width = len(init_str)
        self.height = math.ceil(len(self.content) / self.width)

        if ( self.width * self.height != len(self.content)):
            raise Exception ( "illegal length of map definition")


    def init_frequencies(self):
        self.frequencies = list(set(list(self.content)))
        self.frequencies.sort()

    def init_antenna_locations(self):
        self.antenna_locations = {}
        for frequency in self.frequencies:
            found_indexes = [match.start() for match in re.finditer(frequency, self.content)]

            self.antenna_locations[frequency] = list(map( lambda index : self.coordinates_for_index(index), found_indexes))
            

    def get_antennas_for_frequency(self, frequency)-> list:
        return self.antenna_locations[frequency]
    
    def get_found_frequencies ( self ) -> list :
        return self.frequencies

    def coordinates_for_index ( self, index ) -> Coordinate:
        return Coordinate( index % self.width, math.floor(index / self.width) )
    
    def find_antinodes ( self, antenna1, antenna2) -> list :
        result = []
        dif = antenna2.sub(antenna1)

        antinote1 = antenna1.sub (dif)
        if ( self.is_in_bounds (antinote1)):
            result.append(antinote1)
        
        antinote2 = antenna2.add (dif)
        if ( self.is_in_bounds (antinote2)):
            result.append(antinote2)

        return result
    
    def is_in_bounds ( self, location) -> bool :
        return location.x >= 0 and location.y >= 0 and location.x < self.width and location.y < self.height