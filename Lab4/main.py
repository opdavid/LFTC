from src.Controller import *


def main():
    c = Controller()
    c.readFromFile("data")
    c.computeFirstOfGrammar()
    c.computeFollowOfGrammar()
    c.computeTable()
    c.analize()


if __name__ == "__main__":
    main()
    print("hello world")
