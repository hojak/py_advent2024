from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates

directions = [
    Coordinates(1,0),
    Coordinates(0,1),
    Coordinates(-1,0),
    Coordinates(0,-1),
]

class PlantArrangement:
    map : StringMap

    def __init__(self, map):
        self.map = StringMap(map)

    def get_data_of_region ( self, start_point: Coordinates):
        work_map = StringMap(self.map.__str__())
        plant = self.map.get_char_at(start_point)

        look_into = [ start_point ]
        area = 0
        perimeter = 0
        work_map.set_char_at (start_point, " ")

        while len(look_into) > 0:
            current = look_into.pop()
            area += 1   
            possible_nexts = self.get_neighbors_with_same_plant(current)

            perimeter += 4 - len ( possible_nexts)

            for next in possible_nexts:
                if ( work_map.get_char_at(next) == plant ):
                    work_map.set_char_at(next, " ")
                    look_into.append (next)

        return { 'area': area, 'perimeter': perimeter }
    
    def has_been_visited ( self, work_map: StringMap, location:Coordinates):
        return work_map.get_char_at(location) == " "
    
    
    def count_neighbors_with_same_plant ( self, position: Coordinates): 
        return len(self.get_neighbors_with_same_plant(position))
    

    def get_neighbors_with_same_plant ( self, position: Coordinates):
        result = []
        this_plant = self.map.get_char_at(position)

        for direction in directions:
            if ( self.map.get_char_at(position.add(direction)) == this_plant):
              result.append ( position.add(direction))

        return result
