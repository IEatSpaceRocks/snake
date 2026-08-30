# IEatSpaceRocks, 30/08/2026

# Libraries
import sys, random

# Generate board
board = [["g"] * 17 for _ in range(15)]

# Variables
snakeY, snakeX = 7, 8
appleY, appleX = 7, 8
snake = []
score = 0
running = True
lastMove = ""

# Set up ANSI text formatting, define all colours used
class ANSI:
    RESET = "\x1b[0m"
    
    def getCol(rgb):
        r, g, b = rgb
        return f"\x1b[48;2;{r};{g};{b}m"
    
    GREEN1 = getCol((167, 217, 72))
    GREEN2 = getCol((142, 204, 57))
    BLUE1 = getCol((66, 111, 227))
    BLUE2 = getCol((58, 98, 205))
    RED = getCol((231, 71, 29))


# Functions

# Clear the terminal
def clearTerm():
    sys.stdout.write("\033[H\033[J")        # Move cursor to top left and clear everything after it

# Print a 4 space long block in a given colour
def printBlock(colour):
    print(getattr(ANSI, colour) + "    " + ANSI.RESET, end="")

# Check if apple is eaten. If yes, generate a new one and add one to the score
def checkApple(aX, aY, sX, sY, score):
    if aX == sX and aY == sY:
        while [aY, aX] in snake or (aX == sX and aY == sY):
            aX = random.randint(0, 16)
            aY = random.randint(0, 14)
        board[aY][aX] = "A"
        score += 1
    return aX, aY, score

# Update the snakes length and position. Check if the snake collided into itself
def updateSnake(sX, sY, score):
    snake.append([sY, sX])
    board[sY][sX] = "S"
    while len(snake) != score:
        if sY == snake[0][0] and sX == snake[0][1]:
            pass
        else:
            board[snake[0][0]][snake[0][1]] = "g"
        snake.pop(0)
    if snake.count([sY, sX]) > 1:
        return False
    else:
        return True



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
                elif x == snakeX and y == snakeY:   # If snake head:
                    printBlock("BLUE2")
                elif board[y][x] == "S":            # If a snake tile:
                    printBlock("BLUE1")
                elif board[y][x] == "A":            # If an apple tile:
                    printBlock("RED")
                count += 1                          # Add one to count, to change the grass colour
            count += 1                              # Add one to count after each row, to make it print the same colour blocks again (So we get a 2 high patch)
            print()                                 # New line
        count += 1                                  # Add one to count, so after every 2 rows of same colours, we get an offset 2 rows
                
    
# Initalize apple and snake
appleX, appleY, score = checkApple(appleX, appleY, snakeX, snakeY, score)
running = updateSnake(snakeX, snakeY, score)

# MAIN LOOP
    
while running:

    # Clear terminal
    clearTerm()
        
    # Print board (Every second grass patch will be a different shade)
    printBoard()
    
    # Input for movement direction
    move = ""
    while move not in ("w", "a", "s", "d"):
        move = input()
        sys.stdout.write("\033[1A\033[2K")        # Move to previous line and erase it (Clears the last input)
    
    # Logic for movement
    if move == "w":
        snakeY -= 1
    elif move == "a":
        snakeX -= 1
    elif move == "s":
        snakeY += 1
    else:
        snakeX += 1

    # Update apple and snake
    appleX, appleY, score = checkApple(appleX, appleY, snakeX, snakeY, score)
    running = updateSnake(snakeX, snakeY, score)
        
    # Check if player is out of bounds (Dead)
    if snakeY < 0 or snakeX < 0 or snakeY > 14 or snakeX > 16:
        print("You died")
        running = False