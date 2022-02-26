# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:
    x = 0
    a = 0
    b = 0
    c = 0
    

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    left = key[pygame.K_LEFT]
    right = key[pygame.K_RIGHT]
    up = key[pygame.K_UP]
    down = key[pygame.K_DOWN]

    
    if left == True:
        x = 100
    else:
        x = 75
        
    if right == True:
        c = 100
    else:
        c = 75
    
    if up == True:
        b = 100
    else:
        b = 75

    if down == True:
        a = 100
    else:
        a = 75
    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0,255 , 0), (250, 400), a)
    pygame.draw.circle(screen, (0, 255, 0), (250,100), b) 
    
    pygame.draw.circle(screen, (0, 255, 0), (100, 250),x ) 
    
    pygame.draw.circle(screen, (0, 255, 0), (400, 250), c)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
