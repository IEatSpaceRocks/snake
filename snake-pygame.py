# IEatSpaceRocks, 30/08/2026

# Libraries
import pygame

# Define colours
colours = {
    "GREEN1" : (170, 215, 81),
    "GREEN2" : (162, 209, 73),
    "GREEN3" : (87, 138, 52),
    "GREEN4" : (74, 117, 44)
}

# Variables
running = True


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


# MAIN LOOP

while running:
    
    # Exit game if X or ESC pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Add board to the screen
    screen.blit(board, (0, 0))
    
    # Update screen
    pygame.display.flip()
    
    # 60 fps
    pygame.time.Clock().tick(60)

# If game loop exited, exit pygame
pygame.quit()



