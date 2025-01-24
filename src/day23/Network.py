class Network:

    def __init__(self, description):
        self.computers = {}

        for line in description.strip().split('\n'):
            self.register_connection(line)

    def register_connection(self, line):
        (computer1, computer2) = line.split('-')

        if ( computer2 < computer1 ):
            (computer1, computer2) = (computer2, computer1)

        if ( not computer1 in self.computers):
            self.computers[computer1] = [computer2]
        else:
            self.computers[computer1].append(computer2)

        if ( not computer2 in self.computers):
            self.computers[computer2] = []


    def get_computers(self):
        return self.computers.keys()
    
    def has_connection(self, computer1, computer2):
        if ( computer2 < computer1):
            return self.has_connection(computer2, computer1)
        
        return computer1 in self.computers and computer2 in self.computers[computer1]
    
    def find_triples(self):
        result = []

        computers = list(self.get_computers())
        computers.sort()

        for computer in computers:
            connected = self.computers[computer]
            connected.sort()

            index1 = 0
            while index1 < len(connected) and connected[index1] < computer:
                index1+=1

            for index2 in range(index1+1, len(connected)-1):
                if ( self.has_connection(connected[index1], connected[index2])):
                    result.append(computer + ',' + connected[index1] + ',' + connected[index2])

        return result