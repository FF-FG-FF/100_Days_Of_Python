import pygame

# Initialize Pygame
pygame.init() 

# Set the width and height of the screen
width, height = 800, 600

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Window")

# Set the background color
bg_color = (0, 0, 255)  # Blue color in RGB

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(bg_color)

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()
7