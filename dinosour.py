# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

x = 0
change = False
hold = False
horizontal = 0


ver = 0
font = pygame.font.SysFont("Commic SansMS",30)


image = pygame.image.load('./picture/pngegg.png')
x,y = image.get_size()
    
image = pygame.transform.scale(image, (150, 150))
# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run unt`il the user asks to quit
running = True
while running:
    

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    click = pygame.mouse.get_pressed()[0]
    
    horizontal += 0.1
    if click == True:
        x = 255
    
        
    if click == False:
        x = 0
     
 
  
    screen.blit(image,(100,ver))

    print(ver)

    down = pygame.key.get_pressed()
    if down[pygame.K_DOWN] == True:
        ver +=1

    if ver > 200:
        down == False


    up = pygame.key.get_pressed()
    if up[pygame.K_UP] == True:
        ver -=1

    if horizontal>500:
        horizontal = 1
    elif horizontal<1:
        horizontal = 500
   

    
    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (x, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

ver = 0

image = pygame.image.load('./picture/pngegg.png')
image = pygame.transform.scale(image, (150, 150))




# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


  
    screen.blit(image,(ver))

    down = pygame.key.get_pressed()
    if down[pygame.K_DOWN] == True:
        ver +=1

        
    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()