from src.Production import *
import src.Gramar

class Automata:

    def __init__(self):
        self.states = []
        self.alphabet = []
        self.finalStates = []
        self.startingSymbol = ''
        self.transitions = []

    def transformToGrammar(self):
        g = src.Gramar.Grammar()
        g.startingSymbol = self.startingSymbol
        g.nodes = self.states
        g.terminals = self.alphabet
        for transition in self.transitions:
            p = Production()
            p.lhd = transition.fromState
            p.rhd = []
            p.rhd.append(transition.alpha)
            p.rhd.append(transition.toState)
            g.productions.append(p)

        for p in g.productions:
            print(p)
