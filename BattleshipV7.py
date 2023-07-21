# Sidney & Kenyatta Battleship

import random

# Defining the Game Board
def print_board(board):
    for z in board:
        print(" ".join(z))

def print_board2(board2):
    for x in board2:
        print(" ".join(x))

'''We tried to allow for letting the user choose between random and deliberate placement,
but we couldn't get it done in time and commented it out'''

 # We tried to use a flip coin function to determine ship length and orientation. 
 # Issues- we don't know how to integrate the function into our code.
 
########

#######
def makelo(board):
    #while True:
            #choice = (input("Would you like to place your ships?: y/n: "))
            
            #if choice == ("n"):
                return random.randint(1, len(board)), random.randint(1, len(board[0]))
            
            #elif choice == ("y"):
            #    inputrow=int(input("Row: "))
             #   inputcol=int(input("Column: "))
            #break

def makelo2(board2):
          while True:
            RowRowRow = random.randrange(0,10)
            ColColCol = random.randrange(0,10)
            dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
            if Func(RowRowRow, ColColCol, 5, dir):
                add(RowRowRow, ColColCol, 5, dir)
                break
            while True:
                RowRowRow = random.randrange(0,10)
                ColColCol = random.randrange(0,10)
                dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
                if Func(RowRowRow, ColColCol, 4, dir):
                    add(RowRowRow, ColColCol, 4, dir)
                    break
            while True:
                RowRowRow = random.randrange(0,10)
                ColColCol = random.randrange(0,10)
                dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
                if Func(RowRowRow, ColColCol, 3, dir):
                    add(RowRowRow, ColColCol, 3, dir)
                    break
            while True:
                RowRowRow = random.randrange(0,10)
                ColColCol = random.randrange(0,10)
                dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
                if Func(RowRowRow, ColColCol, 3, dir):
                    add(RowRowRow, ColColCol, 3, dir)
                    break
            while True:
                RowRowRow = random.randrange(0,10)
                ColColCol = random.randrange(0,10)
                dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
                if Func(RowRowRow, ColColCol, 2, dir):
                    add(RowRowRow, ColColCol, 2, dir)
                    break       
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

grid = int(input("Choose Your Grid Size: "))

grid2 = grid

# Board display is made

board = []
for i in range(grid):
    board.append(["O"] * grid)

board2 = []
for o in range(grid2):
    board2.append(["O"] * grid2)

# Variable to represent rows and columns inside the board

RowRowRow, ColColCol = makelo(board) 

def cpuguess(board):
    return random.randint(1, len(board)), random.randint(1, len(board[0]))

#CPU=5
print("Titanico:",(makelo(board)))
 # Loop for the users turn
for LAUNCH in range(6):
# Stores user guesses in a list, output is result of user launch. 
    if LAUNCH == 5:
        print("All ships not sunk. \n Game Over.")
        board2[GuessRow][GuessColumn] = "X"
        break
    
    print("Launch", LAUNCH + 1,"!")
    print_board2(board2)
    
    GuessRow, GuessColumn = inputthatthang(grid)

    if GuessRow + 1 == RowRowRow and GuessColumn + 1 == ColColCol:
        print("\nWow! You sunk an enemy ship!")
        board2[GuessRow][GuessColumn] = "X"
        print_board2(board2)
        print("You Won! \nGame Over!")
        break
    
    else:
        if board2[GuessRow][GuessColumn] == "-":
            print("\n YOU ALREADY GUESSED THAT :|.")
            print(" ")
        else:
            print("\n Come on man! You MISSED!")
            board2[GuessRow][GuessColumn] = "-"
            print(" ")

# Computer guess - If Computer Guess =  User's Inputted Board or User's Randomized Ship, the game ends.    
    for COMPGUESS in range(1):
        print("CPU Turn:")
        print_board(board)
        
        cguess = cpuguess(board)
        
        print("CPU guessed:",cguess)
        print(" ")
        
        if cguess == makelo(board):
            print ("Titanico has been sunk! ;( \n Game Over.") 
            board[cguess] = int("X")
            break
        #else: 
            if board[cguess] == "-":
                print(" ")
            else:
                print(" ")
                board[cguess] = "-"
                print(" ")

