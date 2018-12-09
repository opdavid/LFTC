import re

from domain.CodingTable import CodingTable
from domain.Pair import Pair
from domain.SimbolTable import SimbolTable
from src.Grammar import Grammar
from src.Production import Production


class Controller:

    def __init__(self):
        self.ST = SimbolTable(Pair("root", -1))
        self.CT = CodingTable()
        self.numberRegex = re.compile('[0-9]')
        self.identRegex = re.compile('\w')
        self.PIF = []
        self.reservedWords = ["begin", "end", "program", "and", "not", "or", "for", "else", "if", "then", "do", "read",
                              "while", "write", "integer", "var", "array", "declare"]
        self.compound = ["<"]
        self.grammar = Grammar()

    def readFromFile(self, filename):
        count = 1
        with open(filename, "r") as f:
            self.grammar.nodes = f.readline().rstrip('\n').split(',')
            self.grammar.terminals = f.readline().rstrip('\n').split(',')
            self.grammar.startingSymbol = f.readline().rstrip('\n')
            line = f.readline().rstrip('\n')
            for char in line:
                self.grammar.input.append(char)
            print(self.grammar.input)
            for line in f:
                line = line.rstrip('\n').split('-')
                p = Production()
                lhd = line[0].split(' ')[0]
                p.lhd = lhd
                rhd = line[1].rstrip('\n').split()
                p.rhd = rhd
                self.grammar.productions.append(p)

        print(self.grammar)
