import Board
import User
import Goal
import os
class Game:
    def __init__(self, p_chr, p_name, g_chr):
        self.__UserObject = User.User(p_chr, p_name)
        self.__GoalObject = Goal.Goal(g_chr)
        self.__BoardObject = Board.Board()
    def Play(self):
        # starting positions
        self.__UserObject.SetPosition(2, 1)
        self.__GoalObject.SetPosition(0, 2)

        while self.__UserObject.GetPoints() < 5:
            os.system("cls")
            self.__BoardObject.Reset()
            print(self.__UserObject.GetPoints())
            self.__BoardObject.SetPosition(self.__UserObject.GetCharacter(), self.__UserObject.GetPosX(), self.__UserObject.GetPosY())
            self.__BoardObject.SetPosition(self.__GoalObject.GetCharacter(), self.__GoalObject.GetPosX(), self.__GoalObject.GetPosY())
            self.__BoardObject.Display()
            self.__UserObject.Move()
            if(self.CheckCollision()):
                self.__UserObject.AddPoint()
                self.__GoalObject.Move()

    def CheckCollision(self):
        if self.__UserObject.GetPosX() == self.__GoalObject.GetPosX() and self.__UserObject.GetPosY() == self.__GoalObject.GetPosY():
            return True
        else:
            return False