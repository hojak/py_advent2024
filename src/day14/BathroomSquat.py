from day14.Roboter import Roboter
from adv24Tools.Coordinates import Coordinates
import math

class BathroomSquat:
    robots = []
    floor_size : Coordinates

    def __init__(self, init_string, floor_size = Coordinates(11,7)):
        for robot_line in init_string.split ("\n"):
            self.robots.append ( Roboter.parse_line(robot_line))

        self.floor_size = floor_size


    def march(self, number_of_seconds):
        for robot in self.robots:
            robot.walk(number_of_seconds, self.floor_size)



    def number_of_robots_in_quadrant(self, quadrant):
        quadrant_start_positions = [
            Coordinates(0,0),
            Coordinates(self.floor_size.x-math.floor (self.floor_size.x / 2), 0),
            Coordinates(0, self.floor_size.y-math.floor (self.floor_size.y / 2)),
            Coordinates(self.floor_size.x-math.floor (self.floor_size.x / 2), self.floor_size.y-math.floor (self.floor_size.y / 2)),
        ]
        result = 0

        top_left = quadrant_start_positions[quadrant]
        bottom_right = Coordinates(math.floor (self.floor_size.x / 2)-1, math.floor (self.floor_size.y / 2)-1).add ( top_left)

        for robot in self.robots:
            if robot.position.is_in_box ( top_left,bottom_right ):
                result += 1

        return result
    
    def safety_factor ( self ):
        result = 1
        for quadrant in range(4):
            result *= self.number_of_robots_in_quadrant(quadrant)

        return result