import math
import re


class GuardStatus:
    x : int
    y : int
    orientation : str

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation


    def __eq__(self, other): 
        return self.x == other.x and self.y == other.y and self.orientation == other.orientation
    
    def __str__(self):
        return f"({self.x}|{self.y}|{self.orientation})"
    
    def get_next_position(self) -> tuple[int,int]: 
        match self.orientation:
            case '<': return self.x-1, self.y
            case '>': return self.x+1, self.y
            case '^': return self.x, self.y-1
            case 'v': return self.x, self.y+1

        return self.x,self.y
    
    def turn_right(self) :
        match self.orientation:
            case '<': return GuardStatus(self.x, self.y, '^')
            case '>': return GuardStatus(self.x, self.y, 'v')
            case '^': return GuardStatus(self.x, self.y, '>')
            case 'v': return GuardStatus(self.x, self.y, '<')
        
        return self

        


class LabMap:

    content: str
    trail: str
    width: int
    height: int
    guard_status: GuardStatus

    def __init__(self, init_str):
        self.content = init_str.replace('\n', '')
        found = init_str.find('\n')
        if (found >= 0):
            self.width = found
        else:
            self.width = len(init_str)
        self.height = math.ceil(len(self.content) / self.width)
        
        self.init_guard_status()
        self.init_trail()

    def init_trail ( self ) :
        self.trail = ' ' * len ( self.content )
        self.mark_guard_position()

    def mark_guard_position(self):
        guard_index = self.get_index_for_coordinates(self.guard_status.x, self.guard_status.y)
        self.trail = self.trail[0:guard_index] + 'X' + self.trail[guard_index+1:]        

    def init_guard_status(self):
        re_result = re.search(r'[v^<>]', self.content)

        if ( re_result == None ):
            raise Exception ("No start position found")
        
        (x,y) = self.get_coordinates_for_index( re_result.start() )
        self.guard_status = GuardStatus(x,y,re_result.group())

        self.content = self.content[:re_result.start()] + '.' + self.content[re_result.start()+1:]

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def __str__(self):
        guard_index = self.get_index_for_coordinates ( self.guard_status.x, self.guard_status.y )

        content_with_guard = self.content[:guard_index] + self.guard_status.orientation + self.content[guard_index+1:]

        # insert line breaks
        return self.break_lines(content_with_guard)
    
    def break_lines ( self, content ): 
        return re.sub('(.{'+str(self.get_width())+'})',r'\1\n', content)[:-1]

    def get_trail (self):
        return self.break_lines ( self.trail )
    
    def get_trail_length(self):
        return len (re.sub('[^X]','',self.get_trail())) 
    
    def get_guard_status(self):
        return self.guard_status
    
    def get_coordinates_for_index ( self, index ):
        return index % self.width, math.floor(index / self.width)
    
    def get_index_for_coordinates(self, x: int, y: int) -> int:
        return x + y * self.width
    
    def walk_guard(self):
        next_x, next_y = self.guard_status.get_next_position()
        
        if ( self.is_out_of_bounds ( next_x, next_y)):
            return False

        if ( self.is_occupied ( next_x, next_y ) ):
            self.guard_status = self.guard_status.turn_right()
        else:
            self.guard_status = GuardStatus(next_x, next_y, self.guard_status.orientation)
            self.mark_guard_position()

        return True

    def is_occupied ( self, x, y) -> bool :
        return self.content[self.get_index_for_coordinates(x,y)] == '#'
    
    def is_out_of_bounds (self, x, y ) -> bool :
        return x<0 or y<0 or x>=self.width or y >= self.height
    
    def run_patrol ( self ): 
        while ( self.walk_guard() ):
            pass

    def ends_in_loop ( self ) -> bool:
        already_visited = {}

        while (self.walk_guard()):
            current_index = self.get_index_for_coordinates ( self.guard_status.x, self.guard_status.y)
            if ( not current_index in already_visited ):
                already_visited[current_index] = [self.guard_status.orientation]
            elif ( not self.guard_status.orientation in already_visited[current_index] ):
                already_visited[current_index].append(self.guard_status.orientation)
            else:
                return True
            
        return False
    

    def is_next_posistion_a_possible_loop_obstacle(self) -> bool:
        next_guard_x, next_guard_y = self.guard_status.get_next_position()

        if ( self.is_occupied ( next_guard_x, next_guard_y )):
            return False

        map_to_check = self.__str__()
        next_index = self.get_index_for_coordinates(next_guard_x, next_guard_y)
        map_to_check = map_to_check[:next_index+1] + '#' +map_to_check[next_index+2:]

        map = LabMap ( map_to_check )

        return map.ends_in_loop()


