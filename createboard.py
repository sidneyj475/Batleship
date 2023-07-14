from random import randint

num = 5

board = []
# range() is columns
for i in range(num):
    board.append(num * ["O"]) # this appends a list of five "O" strings
#for z in board:
    #print(*z)
def print_board(board):
    print ("Battleship")
print_board(board)

# board done 
guessRow = int(input("Guess Row:"))
guessColumn = int(input("Guess Col:"))

  
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