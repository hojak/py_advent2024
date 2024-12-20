from adv24Tools.StringMap import StringMap


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
