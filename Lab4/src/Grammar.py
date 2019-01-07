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
        self.follow = {}
        self.table = {}

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

    def computeFollow(self):
        f = {}
        for node in self.nodes:
            f[node] = []
        f[self.startingSymbol].append('e')

        for node in self.nodes:
            for production in self.productions:
                if node in production.rhd:
                    i = 0
                    while i < len(production.rhd):
                        # print(1)
                        if node == production.rhd[i] and i + 1 < len(production.rhd):
                            if production.rhd[i + 1] in self.terminals:
                                f[node].append(production.rhd[i + 1])
                            else:
                                for elem in self.first[production.rhd[i + 1]]:
                                    f[node].append(elem)
                                for elem in f[production.lhd]:
                                    f[node].append(elem)
                        else:
                            if node == production.rhd[i] and node != production.lhd:
                                for elem in f[production.lhd]:
                                    f[node].append(elem)
                        i += 1

        for node in self.nodes:
            for elem in f[node]:
                f[node] = list(set(f[node]))
        self.follow = copy.deepcopy(f)

    def computeTable(self):
        table = {}
        reun = self.terminals + self.nodes + ['e']
        for row in reun:
            for col in self.terminals + ['e']:
                table[(row, col)] = []
                if col == row:
                    table[(row, col)].append("pop")

        i = 0
        for production in self.productions:
            i += 1
            check = 0
            if 'e' not in self.first[production.lhd]:
                for elem in self.first[production.lhd]:
                    if elem in production.rhd:
                        table[(production.lhd, elem)].append((production.rhd, i))
                        check = 1
            if check == 0:
                if 'e' not in production.rhd:
                    for elem in self.first[production.lhd]:
                        if elem != 'e':
                            table[(production.lhd, elem)].append((production.rhd, i))
                else:
                    for elem in self.follow[production.lhd]:
                        table[(production.lhd, elem)].append((production.rhd, i))
            # del first[production.lhd][-1]

        table[('e', 'e')] = "acc"
        self.table = copy.deepcopy(table)
