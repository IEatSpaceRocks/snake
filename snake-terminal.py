# IEatSpaceRocks, 28/08/2026

# Libraries
import random
import os, subprocess

# Generate board
board = [["g"] * 17 for _ in range(15)]

# Variables
snakeY, snakeX = 7, 8
running = True


# Set up ANSI text formatting, define all colours used
class ANSI:
    RESET = "\x1b[0m"
    
    def getCol(rgb):
        r, g, b = rgb
        return f"\x1b[48;2;{r};{g};{b}m"
    
    GREEN1 = getCol((167, 217, 72))
    GREEN2 = getCol((142, 204, 57))
    BLUE = getCol((66, 111, 227))


# Functions

# Clear the terminal
def clearTerm():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

# Print a 4 space long block in a given colour
def printBlock(colour):
    print(getattr(ANSI, colour) + "    " + ANSI.RESET, end="")

# Print the board itself
def printBoard():
    count = 0                                       # Count determines if the given patch of grass is lighter or darker green
    for y in range(15):                             # For the 15 rows
        for _ in range(2):                          # So that each block of 4 spaces gets generated under eachother, to make a full patch, that is 4 spaces wide and 2 high
            for x in range(17):                     # For the 17 columns
                if board[y][x] == "g":              # If a grass tile:
                    if count % 2 == 0:              # If count is even -> light green
                        printBlock("GREEN1")
                    else:                           # If count is uneven -> darker green
                        printBlock("GREEN2")
                elif board[y][x] == "S":            # If a snake tile:
                    printBlock("BLUE")
                count += 1                          # Add one to count, to change the grass colour
            count += 1                              # Add one to count after each row, to make it print the same colour blocks again (So we get a 2 high patch)
            print()                                 # New line
        count += 1                                  # Add one to count, so after every 2 rows of same colours, we get an offset 2 rows
                
    
    
# MAIN LOOP
    
while running:
    
    clearTerm()
    
    # Add snake to board
    board[snakeY][snakeX] = "S"
    
    # Print board (Every second grass patch will be a different shade)
    printBoard()
    
    # Remove previous snake
    board[snakeY][snakeX] = "g"
    
    # Input for movement direction
    move = input()
    while move not in ("w", "a", "s", "d"):
        move = input()
    
    # Logic for movement
    if move == "w":
        snakeY -= 1
    elif move == "a":
        snakeX -= 1
    elif move == "s":
        snakeY += 1
    else:
        snakeX += 1
        
    # Check if player is out of bounds (Dead)
    if snakeY < 0 or snakeX < 0 or snakeY > 14 or snakeX > 16:
        print("You died")
        running = False
        