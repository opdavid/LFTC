from src.domain.Automata import Automata
from src.Transition import Transition


class Grammar:

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
            if len(p.rhd) > 1 and p.rhd[1] is self.startingSymbol:
                return False
            if len(p.rhd) > 2:
                return False
        return True

    def transformToFA(self):
        a = Automata()
        a.states = self.nodes
        a.alphabet = self.terminals
        a.finalStates = []
        for non_terminal in self.nodes:
            for production in self.getProductionsFor(non_terminal):
                t = Transition()
                t.fromState = production.lhd
                t.alpha = production.rhd[0]
                if len(production.rhd) == 1:
                    t.toState = 'K'
                else:
                    t.toState = production.rhd[1]
                if production.rhd[0] is 'e':
                    a.finalStates.append(production.lhd)
                a.transitions.append(t)
        return a
