# IEatSpaceRocks, 27/08/2026

import random
import os, subprocess

board = [["g"] * 17 for _ in range(15)]

snakeY, snakeX = 7, 8
running = True
    
def clearTerm():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    
while running:
    clearTerm()
    
    board[snakeY][snakeX] = "S"
    
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
        
    board[snakeY][snakeX] = "g"
    
    move = input()
    
    while move not in ("w", "a", "s", "d"):
        move = input()
        
    if move == "w":
        snakeY -= 1
    elif move == "a":
        snakeX -= 1
    elif move == "s":
        snakeY += 1
    else:
        snakeX += 1 
    
    if snakeY < 0 or snakeX < 0 or snakeY > 14 or snakeX > 16:
        print("You die")
        running = False
    else:
        board[snakeY][snakeX] = "S"