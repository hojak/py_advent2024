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
        return self.path_to_finish_with_lowest_score().score()
    
    def path_to_finish_with_lowest_score(self):
        queue = [ReindeerPath(self.reindeer_position, self.reindeer_heading)]
        maze_field_scores = {}

        current_path = queue.pop(0)

        while current_path.end_position != self.end_position:
            if ( not current_path.end_position in maze_field_scores or maze_field_scores[current_path.end_position] > current_path.score()
                or current_path.steps[-1] != ReindeerPath.Step.forward):                    

                maze_field_scores[current_path.end_position] = current_path.score()
                
                possible_steps = self.possible_next_steps(current_path)
                possible_next_paths = list(map(lambda step: current_path.add_step(step), possible_steps))
                                        
                queue = merge_lists_of_paths ( queue, possible_next_paths )

            current_path= queue.pop(0)

        return current_path
    
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

def merge_lists_of_paths( list1, list2):
    result = []

    index1 = 0
    index2 = 0

    while ( index1<len(list1) or index2<len(list2)):
        if ( not index1 >= len(list1) and (index2 >= len(list2) or list1[index1].score() <= list2[index2].score())):
            result.append ( list1[index1])
            index1 +=1
        else:
            result.append ( list2[index2])
            index2 +=1
            
    return result