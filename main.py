import Board
import User
B1 = Board.Board()
B1.Display()
B1.SetPosition('x', 0, 1)
B1.Display()
B1.Reset()
B1.SetPosition('o', 0, 2)
B1.Display()

U1 = User.User('X', "player1")

while True:
    print(U1.GetPosX())
    print(U1.GetPosY())
    U1.Move()

# dodanie/zmiana plików repozytorium
# git status
# git add .
# git commit -m "..."
# git push -u origin master



