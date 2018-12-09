class Grammar:

    def __init__(self):
        self.nodes = []
        self.terminals = []
        self.startingSymbol = ''
        self.productions = []
        self.input = []

    def __str__(self):
        print(self.nodes)
        print(self.terminals)
        print(self.startingSymbol)
        print(self.input)
        for p in self.productions:
            print(p)
        return ""
