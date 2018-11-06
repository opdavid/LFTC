class Transition:

    def __init__(self):
        self.fromState = ''
        self.alpha = ''
        self.toState = ''

    def __str__(self):
        s = "("
        s += self.fromState + ","
        s += self.alpha + ") = "
        s += self.toState

        return s
