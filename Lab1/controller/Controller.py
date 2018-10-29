import re
from domain.SimbolTable import SimbolTable
from domain.CodingTable import CodingTable


class Controller:

    def __init__(self):
        self.ST = SimbolTable(-1)
        self.CT = CodingTable()
        self.numberRegex = re.compile('[0-9]')
        self.identRegex = re.compile('\w')
        self.reservedWords = ["begin", "end", "program", "and", "not", "or", "for", "else", "if", "then", "do", "read",
                              "while", "write", "integer", "var", "array"]

    def readFromFile(self, filename):
        with open(filename, "r") as f:
            for line in f:
                token_list = re.split('(\W)', line)
                for token in token_list:
                    if token != '\n' and token != ' ' and token != '':
                        if self.numberRegex.match(token):
                            self.ST.insert_val(self.CT.get_value_for_key("constant"))
                        elif token in self.reservedWords:
                            self.ST.insert_val(self.CT.get_value_for_key(token))
                        elif self.identRegex.match(token):
                            self.ST.insert_val(self.CT.get_value_for_key("identifier"))
                        else:
                            try:
                                code = self.CT.get_value_for_key(token)
                                self.ST.insert_val(code)
                            except Exception:
                                print("Invalid token: " + token)
                        # print(token)
        print(self.ST.display(self.ST))
