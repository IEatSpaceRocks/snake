# IEatSpaceRocks, 30/08/2026

# Libraries
import pygame

# Define colours
colours = {
    "GREEN1" : (170, 215, 81),
    "GREEN2" : (162, 209, 73),
    "GREEN3" : (87, 138, 52),
    "GREEN4" : (74, 117, 44),
    "RED" : (231, 71, 29),
    "BLUE" : (66, 111, 227)
}

# Variables
running = True
apple = [1, 1]
snake = [[9, 8]]
count = 0
facing = ["up"]

# Initialize Pygame and set up the screen
pygame.init()
screen = pygame.display.set_mode((760, 800))
pygame.display.set_caption("Snake")


# Generate the base board for the game
board = pygame.Surface((760, 800)).convert()
#Background
board.fill(colours.get("GREEN3"))
# Header
pygame.draw.rect(board, colours.get("GREEN4"), (0, 0, 760, 120))
# Squares
for col in range(1, 18):
    for row in range(1, 16):
        colour = "GREEN2" if (row + col) % 2 == 0 else "GREEN1"
        pygame.draw.rect(board, colours.get(colour), (col * 40, 120 + row * 40, 40, 40))
        
def draw():
    pygame.draw.circle(screen, colours.get("RED"), (40 + apple[0] * 40 - 20, 160 + apple[1] * 40 - 20), 19)
    for part in snake:
        pygame.draw.rect(screen, colours.get("BLUE"), (part[0] * 40, 120 + part[1] * 40, 40, 40))

def move(direction):
    if direction == "left":
        snake[0][0] -= 1
    elif direction == "right":
        snake[0][0] += 1
    elif direction == "up":
        snake[0][1] -= 1
    elif direction == "down":
        snake[0][1] += 1


# MAIN LOOP

while running:
    
    # Exit game if X or ESC pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if facing[0] != "left" and len(facing) == 1:
                    facing.append("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if facing[0] != "right" and len(facing) == 1:
                    facing.append("right")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                if facing[0] != "up" and len(facing) == 1:
                    facing.append("up")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if facing[0] != "down" and len(facing) == 1:
                    facing.append("down")
            

            
    count += 1
    
    if count % 10 == 0:
        print(facing)
        if len(facing) == 2:
            move(facing[0])
            facing.pop(0)
        else:
            move(facing[0])
            
    # Add board to the screen
    screen.blit(board, (0, 0))
    
    draw()
    
    # Update screen
    pygame.display.flip()  
        
    # 60 fps
    pygame.time.Clock().tick(60)

# If game loop exited, exit pygame
pygame.quit()
