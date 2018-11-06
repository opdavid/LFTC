from src.Automata import Automata
from src.Transition import Transition


class Gramar:

    def __init__(self):
        self.nodes = []
        self.terminals = []
        self.startingSymbol = ''
        self.productions = []

    def getProductionsFor(self, non_terminal):
        # print(non_terminal)
        # print(self.startingSymbol)
        # l = self.productions[0].lhd[0]
        # print(l)
        # print(non_terminal is l)
        prodList = []
        for p in self.productions:
            l = p.lhd[0]
            if non_terminal is l:
                prodList.append(p)
        return prodList

    def verifyIfRegular(self):
        pass

    def transformToFA(self):
        a = Automata()
        a.states = self.nodes
        a.alphabet = self.terminals
        for non_terminal in self.nodes:
            for production in self.getProductionsFor(non_terminal):
                t = Transition()
                t.fromState = production.lhd
                t.alpha = production.rhd[0]
                if len(production.rhd) == 1:
                    t.toState = 'K'
                else:
                    t.toState = production.rhd[1]
                a.transitions.append(t)
        return a
