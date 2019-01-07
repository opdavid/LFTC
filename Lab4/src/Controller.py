from src.Grammar import Grammar
from src.Production import Production
from src.Stack import Stack


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

    def computeFirstOfGrammar(self):
        self.grammar.computeFirst()
        # print(self.grammar.first)

    def computeFollowOfGrammar(self):
        self.grammar.computeFollow()
        # print(self.grammar.follow)

    def computeTable(self):
        self.grammar.computeTable()
        print(self.grammar.table)

    def analize(self):
        initialStack = Stack()
        workingStack = Stack()
        output = []
        initialStack.push(')')
        initialStack.push('a')
        initialStack.push('+')
        initialStack.push('a')
        initialStack.push('(')
        initialStack.push('*')
        initialStack.push('a')
        workingStack.push(self.grammar.startingSymbol)
        print(initialStack.isEmpty())
        while not initialStack.isEmpty():
            print(workingStack.peek(), initialStack.peek())
            print(self.grammar.table[(workingStack.peek(), initialStack.peek())])
            if self.grammar.table[(workingStack.peek(), initialStack.peek())][0] == 'pop':
                workingStack.pop()
                initialStack.pop()
            else:
                if len(self.grammar.table[(workingStack.peek(), initialStack.peek())]) > 0:
                    l = self.grammar.table[(workingStack.peek(), initialStack.peek())][0][0]
                    print(l)
                    nr = self.grammar.table[(workingStack.peek(), initialStack.peek())][0][1]
                    print(nr)
                    workingStack.pop()
                    while l:
                        workingStack.push(l[-1])
                        del l[-1]

                    output.append(nr)

        print(output)



