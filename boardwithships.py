from random import randint

guesses = 5
num = int(input("Enter your grid size: "))
validRows =  num
validColumns = num
board = []

turn=0 

def print_board(board):
    print ("Let's Play Battleship!")
print_board(board)


for i in range(num):
    board.append(num * ["O"]) # this appends a list of five "O" strings
for z in board:
    print(*z)
    
def shiplocation():
    inputRow = int(input("Place your ship in a row: \n"))
    if inputRow not in range(validRows +1):
            print ("Enter a valid row number.")
            inputRow = input("Place your ship in a row: \n")
    inputColumn = int(input("Place your ship in a column: \n"))
    if inputColumn not in range(validColumns +1):
            print("Enter a valid column number.")
            inputColumn = input("Place your ship in a column: \n")
shiplocation()
print ("Your ship has been placed. Buena Suerte!")

def randomRow(board):
    return randint(0,len(board)-1)

def randomColumn(board):
    return randint(0,len(board)-1)

shipRow=randomRow(board)
shipColumn=randomColumn(board)

print(shipRow)
print(shipColumn)

turn=0
for turn in range(guesses):
    print ("Turn:", turn + 1)
    
    guessRow = int(input("Guess a Row:"))
    guessColumn = int(input("Guess a Column:"))

    if guessRow == shipRow and guessColumn == shipColumn:
        print ("Hit!")
    else:
        if (guessRow not in range(num)) or (guessColumn not in range(num)):
            print ("Enter a Valid Number")
        elif(board[guessRow][guessColumn] == "X"):
            print ("Already Hit")
        else:
            print ("Miss!")
            board[guessRow][guessColumn] = "X"
            print("Try Again")
            
        print_board(board)