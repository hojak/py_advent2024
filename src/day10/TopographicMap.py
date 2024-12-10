from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinate import Coordinates

class TopographicMap (StringMap):
    
    def __init__(self, map):
        super().__init__(map)

    def score_of_location(self, location: Coordinates) -> int:
        return len(self.get_reachable_hill_tops(location, 0))

    def get_reachable_hill_tops ( self, location: Coordinates, current_height: int) -> list:
        if ( not self.is_within_bounds(location) or self.get_char_at(location) != str(current_height) ):
            return []
        
        if ( current_height == 9):
            return [self.index_for_coordinates(location)]
        
        return list(set(self.get_reachable_hill_tops(location.add(Coordinates(0,1)),  current_height+1) \
            + self.get_reachable_hill_tops(location.add(Coordinates(1,0)),  current_height+1) \
            + self.get_reachable_hill_tops(location.add(Coordinates(0,-1)),  current_height+1) \
            + self.get_reachable_hill_tops(location.add(Coordinates(-1,0)),  current_height+1)))

    def sum_of_scores (self) -> int:
        result = 0
        for index in range(len(self.content)):
            if ( self.content[index] == '0'):
                result += self.score_of_location( self.coordinates_for_index(index))

        return result



    def number_of_different_trails(self) -> int:
        result = 0
        for index in range(len(self.content)):
            if ( self.content[index] == '0'):
                result += self.number_of_different_trails_from_location(self.coordinates_for_index(index), 0)

        return result
    
    def number_of_different_trails_from_location ( self, location: Coordinates, current_height: int) -> int:
        if ( not self.is_within_bounds(location) or self.get_char_at(location) != str(current_height) ):
            return 0
        
        if ( current_height == 9):
            return 1
        
        return self.number_of_different_trails_from_location(location.add(Coordinates(0,1)),  current_height+1) \
            + self.number_of_different_trails_from_location(location.add(Coordinates(1,0)),  current_height+1) \
            + self.number_of_different_trails_from_location(location.add(Coordinates(0,-1)),  current_height+1) \
            + self.number_of_different_trails_from_location(location.add(Coordinates(-1,0)),  current_height+1)
