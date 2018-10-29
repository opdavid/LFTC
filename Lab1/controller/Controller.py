import re
from domain.SimbolTable import SimbolTable
from domain.CodingTable import CodingTable
from domain.Pair import Pair


class Controller:

    def __init__(self):
        self.ST = SimbolTable(-1)
        self.CT = CodingTable()
        self.numberRegex = re.compile('[0-9]')
        self.identRegex = re.compile('\w')
        self.PIF = []
        self.reservedWords = ["begin", "end", "program", "and", "not", "or", "for", "else", "if", "then", "do", "read",
                              "while", "write", "integer", "var", "array", "declare"]

    def readFromFile(self, filename):
        count = 1
        with open(filename, "r") as f:
            for line in f:
                token_list = re.split('(\W)', line)
                for token in token_list:
                    if token != '\n' and token != ' ' and token != '':
                        if self.numberRegex.match(token):
                            self.ST.insert_val(Pair(token, count))
                            self.PIF.append(Pair(self.CT.get_value_for_key("constant"), count))
                            count += 1
                        elif token in self.reservedWords:
                            self.PIF.append(Pair(self.CT.get_value_for_key(token), -1))
                        elif self.identRegex.match(token):
                            self.ST.insert_val(Pair(token, count))
                            self.PIF.append(Pair(self.CT.get_value_for_key("identifier"), count))
                            count += 1
                        else:
                            try:
                                code = self.CT.get_value_for_key(token)
                                # self.ST.insert_val(code)
                            except Exception:
                                print("Invalid token: " + token)
                        # print(token)
        for a in self.PIF:
            print(a)
        print("******************************************\n")
        for a in self.ST.display(self.ST):
            print(a)
