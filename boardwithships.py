
from random import randint

NO_USER_GUESS=5

num = int(input("Enter your grid size: "))

board = []

def print_board(board):
    print ("Let's Play Battleship!")
print_board(board)


for i in range(num):
    board.append(num * ["O"]) # this appends a list of five "O" strings
for z in board:
    print(*z)
    
def shiplocation():
    for placement in range(num):
        inputRow = input("Place your ship in a row: \n")
        break
    if inputRow not in range(num):
            print ("Enter a valid row number.")
            inputRow = input("Place your ship in a row: \n")
    for placement in range(num):        
        inputColumn = input("Place your ship in a column: \n")
        break
    if inputColumn not in range(num):
            print("Enter a valid column number.")
            inputColumn = input("Place your ship in a column: \n")
    
shiplocation()

# range() is columns

turn = 0
for attempt in range(NO_USER_GUESS):
    guessRow = int(input("Guess Row:"))
    guessColumn = int(input("Guess Col:"))

#if guessRow == NO_USER_GUESS and guessColumn == shiplocation:
      #print ("Hit")
#else:
   # if (guessRow < range(num) or guessRow > range(num)) or (guessColumn < range(num) or guessColumn > range(num)):
    #      print ("Enter a Valid Number")
