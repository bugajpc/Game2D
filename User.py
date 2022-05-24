import Player
class User(Player.Player):
    def __init__(self, character, name):
        super().__init__(character)
        self.__name = name
        self.__points = 0
    def AddPoint(self):
        self.__points += 1
    def GetPoints(self):
        return self.__points
    def GetName(self):
        return self.__name
    def Move(self):
        user_input = input("Move: ")
        if user_input == 'w':
            if self._pos_x == 0:
                self._pos_x = 3
            else:
                self._pos_x -= 1
        elif user_input == 's':
            if self._pos_x == 3:
                self._pos_x = 0
            else:
                self._pos_x += 1
        elif user_input == 'a':
            if self._pos_y == 0:
                self._pos_y = 3
            else:
                self._pos_y -= 1
        elif user_input == 'd':
            if self._pos_y == 3:
                self._pos_y = 0
            else:
                self._pos_y += 1
        else:
            print("Wrong input")