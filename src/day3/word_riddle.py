
class WordRiddle:
    content: str
    width: int

    def __init__(self, init_str):
        self.content = init_str.replace('\n', '')
        found = init_str.find('\n')
        if (found >= 0):
            self.width = found
        else:
            self.width = len(init_str)


    def get_width(self) -> int:
        return self.width


