class Board:
    def __init__(self):
        self.__board = [
                [' ',' ',' ',' '],
                [' ',' ',' ',' '],
                [' ',' ',' ',' '],
                [' ',' ',' ',' ']]
    def Display(self):
        for x in self.__board:
            for y in x:
                print("[", end="")
                print(y, end="")
                print("]", end="")
            print()
    def Reset(self):
        self.__board = [
                [' ',' ',' ',' '],
                [' ',' ',' ',' '],
                [' ',' ',' ',' '],
                [' ',' ',' ',' ']]
    def SetPosition(self, chr, x, y):
        self.__board[x][y] = chr