from src.Production import Production
from src.Gramar import Gramar
from src.Automata import Automata
from src.Transition import Transition
import re


class Controller:

    def __init__(self):
        self.gramar = Gramar()
        self.automata = Automata()

    def readFromFileGramar(self, filename):
        with open(filename) as f:
            self.gramar.nodes = f.readline().rstrip('\n').split(',')
            self.gramar.terminals = f.readline().rstrip('\n').split(',')
            for line in f:
                line = line.rstrip('\n').split('-')
                p = Production()
                lhd = line[0]
                p.lhd = lhd
                rhd = line[1].rstrip('\n').split()
                if '|' in rhd:
                    for x in rhd:
                        if re.match('[a-zA-Z]', x):
                            p1 = Production()
                            p1.lhd = lhd
                            p1.rhd = x
                            self.gramar.productions.append(p1)
                else:
                    p.rhd = rhd
                    self.gramar.productions.append(p)

    def readFromFileAutomata(self, filename):
        with open(filename) as f:
            self.automata.states = f.readline().rstrip('\n').split(',')
            self.automata.alphabet = f.readline().rstrip('\n').split(',')
            self.automata.finalStates = f.readline().rstrip('\n').split(',')
            for line in f:
                line = line.rstrip('\n').split('=')
                t = Transition()
                rhd = line[1]
                t.toState = rhd
                lhd = line[0].split(',')
                t.fromState = lhd[0].split('(')[1]
                t.alpha = lhd[1].split(')')[0]
                self.automata.transitions.append(t)

    def printMenu1(self):
        print("********************\n")
        print("1. Gramar")
        print("2. Finite automata")
        print("3. Exit")
        print("********************\n")

    def printMenu2(self):
        print("********************\n")
        print("1. Read Gramar")
        print("2. Print Non-terminals")
        print("3. Print Terminals")
        print("4. Print Productions")
        print("5. Print Productions for a Non-terminal")
        print("6. Back")
        print("********************\n")

    def printMenu3(self):
        print("********************\n")
        print("1. Read Automata")
        print("2. Print States")
        print("3. Print alphabet")
        print("4. Print transitions")
        print("5. Print final states")
        print("6. Back")
        print("********************\n")

    def run(self):
        self.readFromFileGramar("data")
        self.readFromFileAutomata("FA")
        while True:
            self.printMenu1()
            try:
                cmd = int(input())
                if cmd == 1:  # Regular Grammar
                    while True:
                        self.printMenu2()
                        try:
                            cmd1 = int(input())
                            if cmd1 == 1:
                                print("read")
                            elif cmd1 == 2:
                                print("NON-TERMINALS: ")
                                print(self.gramar.nodes)
                            elif cmd1 == 3:
                                print("TERMINALS: ")
                                print(self.gramar.terminals)
                            elif cmd1 == 4:
                                print("PRODUCTIONS: ")
                                for p in self.gramar.productions:
                                    print(p)
                            elif cmd1 == 5:
                                non_terminal = input("Give the non-terminal: ")
                                for p in self.gramar.productions:
                                    print(p.lhd + " " + non_terminal)
                                    print(p.lhd == non_terminal)
                                    if p.lhd == non_terminal:
                                        print(p.lhd)
                            elif cmd1 == 6:
                                break
                            else:
                                print("invalid command")
                        except:
                            print("Error")
                            break
                elif cmd == 2:  # Finite Automata
                    while True:
                        self.printMenu3()
                        try:
                            cmd1 = int(input())
                            if cmd1 == 1:
                                print("read")
                            elif cmd1 == 2:
                                print("STATES: ")
                                print(self.automata.states)
                            elif cmd1 == 3:
                                print("ALPHABET: ")
                                print(self.automata.alphabet)
                            elif cmd1 == 4:
                                print("TRANSITIONS: ")
                                for t in self.automata.transitions:
                                    print(t)
                            elif cmd1 == 5:
                                print("FINAL STATES: ")
                                print(self.automata.finalStates)
                            elif cmd1 == 6:
                                break
                            else:
                                print("invalid command")
                        except:
                            print("Error")
                            break
                elif cmd == 3:
                    print("Bye..")
                    break
                else:
                    print("invalid command")
            except:
                print("error")
                break
