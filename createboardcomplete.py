from random import randint

board = []
# range() is columns
for i in range(50):
    board.append(50 * ["O"]) # this appends a list of five "O" strings
for z in board:
    print(*z)

# board done 
