class Network:

    def __init__(self, description):
        self.computers = {}

        for line in description.strip().split('\n'):
            self.register_connection(line)

    def register_connection(self, line):
        print ( "line: " + line)
        (computer1, computer2) = line.split('-')

        if ( not computer1 in self.computers):
            self.computers[computer1] = [computer2]
        else:
            self.computers[computer1].append ( computer2 )

        if ( not computer2 in self.computers):
            self.computers[computer2] = [computer1]
        else:
            self.computers[computer2].append ( computer1 )


    def get_computers(self):
        return self.computers.keys()
    

    def has_connection(self, computer1, computer2):
        return computer1 in self.computers and computer2 in self.computers[computer1]