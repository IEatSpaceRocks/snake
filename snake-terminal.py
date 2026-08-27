# IEatSpaceRocks, 27/08/2026

# Libraries
import random
import os, subprocess

# Generate board
board = [["g"] * 17 for _ in range(15)]

# Variables
snakeY, snakeX = 7, 8
running = True


# Functions

def clearTerm():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    
    
# MAIN LOOP
    
while running:
    
    clearTerm()
    
    # Add snake to board
    board[snakeY][snakeX] = "S"
    
    # Print board (Every second grass patch will be a different shade)
    count = 0
    for y in range(15):
        for x in range(17):
            if board[y][x] == "g":
                if count % 2 == 0:
                    print("g", end=" ")
                else:
                    print("G", end=" ")
            elif board[y][x] == "S":
                print("S", end=" ")
            count += 1
        print()
        
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
        