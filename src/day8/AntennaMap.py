from adv24Tools.Coordinate import Coordinate

class AntennaMap:
    content: str
    frequencies : list

    def __init__(self, map : str ):
        self.content = map

        self.init_frequencies()


    def init_frequencies(self):
        self.frequencies = list(set(list(self.content)))
        self.frequencies.sort()

    def get_antennas_for_frequency(self, frequency)-> list:
        return [Coordinate(0,0)]
    
    def get_found_frequencies ( self ) -> list :
        return self.frequencies