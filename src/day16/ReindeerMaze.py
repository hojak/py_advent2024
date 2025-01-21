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
        return self.paths_to_finish_with_lowest_score()[0].score()
    
    def paths_to_finish_with_lowest_score(self):
        queue = [ReindeerPath(self.reindeer_position, self.reindeer_heading)]
        maze_field_scores = {}
        fixed_score = -1

        current_path = queue.pop(0)
        result = []

        iteration = 0

        while current_path != None and (fixed_score == -1 or current_path.score() <= fixed_score):
            iteration += 1

            if ( iteration % 2500 == 0):
                print ( str(iteration) + ": " + str(len(maze_field_scores)) 
                       + " of possibly " + str(self.get_height() * self.get_width()) 
                       + " have a score, current score: " + str( current_path.score()) 
                       + "   queue: " + str(len(queue)) )

            if current_path.end_position == self.end_position:
                result.append(current_path)
                fixed_score = current_path.score()
            elif ( not current_path.end_position in maze_field_scores or maze_field_scores[current_path.end_position] >= current_path.score()
                or current_path.steps[-1] != ReindeerPath.Step.forward):                    

                maze_field_scores[current_path.end_position] = current_path.score()
                
                possible_steps = self.possible_next_steps(current_path)
                possible_next_paths = list(map(lambda step: current_path.add_step(step), possible_steps))
                                        
                queue = merge_lists_of_paths ( queue, possible_next_paths )

            if len(queue) > 0: 
                current_path = queue.pop(0)
            else:
                current_path = None
        return result
    
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
    
    def get_number_of_interesting_path_coordinates(self):
        possible_paths = self.paths_to_finish_with_lowest_score()

        set_of_coordinates = set([])
        for path in possible_paths:
            set_of_coordinates |= path.touched_coordinates()

        return len ( set_of_coordinates)

class ReindeerPath:

    def __init__(self, end_position, end_heading, list_of_steps = []):
        self.end_position = end_position
        self.end_heading = end_heading
        self.steps = list_of_steps
        self.cached_score = None

    def score(self):
        if self.cached_score == None:
            self.cached_score = self.compute_score()
        return self.cached_score
    
    def compute_score(self):
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
    
    def __str__(self):
        return "".join( map(lambda step: str(step), self.steps))
    
    def touched_coordinates(self):
        touched = [self.end_position]

        current_position = self.end_position
        current_heading = self.end_heading

        for step in self.steps[::-1]:
            match step:
                case ReindeerPath.Step.forward:
                    current_position = current_position.sub(current_heading.value)
                    touched.append(current_position)
                case ReindeerPath.Step.turn_left:
                    current_heading = current_heading.rotate_right()
                case ReindeerPath.Step.turn_right:
                    current_heading = current_heading.rotate_left()

        return set(touched)

    class Step (Enum):
        forward = 1
        turn_left = 2
        turn_right = 3

        def __str__(self):
            match ( self ):
                case ReindeerPath.Step.forward: return "^"
                case ReindeerPath.Step.turn_left: return "<"
                case ReindeerPath.Step.turn_right: return ">"

def merge_lists_of_paths(list1, list2):
    ## assumption: both lists are sorted
    ## assumption: list2 has 0 to 3 elements
    if (len(list1) == 0):
        return list2
    if ( len(list2) == 0):
        return list1

    index1 = 0
    result = list1

    for item in list2:
        while ( index1 < len(list1) and item.score() >= list1[index1].score()):
            index1+=1
        result.insert (index1, item)
        
    return result