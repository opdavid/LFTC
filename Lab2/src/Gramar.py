class Gramar:

    def __init__(self):
        self.nodes = []
        self.terminals = []
        self.productions = []

    def getProductionsFor(self, non_terminal):
        for p in self.productions:
            print(p.lhd + " " + non_terminal)
            print(p.lhd == non_terminal)
            if p.lhd == non_terminal:
                print(p.lhd)

    def verifyIfRegular(self):
        pass
