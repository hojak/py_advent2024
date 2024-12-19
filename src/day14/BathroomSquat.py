from day14.Roboter import Roboter
from adv24Tools.Coordinates import Coordinates
import math

class BathroomSquat:
    robots = []
    field_size = Coordinates(11,7)

    def __init__(self, init_string):
        for robot_line in init_string.split ("\n"):
            self.robots.append ( Roboter.parse_line(robot_line))


    def march(self, number_of_seconds):
        for robot in self.robots:
            robot.walk(number_of_seconds, self.field_size)



    def number_of_robots_in_quadrant(self, quadrant):
        quadrant_start_positions = [
            Coordinates(0,0),
            Coordinates(self.field_size.x-math.floor (self.field_size.x / 2), 0),
            Coordinates(0, self.field_size.y-math.floor (self.field_size.y / 2)),
            Coordinates(self.field_size.x-math.floor (self.field_size.x / 2), self.field_size.y-math.floor (self.field_size.y / 2)),
        ]
        result = 0

        top_left = quadrant_start_positions[quadrant]
        bottom_right = Coordinates(math.floor (self.field_size.x / 2)-1, math.floor (self.field_size.y / 2)-1).add ( top_left)

        for robot in self.robots:
            if robot.position.is_in_box ( top_left,bottom_right ):
                print ( robot.position )
                result += 1

        return result
    
    def safty_factor ( self ):
        result = 1
        for quadrant in range(3):
            result *= self.number_of_robots_in_quadrant(quadrant)

        return result