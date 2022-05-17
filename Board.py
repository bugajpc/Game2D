class Board:
    def __init__(self):
        self.__board = [
                [' ',' ',' ',' '],
                [' ',' ',' ',' '],
                [' ',' ','x',' '],
                [' ',' ',' ',' ']]
    def Display(self):
        for x in self.__board:
            for y in x:
                print("[", end="")
                print(y, end="")
                print("]", end="")
            print()
