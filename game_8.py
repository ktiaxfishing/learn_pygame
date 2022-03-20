# Simple pygame program

# Import and initialize the pygame library
import random
import pygame
from glom import Glom
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS',30)
textrender = font.render("hello",False,(255,0,0))
x = 0

# # Set up the drawing window
screen = pygame.display.set_mode([500, 500])
print(Glom, type(Glom))
c = Glom()
score = 0
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
    x +=1 
    xx = str(x)
    textrender = font.render(xx,False,(255,0,0))
    screen.blit(textrender,(100,100))
#     # 
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()[0]
    
    score_ = c.draw(screen,mouse_pos,mouse_click)
    if score_=="+1":
        score+=1
#     # Flip the display
    pygame.display.flip()
    print(score)



# # Done! Time to quit.
# pygame.quit()