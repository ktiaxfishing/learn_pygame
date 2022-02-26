# Simple pygame program

# Import and initialize the pygame library
import random
import pygame
# import my_circle
from my_circle import MyCircle
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

'''
# my variable
size = 0
max_size = 100
x = random.randint(1,500)
y = random.randint(1,500)
'''
# c1 = MyCircle(screen)
# c2 = MyCircle(screen)
# c3 = MyCircle(screen)
all_circles = []
for i in range(5):
    c = MyCircle(screen)
    all_circles.append(c)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # logic
    '''
        # old code
        size +=0.01
        if size >= max_size:
            size = 0
            
            # new center
            x = random.randint(1,500)
            y = random.randint(1,500)

        # draw
        pygame.draw.circle(screen, (0, 0, 255), (x, y), size)
    '''
    # c1.update()
    # c2.update()
    # c3.update()
    for circle in all_circles:
        circle.logic()
        circle.draw()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()