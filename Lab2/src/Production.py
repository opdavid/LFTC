class Production:
    def __init__(self):
        self.lhd = ''
        self.rhd = []

    def __str__(self):
        s = ""
        s += self.lhd + " - "
        for x in self.rhd:
            s += x
            s += ' '
        return s
