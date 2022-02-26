#  pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    key = pygame.key.get_pressed()
    left = key[pygame.K_LEFT]
    right = key[pygame.K_RIGHT]
    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    if left == True:
        
        pygame.draw.circle(screen, (0, 0, 255), (100, 250), 20)
        pygame.draw.circle(screen, (0, 0, 255), (200, 250), 20)
        pygame.draw.circle(screen, (0, 0, 255), (300, 250), 20)
        pygame.draw.circle(screen, (0, 0, 255), (400, 250), 20)
        pygame.draw.circle(screen, (0, 0, 255), (500, 250), 20)
        pygame.draw.circle(screen, (0, 0, 255), (200, 200), 20)
        pygame.draw.circle(screen, (0, 0, 255), (200, 400), 20)
    
    elif right == True:
        
        pygame.draw.circle(screen, (0, 0, 255), (100, 250), 20)
        pygame.draw.circle(screen, (0, 0, 255), (200, 250), 20)
        pygame.draw.circle(screen, (0, 0, 255), (300, 250), 20)
        pygame.draw.circle(screen, (0, 0, 255), (400, 250), 20)
        pygame.draw.circle(screen, (0, 0, 255), (500, 250), 20)
        pygame.draw.circle(screen, (0, 0, 255), (400, 200), 20)
        pygame.draw.circle(screen, (0, 0, 255), (400, 400), 20)


    # Flip the display
    pygame.display.flip()
# Done! Time to quit.
pygame.quit()