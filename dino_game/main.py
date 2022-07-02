# Simple pygame program

# Import and initialize the pygame library
import pygame
import mylib
from cactus import Cactus
from dino import Dino
import time
import random
pygame.init()

x = 0
change = False
hold = False
PINK = (255,0,255)
BLUE = (0,0,255)
color_name = 0
horizontal = 100
vertical = 100
font = pygame.font.SysFont("commic sansms",30)
clock = pygame.time.Clock()
dino_pos = (50,50)
ran_time = random.randint(1,3)
now =  time.time()
next_cactus_time = ran_time + now
dino_w = 100
RED =(255,0,0)
WHITE = (255,255,255)
bgc = WHITE
score = 2
# load images
pink_text_img = font.render("pink",False,PINK)
blue_text_img = font.render("blue",False,BLUE)


click_text_img = font.render("click",False,PINK)

no_click_text_img = font.render(" ",False,PINK)
# click_rendered_text
# rendered_click
# rendered_text_click

# nameing
# 1 name
# 2 object type [img, text_img, color, text, size]
dino_img_list = []
for i in range(1, 4):
    img = pygame.image.load('./picture/dino_%d.png'%(i))
    img = mylib.rescale_img(img, width=dino_w)
    dino_img_list.append(img)


# init screen
screen = pygame.display.set_mode([500, 500])
w, h = pygame.display.get_surface().get_size()

# init dino
dino = Dino(dino_img_list, ground = h-130,width = dino_w)

# variables
counter = 0
cactus_list = []
can_cal_score = True

def dino_hit(dino, cactus):
    x_dino = dino.x
    width_dino = dino.width
    x_cactus = cactus.x
    front_dino = dino.x + dino.width
    back_dino = dino.x
    front_cactus = cactus.x + cactus.width/2
    back_cactus = cactus.x - cactus.width/2
    
    y_dino = dino.y
    y_cactus = cactus.y
    
    



    if front_dino > back_cactus and back_dino < front_cactus:
        if y_dino < 320:
            return 'white'
        # change background color to red
        return 'red'

 
    return 'white'
    
    
    # if back_dino > front_cactus and front_dino < back_cactus:
        # change background color to white
        # bgc = WHITE

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

    if len(cactus_list) > 0:
        color = dino_hit(dino, cactus_list[0])
        if color == 'red':
            bgc = RED
        elif color == 'white':
            bgc = WHITE
  
    # close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # q to quit
    if key[pygame.K_q]:
        running = False

    # a to spawn cactus
    # if key[pygame.K_a]:
    #     print('new cactus')
    #     cactus_list.append(Cactus(screen))

    # cactus_list.append(Cactus(screen))

    # new cactus system
    now = time.time()
    if now > next_cactus_time:
        cactus_list = []
        cactus_list.append(Cactus(screen))
        ran_time = random.randint(1,3)
        next_cactus_time = ran_time + now
        can_cal_score = True


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

    # process check click
    if click == True:
        text_click = 'click'
    else:
        text_click = " "

    # calculate scroe
    if bgc == RED and can_cal_score:
        score = int(score)
        score = score - 1
        can_cal_score = False
    
    score = str(score)
    score_text_img = font.render(score,False,BLUE)

    # game over check
    score = int(score)
    
    gameover_text_img = font.render("game over",False,PINK)

   
        

    
    ################################
    ##########         #############
    ########## display #############
    ##########         #############
    ################################

    # fill background
    screen.fill(bgc)


    # # blit text img
    # if text_color == 'pink':
    #     screen.blit(pink_text_img,(20,20)) 
    # elif text_color == 'blue':
    #     screen.blit(blue_text_img,(20,20))

    # # blit check click
    # if text_click == 'click':
    #     screen.blit(click_text_img,(40,80))

    # # blit show text
    # screen.blit(dino_info, (100,50))
    screen.blit(score_text_img,(50,50))

    if score < 1:
        
        screen.blit(gameover_text_img,(200,100))
    # x = dino.x
    # if key[pygame.K_RIGHT]:
    #     x += 1
    # if key[pygame.K_LEFT]:
    #     x -= 1
    # dino.x = x
    # print(x)

    # update cactus
    for cactus in cactus_list:
        cactus.update()

    # blit dino
    dino.blit(screen, key)



    pygame.display.flip()

    # counter += 1
    # print(counter)
    clock.tick(60) 

# Done! Time to quit.
pygame.quit()





# loop
    # get input

    # process

    # draw (display)




