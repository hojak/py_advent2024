from adv24Tools.StringMap import StringMap
from adv24Tools.Coordinates import Coordinates
from enum import Enum

class ReindeerMaze(StringMap):

    start_position_char = "S"
    end_position_char = "E"
    class Headings(Enum):
        east = Coordinates(1,0)

    def __init__(self, map):
        super().__init__(map)

        self.start_position = self.get_coordinates_for(ReindeerMaze.start_position_char)
        self.end_position = self.get_coordinates_for(ReindeerMaze.end_position_char)
        self.reindeer_position = self.start_position
        self.reindeer_heading = ReindeerMaze.Headings.east

    def lowest_score_for_path_to_finish(self):
        queue = [(ReindeerPath([]), self.reindeer_position, self.reindeer_heading)]

        (current_path, current_position, current_heading) = queue.pop()

        while current_position != self.end_position:
            queue.append ( (current_path.add_step(ReindeerPath.Step.forward), current_position.add(current_heading.value), current_heading) )

            (current_path, current_position, current_heading) = queue.pop()

        return current_path.score()


class ReindeerPath:

    def __init__(self, list_of_steps):
        self.steps = list_of_steps

    def score(self):
        return len([step for step in self.steps if step == ReindeerPath.Step.forward]) + \
            1000 * len([step for step in self.steps if step != ReindeerPath.Step.forward])
    
    def add_step (self, step):
        return ReindeerPath(self.steps + [step])
    
    class Step (Enum):
        forward = 1
        turn_left = 2
        turn_right = 3