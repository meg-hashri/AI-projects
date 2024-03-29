def Costboard(board):
    print("current state of the board")
    for i in range(0, 9):
        if ((i > 0) and (i % 3 == 0)):
            print("\n")
        if (board[i] == 0):
            print("_", end=" ")
        if (board[i] == 1):
            print("O", end=" ")
        if (board[i] == -1):
            print("X", end=" ")
    print("\n\n")

def User1Turn(board):
    pos = int(input("Enter the X's position from [1,2,...,9]"))
    if (board[pos - 1] != 0):
        print("Wrong move")
        exit(0)
    else:
        board[pos - 1] = -1

def User2Turn(board):
    pos = int(input("Enter the O's position from [1,2,...,9]"))
    if (board[pos - 1] != 0):
        print("Wrong move")
        exit(0)
    else:
        board[pos - 1] = 1

def analyzeboard(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if (board[cb[i][0]] != 0 and
            board[cb[i][0]] == board[cb[i][1]] and
            board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][0]];
    return 0;

def minmax(board, player):
    """
    Prioritize defensive moves to block potential wins for the opponent.
    """
    x = analyzeboard(board)
    if (x != 0):
        return (x * player)
    pos = -1
    value = -2  
    for i in range(0, 9):
        if (board[i] == 0):
            board[i] = player;
            score = -minmax(board, player*-1); 
            board[i] = 0 ;
            if (score > value): 
                value = score;
                pos = i;

    if(pos==-1):
      return 0;
    return value;

def CompTurn(board):
    pos = -1
    value = -2
    for i in range(0, 9):
        if (board[i] == 0):
            board[i] = 1;
            score = -minmax(board, -1)
            board[i] = 0;
            if (score > value):
                value = score;
                pos = i;
    board[pos] = 1;

def main():
    choice = int(input("Enter 1 for single player,2 for multiplayer"))
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if (choice == 1):
        print("Computer: O Vs. You: X")
        player = int(input("Enter 1 to play 1st,Enter 2 to play 2nd"))
        for i in range(0, 9):
            if (analyzeboard(board) != 0):
                break
            if ((i + player) % 2 == 0):
               CompTurn(board);
            else:
              Costboard(board);
              User1Turn(board);
    else:
      for i in range(0, 9):
        if (analyzeboard(board) != 0):
          break;
        if (i % 2 == 0):
          Costboard(board);
          User1Turn(board);
        else:
          Costboard(board);
          User2Turn(board);

    x = analyzeboard(board);
    if (x == 0):
       Costboard(board);
       print("DRAW");
    if(x==-1):
      Costboard(board);
      print("PLAYER X WON...");
    if(x==1):
      Costboard(board);
      print("PLAYER O WON...");
