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
            self.computers[computer2] = [computer1]
        else:
            self.computers[computer2].append(computer1)



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

            while index1 < len(connected)-1:
                for index2 in range(index1+1, len(connected)):
                    if ( self.has_connection(connected[index1], connected[index2])):
                        result.append(computer + ',' + connected[index1] + ',' + connected[index2])
                index1 += 1

        return result
    
    def find_triples_with_t_computer(self):
        triples = self.find_triples()
        return list(filter(has_a_t_computer, triples))
    
    def find_max_clique(self):
        computers = set(self.get_computers())

        max_clique = list(self.bron_kerbosch_max_clique(set([]),computers,set([])))
        max_clique.sort()

        return ','.join(max_clique)


    def bron_kerbosch_max_clique(self, R: set, P: set, X: set) -> set:
        # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
        if len(P) == 0 and len(X) == 0:
            return R
    
        result = set()
    
        for v in P.copy():
            sub_P = P.intersection(set(self.computers[v]))
            sub_X = X.intersection(set(self.computers[v]))
            sub_R = R.copy()
            sub_R.add(v)

            sub_result = self.bron_kerbosch_max_clique(sub_R, sub_P, sub_X)

            if ( len(sub_result) > len(result)):
                result = sub_result

            P.remove(v)
            X.add(v)

        return result


def has_a_t_computer(triple):
    computers = triple.split(',')
    return computers[0][0]=='t' or computers[1][0]=='t' or computers[2][0]=='t'