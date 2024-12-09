import math
import re
from adv24Tools.Coordinate import Coordinates

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
        reduced_map = re.sub(r'[^a-zA-Z0-9]', '', self.content)
        self.frequencies = list(set(list(reduced_map)))
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

    def coordinates_for_index ( self, index ) -> Coordinates:
        return Coordinates( index % self.width, math.floor(index / self.width) )
    
    def index_for_coordinates ( self, coordinates: Coordinates) -> int:
        return coordinates.x + coordinates.y * self.width
    
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
    
    def get_number_of_antinodes(self) -> int:
        found_antinodes = []

        for frequency in self.frequencies:
            for index1 in range ( len(self.antenna_locations[frequency])-1):
                for index2 in range ( index1+1, len(self.antenna_locations[frequency])):
                    for antinode_location in self.find_antinodes ( self.antenna_locations[frequency][index1],self.antenna_locations[frequency][index2]):
                        antinode_index = self.index_for_coordinates ( antinode_location )
                        if ( not antinode_index in found_antinodes ):
                            found_antinodes.append(antinode_index)

        return len ( found_antinodes )


        
    