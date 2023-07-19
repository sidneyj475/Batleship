# Sidney & Kenyatta Battleship

import random

# Defining the Game Board
def print_board(board):
    for z in board:
        print(" ".join(z))

'''We tried to allow for letting the user choose between random and deliberate placement,
but we couldn't get it done in time and commented it out'''


def makelo(board):
    #while True:
        #try:
            #choice = (input("Would you like to place your ships?: y/n: "))
            
            #if choice == ("n"):
                return random.randint(1, len(board)), random.randint(1, len(board[0]))
            
            #else:
                #inputrow=int(input("Row: "))
                #inputcol=int(input("Column: "))
        #except: 
            #print("Whaaaaaa")

# Definining user input, input will be the shot that the player takes at the computer's board.
  
def inputthatthang(grid):
    while(True):
        try:
            GuessRow = eval(input("Take a shot, Guess Row: "))
            GuessColumn = eval(input("Now Guess Column: "))
            
            if GuessColumn <= grid and GuessRow <= grid:
                return GuessRow-1, GuessColumn-1
            else:
                print("Seems like you're aiming for failure. Try again...\n")
        except: 
                print("Aim inside the grid.\n")
 # Game Intro       
 
print("Let's Play Battleship! Your enemy is on water. They're coming at you and FAST! Do your best to destroy their fleet. You have 5 chances.")

# User defines how large board will be. The board size will be the same for both players (user and computer)

grid = int(input("Choose Your Grid Size:"))

# Board display is made

board = []
for i in range(grid):
    board.append(["O"] * grid)


# Variable to represent rows and columns inside the board

RowRowRow, ColColCol = makelo(board) 

def cpuguess(board):
    return random.randint(1, len(board)), random.randint(1, len(board[0]))

#CPU=5

 # Loop for the users turn
for LAUNCH in range(6):
# Stores user guesses in a list, output is result of user launch. 
    if LAUNCH == 5:
        print("Game Over.")
        board[GuessRow][GuessColumn] = "X"
        break
    
    print("Launch", LAUNCH + 1,"!")
    print_board(board)
    
    GuessRow, GuessColumn = inputthatthang(grid)

    if GuessRow + 1 == RowRowRow and GuessColumn + 1 == ColColCol:
        print("\nWow! You sunk an enemy ship!")
        board[GuessRow][GuessColumn] = "X"
        print_board(board)
        print("")
        break
    
    else:
        if board[GuessRow][GuessColumn] == "-":
            print("\n YOU ALREADY GUESSED THAT :|.")
            print(" ")
        else:
            print("\n Come on man! You MISSED!")
            board[GuessRow][GuessColumn] = "-"
            
    for compguess in range(1):
        print("CPU guessed:",(cpuguess(board)))
        print(" ")
        if cpuguess(board) == makelo(board):
            print ("Your ship has been sunk! ;( ") 
            print("Game Over.")
            break

        
  