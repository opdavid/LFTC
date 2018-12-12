from src.Grammar import Grammar
from src.Production import Production


class Controller:

    def __init__(self):
        self.grammar = Grammar()

    def readFromFile(self, filename):
        with open(filename, "r") as f:
            self.grammar.nodes = f.readline().rstrip('\n').split(',')
            self.grammar.terminals = f.readline().rstrip('\n').split(',')
            self.grammar.startingSymbol = f.readline().rstrip('\n')
            line = f.readline().rstrip('\n')
            for char in line:
                self.grammar.input.append(char)

            for line in f:
                line = line.rstrip('\n').split('-')
                p = Production()
                lhd = line[0].split(' ')[0]
                p.lhd = lhd
                rhd = line[1].rstrip('\n').split()
                p.rhd = rhd
                self.grammar.productions.append(p)

    def computeFirstOfGramar(self):
        self.grammar.computeFirst()
        print(self.grammar.first)
