from src.Automata import Automata
from src.Transition import Transition


class Gramar:

    def __init__(self):
        self.nodes = []
        self.terminals = []
        self.startingSymbol = ''
        self.productions = []

    def getProductionsFor(self, non_terminal):
        prodList = []
        for p in self.productions:
            if non_terminal is p.lhd:
                prodList.append(p)
        return prodList

    def verifyIfRegular(self):
        for p in self.productions:
            if p.rhd[0] in self.nodes:
                return False
            if p.rhd[0] is 'e' and p.lhd is not self.startingSymbol:
                return False
        return True

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
