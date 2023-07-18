#Sidney & Kenyatta Battleship
import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def makelo(board):
    return random.randint(1, len(board)), random.randint(1, len(board[0]))

def UserInput(grid):
    while(True):
        try:
            GuessRow = eval(input("\nGuess Row: "))
            GuessColumn = eval(input("Guess Col: "))
            
            if GuessColumn <= grid and GuessRow <= grid:
                return GuessRow-1, GuessColumn-1
            else:
                print("Seems like you're aiming for failure. Try again...\n")
        except: 
            print("Aim inside the grid.\n")
        

grid = int(input("Grid Size:"))

board = []
for i in range(grid):
    board.append(["O"] * grid)


print("Let's Play Battleship!\n")


ship_row, ship_col = makelo(board) 
print(ship_row, ship_col)

for LAUNCH in range(4):

    if LAUNCH == 3:
        print("Game Over.")
        board[GuessRow][GuessColumn] = "X"
        break
    
    print("Launch", LAUNCH + 1)
    print_board(board)
    
    GuessRow, GuessColumn = UserInput(grid)

    if GuessRow + 1 == ship_row and GuessColumn + 1 == ship_col:
        print("\nWow! You sunk my ship!")
        board[GuessRow][GuessColumn] = "X"
        print_board(board)
        print("")
        break
    
    else:
        if board[GuessRow][GuessColumn] == "--":
            print("\nYou already guessed that :|.")
            print(" ")
        else:
            print("\n Haha you missed!")
            board[GuessRow][GuessColumn] = "--"