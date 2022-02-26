# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
print("hello")
y = 0
x = 200

speed = 1
x_2 = 100
y_2 = 100
up =0
down =0
# Run until the user asks to quit
running = True
while running:

    y+=speed

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -=1
    key = pygame.key.get_pressed()
    left_2 = key[pygame.K_a]
    right_2 = key[pygame.K_d]
    up = key[pygame.K_w]
    down = key[pygame.K_s]

    
    left = key[pygame.K_LEFT]
    right = key[pygame.K_RIGHT]
    if y==500:
        speed = -1
    if y<0:
        speed =1
    if left == True:
        x -=1.1
    if right == True:
        x +=1
    print(x)

    if x <= 0:
        x = 500
    elif x >=500:
        x =0
    

    if x_2<= 0:
        x_2 = 500
    elif x_2 >=500:
        x_2 =0

    if left_2 == True:
        x_2 -=1
    if right_2 == True:
        x_2 +=1
    if up:
        y_2 -=1
    if down:
        y_2 +=1

    
    
    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 250, 0), (x, y), 50)
    pygame.draw.circle(screen, (255, 0, 0), (x_2, y_2), 40)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()