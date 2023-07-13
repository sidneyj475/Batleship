from random import randint

num = 50

board = []
# range() is columns
for i in range(num):
    board.append(num * ["O"]) # this appends a list of five "O" strings
for z in board:
    print(*z)

# board done 
