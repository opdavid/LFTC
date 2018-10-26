import re
from domain.SimbolTable import SimbolTable


class Controller:

    def __init__(self):
        ST = SimbolTable("zor")
        for i in ["ana", "gama", "cri", "fic"]:
            ST.insert_val(i)

        print(ST.display(ST))

    def readFromFile(self, filename):
        with open(filename, "r") as f:
            for line in f:
                l = re.split('(\W)', line)
                print(l)
                # for token in l:
                #     if token != '\n' or token != ' ' or token != '':
                #         print(token)
