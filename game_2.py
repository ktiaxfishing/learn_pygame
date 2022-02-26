# Simple pygame program

# Import and initialize the pygame library
import random
import pygame
pygame.init()
size = 0
x = random.randint(1,500)
y = random.randint(1,500)

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    size +=0.01
    if size >=100:
        size = 0
        
        x = random.randint(1,500)
        y = random.randint(1,500)
        

    



    

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (x, y), size)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()