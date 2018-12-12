import copy
from filecmp import cmp


class Grammar:

    def __init__(self):
        self.nodes = []
        self.terminals = []
        self.startingSymbol = ''
        self.productions = []
        self.input = []
        self.first = {}

    def __str__(self):
        print(self.nodes)
        print(self.terminals)
        print(self.startingSymbol)
        print(self.input)
        for p in self.productions:
            print(p)
        return ""

    def computeFirst(self):
        first = {}
        for node in self.nodes:
            first[node] = []

        self.first = copy.deepcopy(first)

        i = 0
        while True:
            for node in self.nodes:
                for production in self.productions:
                    if production.lhd is node:
                        candidate = production.rhd[0]
                        if candidate in self.terminals or production.rhd[0] is 'e':
                            first.get(node).append(candidate)
                        else:
                            if self.first[candidate]:
                                for x in self.first[candidate]:
                                    first[node].append(x)
                if first[node]:
                    first[node] = list(set(first[node]))

            if self.firstStopCondition(first) and i != 0:
                break
            i = 1
            self.first = copy.deepcopy(first)

    def firstStopCondition(self, first):
        for key in first.keys():
            if set(self.first[key]) != set(first[key]):
                return False
        return True
