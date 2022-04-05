# Simple pygame program

# Import and initialize the pygame library
import random
import pygame
from glom import Glom
pygame.init()
font = pygame.font.SysFont('Commic SansMS',30)
texttriender = font.render("hello",False,(255,0,0))
x = 0


# # Set up the drawing window
screen = pygame.display.set_mode([500, 500])
print(Glom, type(Glom))
c = Glom()
score = 0
print('success')
score = 0
hold = False
fire = False

# Run until the user asks to quit
running = True
while running:

#     # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        

#     # Fill the background with white
    screen.fill((255, 255, 255))
    x += 1
    xx = str(x)
    textrender = font.render(xx,False,(255,0,0))
    screen.blit(textrender,(100,100))

#     # draw
    left = pygame.mouse.get_pressed()[0]
    fire = False
    if left == True and hold == False:
        fire = True
        hold = True
    if left == False and hold == True:
        hold = False

    # if hold == True and left == False:
    #     hold = False
    mouse_pos = pygame.mouse.get_pos()
    point = c.draw(screen,fire,mouse_pos)
    if point == "+1":
        score +=1
    elif point == "-1":
        score -=1
    elif point == "-0.5":
        score -= 0.5
    print(score,hold,fire)
    score_ = c.draw(screen,mouse_pos,left)
    if score_ =="+1":
        score+=1
    pygame.draw.circle(screen, (255,0,0), (mouse_pos[0], mouse_pos[1]),5)
#     # Flip the display
    pygame.display.flip()
    print(score)



# # Done! Time to quit.
# pygame.quit()