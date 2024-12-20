from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates, directions


class PlantArrangement:
    map : StringMap
    still_to_visit : StringMap

    def __init__(self, map):
        self.map = StringMap(map)
        self.still_to_visit = StringMap(self.map.__str__())

    def get_data_of_region ( self, start_point: Coordinates):
        look_into = [ start_point ]
        area = 0
        perimeter = 0
        self.still_to_visit.set_char_at (start_point, " ")

        while len(look_into) > 0:
            current = look_into.pop()
            possible_nexts = self.get_neighbors_with_same_plant(current)

            area += 1   
            perimeter += 4 - len ( possible_nexts)

            for next in possible_nexts:
                if ( not self.has_been_visited ( next )):
                    self.still_to_visit.set_char_at(next, " ")
                    look_into.append (next)

        return { 'area': area, 'perimeter': perimeter }
    
    def has_been_visited ( self, location:Coordinates):
        return self.still_to_visit.get_char_at(location) == " "
    
    
    def count_neighbors_with_same_plant ( self, position: Coordinates): 
        return len(self.get_neighbors_with_same_plant(position))
    

    def get_neighbors_with_same_plant ( self, position: Coordinates):
        result = []
        this_plant = self.map.get_char_at(position)

        for direction in directions:
            if ( self.map.get_char_at(position.add(direction)) == this_plant):
              result.append ( position.add(direction))

        return result
    

    def price_for_fences ( self ) :
        result = 0

        for index in range(len (self.map.content)):
            coordinates = self.map.coordinates_for_index(index)
            if ( not self.has_been_visited(coordinates)):
                region_data = self.get_data_of_region ( coordinates )
                result += region_data['area'] * region_data['perimeter']
                
        return result

