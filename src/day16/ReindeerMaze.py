from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates
from enum import Enum

class ReindeerMaze(StringMap):

    start_position_char = "S"
    end_position_char = "E"
    free_char = '.'
    class Headings(Enum):
        east = Coordinates(1,0)
        west = Coordinates(-1,0)
        north = Coordinates(0, -1)
        south = Coordinates(0, 1)

        def rotate_right(self):
            match (self):
                case ReindeerMaze.Headings.east: return ReindeerMaze.Headings.south
                case ReindeerMaze.Headings.south: return ReindeerMaze.Headings.west
                case ReindeerMaze.Headings.west: return ReindeerMaze.Headings.north
                case ReindeerMaze.Headings.north: return ReindeerMaze.Headings.east

        def rotate_left(self):
            match (self):
                case ReindeerMaze.Headings.east: return ReindeerMaze.Headings.north
                case ReindeerMaze.Headings.south: return ReindeerMaze.Headings.east
                case ReindeerMaze.Headings.west: return ReindeerMaze.Headings.south
                case ReindeerMaze.Headings.north: return ReindeerMaze.Headings.west


    def __init__(self, map):
        super().__init__(map)

        self.start_position = self.get_coordinates_for(ReindeerMaze.start_position_char)
        self.end_position = self.get_coordinates_for(ReindeerMaze.end_position_char)
        self.reindeer_position = self.start_position
        self.reindeer_heading = ReindeerMaze.Headings.east

    def lowest_score_for_path_to_finish(self):
        queue = [ReindeerPath(self.reindeer_position, self.reindeer_heading)]

        current_path = queue.pop()

        while current_path.end_position != self.end_position:
            possible_steps = self.possible_next_steps(current_path)
        
            for possible in possible_steps: 
                queue.append ( current_path.add_step(possible) )

            current_path= queue.pop()

        return current_path.score()
    
    def is_free(self, coordinates):
        return self.get_char_at(coordinates) == ReindeerMaze.free_char or self.get_char_at(coordinates) == ReindeerMaze.end_position_char


    def possible_next_steps(self, path_so_far):
        result = []

        if ( self.is_free (path_so_far.end_position.add(path_so_far.end_heading.value))):
            result.append( ReindeerPath.Step.forward)

        if ( len(path_so_far.steps) == 0):
            result += [ReindeerPath.Step.turn_left, ReindeerPath.Step.turn_right]
        
        elif (path_so_far.steps[-1] == ReindeerPath.Step.forward):
            result += [ReindeerPath.Step.turn_left, ReindeerPath.Step.turn_right]

        if ( len(path_so_far.steps) == 1 and path_so_far.steps[0] == ReindeerPath.Step.turn_right):
            result += [ReindeerPath.Step.turn_right]
        

        return result

class ReindeerPath:

    def __init__(self, end_position, end_heading, list_of_steps = []):
        self.end_position = end_position
        self.end_heading = end_heading
        self.steps = list_of_steps

    def score(self):
        return len([step for step in self.steps if step == ReindeerPath.Step.forward]) + \
            1000 * len([step for step in self.steps if step != ReindeerPath.Step.forward])
    
    def add_step (self, step):
        match step:
            case ReindeerPath.Step.forward:
                return ReindeerPath( self.end_position.add(self.end_heading.value), self.end_heading, self.steps + [step])
            case ReindeerPath.Step.turn_left:
                return ReindeerPath( self.end_position, self.end_heading.rotate_left(), self.steps + [step])
            case ReindeerPath.Step.turn_right:
                return ReindeerPath( self.end_position, self.end_heading.rotate_right(), self.steps + [step])
    
    class Step (Enum):
        forward = 1
        turn_left = 2
        turn_right = 3