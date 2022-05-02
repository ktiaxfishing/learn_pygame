# Simple pygame program

# Import and initialize the pygame library
import pygame
import mylib 
pygame.init()

x = 0
change = False
hold = False
PINK = (255,0,255)
BLUE = (0,0,255)
color_name = 0
horizontal = 100
vertical = 100
font = pygame.font.SysFont("Commic SansMS",30)

# load images
pink_text_img = font.render("pink",False,PINK)
blue_text_img = font.render("blue",False,BLUE)
dino_img_list = []
for i in range(1, 4):
    img = pygame.image.load('./picture/dino_%d.png'%(i))
    img = mylib.rescale_img(img, width=100)
    dino_img_list.append(img)

# class Dino
class Dino:
    def __init__(self, img_list):
        assert type(img_list) == list
        assert type(img_list[0]) == pygame.Surface
        self.img_list = img_list
        self.i = 0
        self.changing_img_speed = 0.005
        self.ground = 400
        self.x = 100
        self.y = self.ground
        self.jumping_speed = 0
        self.mode = 'walk'

    def get_img(self):
        self.i += self.changing_img_speed
        if self.i >= len(self.img_list):
            self.i = 0
        return self.img_list[int(self.i)]

    def blit(self, screen, key):
        ## check key_pressed
        # if key[pygame.K_RIGHT] == True:
        #     self.x +=1
        # if key[pygame.K_LEFT] == True:
        #     self.x -=1
        if key[pygame.K_UP] == True and self.mode == 'walk':
            self.jumping_speed = 5
            self.mode = 'jump'
        
        if self.mode == 'jump':
            self.jumping_speed -= 0.1 # js=9
            self.y -= self.jumping_speed  #js=10 y=490   #js=9 y=481   #js=8 y=473

            # if touch the ground, reset all state
            if self.y >= self.ground:
                self.jumping_speed = 0
                self.y = self.ground
                self.mode = 'walk'

        # if key[pygame.K_DOWN] == True:
        #     self.y +=1
        
        ## update if out screen
        # if self.x > 500:
        #     self.x = 1
        # elif self.x < 1:
        #     self.x = 500

        # blit on screen
        img = self.get_img()
        position = (self.x, self.y)
        screen.blit(img, position)

# init dino
dino = Dino(dino_img_list)

# init screen
screen = pygame.display.set_mode([500, 500])

# loop
running = True
while running:
    ################################
    ##########       ###############
    ########## input ###############
    ##########       ###############
    ################################
    # get mouse input
    click = pygame.mouse.get_pressed()[0]
    key = pygame.key.get_pressed()

    ################################
    ##########         #############
    ########## process #############
    ##########         #############
    ################################

    # close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # text color
    if click == True:
        x = 255
        text_color = 'pink'
    else:
        x = 0
        text_color = 'blue'

    # process show text
    text = ''
    text += 'js='
    text += str(dino.jumping_speed)
    text += ' y='
    text += str(dino.y)
    text += ' mode='
    text += str(dino.mode)
    dino_info = font.render(text,False,PINK)

    ################################
    ##########         #############
    ########## display #############
    ##########         #############
    ################################

    # fill background
    screen.fill((255, 255, 255))

    # blit text img
    if text_color == 'pink':
        screen.blit(pink_text_img,(20,20)) 
    elif text_color == 'blue':
        screen.blit(blue_text_img,(20,20))

    # blit show text
    screen.blit(dino_info, (100,50))

    # blit dino
    dino.blit(screen, key)

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()




# loop
    # get input

    # process

    # draw (display)




