import Board
import User
import Goal
import Game
B1 = Board.Board()
B1.Display()
B1.SetPosition('x', 0, 1)
B1.Display()
B1.Reset()
B1.SetPosition('o', 0, 2)
B1.Display()

U1 = User.User('X', "player1")
print("Points test")
U1.AddPoint()
U1.AddPoint()
U1.AddPoint()
print(U1.GetPoints())

G1 = Goal.Goal('o')
print("Goal position check")
print(G1.GetPosX())
print(G1.GetPosY())
G1.Move()
print(G1.GetPosX())
print(G1.GetPosY())

Game1 = Game.Game('X', 'player1', 'o')
Game1.Play()




# dodanie/zmiana plików repozytorium
# git status
# git add .
# git commit -m "..."
# git push -u origin master



