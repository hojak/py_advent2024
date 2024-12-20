from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import directions


class RaceMap (StringMap):

    def __init__(self, map):
        super().__init__(map)

        index = str.find(self.content, 'S')
        self.start_position = self.coordinates_for_index(index)
        self.set_char_at(self.start_position, StringMap.CHAR_FREE)

        index = str.find(self.content, 'E')
        self.end_position = self.coordinates_for_index(index)
        self.set_char_at(self.end_position, StringMap.CHAR_FREE)


    def start(self):
        return self.start_position

    def end(self):
        return self.end_position
    

    def length_of_cheat ( self, cheat_start, cheat_end):
        if not self.is_accessible(cheat_end):
            return -1
        
        return self.length_of_path(cheat_end, self.end()) + 2 
    
    def number_of_possible_cheats ( self ):
        CHAR_MARKER = 'o'

        if ( not self.is_accessible(self.start())):
            return 0
        
        number_of_cheats = 0
        
        queue = [(self.start(), 0)]
        while len(queue) > 0:
            (current_position, steps_till_here) = queue.pop(0) # shift

            if ( not self.is_accessible ( current_position)):
                continue

            if ( current_position == self.end()):
                self.content = self.content.replace(CHAR_MARKER, StringMap.CHAR_FREE)
                return number_of_cheats

            self.set_char_at(current_position, CHAR_MARKER)

            for direction in directions:
                next = current_position.add(direction)
                if ( self.is_accessible(next)):
                    queue.append( (next, steps_till_here+1))
                elif self.is_possible_cheat ( current_position, direction ):
                    number_of_cheats += 1

        self.content = self.content.replace(CHAR_MARKER, StringMap.CHAR_FREE)      
        return number_of_cheats
    

    def is_possible_cheat ( self, position, direction ):
        if not self.is_within_bounds(position.add(direction) or not self.is_within_bounds(position.add(direction.mul(2)))):
            return False
        
        if self.get_char_at(position.add(direction)) != StringMap.CHAR_BLOCK:
            return False
        
        if not self.is_accessible(position.add(direction.mul(2))):
            return False
        
        path_to_go = self.length_of_path(position.add(direction.mul(2)), self.end())

        return path_to_go >= 0


    def print_cheat(self, position, direction):
        out = StringMap(self.__str__())
        out.set_char_at(position.add(direction), "1")
        out.set_char_at(position.add(direction.mul(2)), "2")
        print ( out.__str__())
        print ("------------------")
    
