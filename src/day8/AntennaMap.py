import re
from day8.StringMap import StringMap

class AntennaMap ( StringMap ):
    frequencies : list
    antenna_locations: dict
    
    def __init__(self, map : str ):
        super().__init__(map)

        self.init_frequencies()
        self.init_antenna_locations()



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
    
    def find_antinodes_with_resonance ( self, antenna1, antenna2) -> list :
        dif = antenna2.sub(antenna1)
        result = []

        possible = antenna1
        while ( self.is_in_bounds ( possible)):
            result.append(possible)
            possible = possible.add ( dif )

        possible = antenna1.sub (dif)
        while (self.is_in_bounds(possible)):
            result.append(possible)
            possible = possible.sub(dif)

        return result        

    
    def is_in_bounds ( self, location) -> bool :
        return location.x >= 0 and location.y >= 0 and location.x < self.width and location.y < self.height
    
    def get_number_of_antinodes(self, with_resonance: bool = False) -> int:
        found_antinodes = []

        for frequency in self.frequencies:
            for index1 in range ( len(self.antenna_locations[frequency])-1):
                for index2 in range ( index1+1, len(self.antenna_locations[frequency])):
                    if ( with_resonance ):
                        antinodes_for_pair = self.find_antinodes_with_resonance ( self.antenna_locations[frequency][index1], self.antenna_locations[frequency][index2])
                    else:
                        antinodes_for_pair = self.find_antinodes ( self.antenna_locations[frequency][index1], self.antenna_locations[frequency][index2])

                    for antinode_location in antinodes_for_pair:
                        antinode_index = self.index_for_coordinates ( antinode_location )
                        if ( not antinode_index in found_antinodes ):
                            found_antinodes.append(antinode_index)

        return len ( found_antinodes )


        
    