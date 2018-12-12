from src.Controller import *


def main():
    c = Controller()
    c.readFromFile("data")
    c.computeFirstOfGramar()


if __name__ == "__main__":
    main()
    print("hello world")
