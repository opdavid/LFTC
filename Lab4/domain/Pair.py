class Pair:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __lt__(self, other):
        if type(self) is type(other):
            return self.first < other.first
        elif isinstance(other, str) and isinstance(self.first, int):
            return True
        elif isinstance(other, int) and isinstance(self.first, str):
            return False

    def __str__(self):
        st = ""
        st += ' ' + str(self.first)
        st += ', ' + str(self.second)
        return st

    def getFirst(self):
        return self.first

    def getSecond(self):
        return self.second
