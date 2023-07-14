from random import randint

NO_USER_GUESS=10

num = 5

board = []

def print_board(board):
    print ("Let's Play Battleship!")
print_board(board)

# range() is columns
for i in range(num):
    board.append(num * ["O"]) # this appends a list of five "O" strings
for z in board:
    print(*z)

def random_row(board):
    return randint(range(num) - 1)

def random_column(board):
    return randint(range(num) - 1)

shipRow = random_row(board)
shipColumn = random_column(board)

turn = 0
for attempt in range(NO_USER_GUESS):
    guessRow = int(input("Guess Row:"))
    guessColumn = int(input("Guess Col:"))

if guessRow == ship_row and guessColumn == ship_col:
      print ("Hit")
else:
    if (guessRow < range(num) or guessRow > range(num)) or (guessColumn < range(num) or guessColumn > range(num)):
          print ("Enter a Valid Number")
    #elif(board[guessRow][guessColumn] == "X"):
          #print ("You guessed that one already!!!")
          
#while board: 
#        try:
 #           guessRow=(input("Enter a Row: "))
   #         guessColumn=(input("Enter a Column: "))
  # #     except ValueError:
     #       print("Numbers only!")
      #      continue

       # if guessRow not in range(num) or guessColumn not in range(num):
        #    print("Please enter a valid row!")
         #   continue
        #
       # row = row - 1 
        # column = column - 1 