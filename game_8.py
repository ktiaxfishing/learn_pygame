# Simple pygame program

# Import and initialize the pygame library
import random
import pygame
from glom import Glom
pygame.init()

# # Set up the drawing window
screen = pygame.display.set_mode([500, 500])

print(Glom, type(Glom))
c = Glom()
print('success')

# Run until the user asks to quit
running = True
while running:

#     # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        

#     # Fill the background with white
    screen.fill((255, 255, 255))

#     # draw
    c.draw(screen)
#     # Flip the display
    pygame.display.flip()

# # Done! Time to quit.
# pygame.quit()