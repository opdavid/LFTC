class Production:
    def __init__(self):
        self.lhd = ''
        self.rhd = []

    def get_lhd(self):
        return self.lhd

    def __str__(self):
        s = ""
        s += self.lhd + " - "
        for x in self.rhd:
            s += x
            s += ' '
        return s
