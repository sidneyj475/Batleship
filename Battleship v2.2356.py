#Sidney & Kenyatta Battleship
import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def generate_location(board):
    return random.randint(1, len(board)), random.randint(1, len(board[0]))

def collect_input(board_size):
    while(True):
        try:
            guess_row = eval(input("\nGuess Row: "))
            guess_col = eval(input("Guess Col: "))
            
            if guess_col <= board_size and guess_row <= board_size:
                return guess_row-1, guess_col-1
            else:
                print("That is not on the board. Please do better next time.\n")
        except: 
            print("Please type an integer that correlates to an index on the board.\n")
        

board_size = 5

board = []
for i in range(board_size):
    board.append(["O"] * board_size)


print("Let's play Battleship!\n")


ship_row, ship_col = generate_location(board) 
print(ship_row, ship_col)

for turn in range(4):

    if turn == 3:
        print("Game Over")
        board[guess_row][guess_col] = "X"
        break
    
    print("Turn", turn + 1)
    print_board(board)
    
    guess_row, guess_col = collect_input(board_size)

    if guess_row + 1 == ship_row and guess_col + 1 == ship_col:
        print("\nGreat Shot, you sunk my ship")
        board[guess_row][guess_col] = "X"
        print_board(board)
        print("")
        break
    
    else:
        if board[guess_row][guess_col] == "M":
            print("\nYou guessed that one already.")
            print(" ")
        else:
            print("\nYou missed my battleship!")
            board[guess_row][guess_col] = "M"