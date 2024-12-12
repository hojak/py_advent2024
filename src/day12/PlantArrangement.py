from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinate import Coordinates

class PlantArrangement (StringMap):

    def count_neighbors_with_same_plant ( self, position: Coordinates): 
        result = 0
        this_plant = self.get_char_at(position)

        if ( self.get_char_at(position.add(Coordinates(1,0))) == this_plant):
            result += 1
        if ( self.get_char_at(position.add(Coordinates(0,1))) == this_plant):
            result += 1
        if ( self.get_char_at(position.add(Coordinates(-1,0))) == this_plant):
            result += 1
        if ( self.get_char_at(position.add(Coordinates(0,-1))) == this_plant):
            result += 1

        return result