from src.Production import Production
import re

class Controller:

    def __init__(self):
        self.nodes = []
        self.terminals = []
        self.productions = []

    def readFromFile(self, filename):
        with open(filename) as f:
            self.nodes = f.readline().rstrip('\n').split(',')
            self.terminals = f.readline().rstrip('\n').split(',')
            for line in f:
                line = line.rstrip('\n').split('-')
                p = Production()
                lhd = line[0]
                p.lhd = lhd
                rhd = line[1].split(' ')
                if '|' in rhd:
                    for x in rhd:
                        if re.match('\w', x) and x != ' ':
                            p1 = Production()
                            p1.lhd = lhd
                            p1.rhd = x
                            self.productions.append(p1)
                else:
                    p.rhd = rhd
                self.productions.append(p)
            print("NODES: ")
            print(self.nodes)
            print("TERMINALS: ")
            print(self.terminals)
            print("PRODUCTIONS: ")
            for p in self.productions:
                print(p)

    def run(self, filename):
        self.readFromFile(filename)
