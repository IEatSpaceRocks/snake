# IEatSpaceRocks, 27/08/2026

import random
import os, subprocess

rows = (
    (10, 11, 12, 13, 14),
    (20, 21, 22, 23, 24),
    (30, 31, 32, 33, 34),
    (40, 41, 42, 43, 44),
    (50, 51, 52, 53, 54)
)
values = {
    10 : "g", 11 : "g", 12 : "g", 13 : "g", 14 : "g",
    20 : "g", 21 : "g", 22 : "g", 23 : "g", 24 : "g",
    30 : "g", 31 : "g", 32 : "S", 33 : "g", 34 : "g",
    40 : "g", 41 : "g", 42 : "g", 43 : "g", 44 : "g",
    50 : "g", 51 : "g", 52 : "g", 53 : "g", 54 : "g",
}

snake = 32
running = True

def printPlace(place):
    print(values.get(place), end=" ")
    
def clearTerm():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    
while running:
    clearTerm()
    
    count = 0
    for row in rows:
        for x in row:
            if values.get(x) == "g":
                if count % 2 == 0:
                    print("g", end=" ")
                else:
                    print("G", end=" ")
            elif values.get(x) == "S":
                print("S", end=" ")
            count += 1
        print()
        
    values.update({snake:"g"})
    
    move = input()
    
    while move not in ("w", "a", "s", "d"):
        move = input()
        
    if move == "w":
        snake -= 10
    elif move == "a":
        snake -= 1
    elif move == "s":
        snake += 10
    else:
        snake += 1 
    
    if snake not in values:
        print("You die")
        running = False
    else:
        values.update({snake:"S"})