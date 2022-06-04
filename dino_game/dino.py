import pygame

class Dino:
    def __init__(self, img_list, ground=400, width=0):
        assert type(img_list) == list
        assert type(img_list[0]) == pygame.Surface
        self.img_list = img_list
        self.img_index = 0
        self.changing_img_at_frame = 20
        self.ground = ground
        self.x = 50
        self.y = self.ground
        self.jumping_speed = 0
        self.mode = 'walk'
        self.count_frame = 0
        self.width = width

    def next_img(self):
        self.img_index += 1
        if self.img_index >= len(self.img_list):
            self.img_index = 0
        return self.img_list[int(self.img_index)]
    # img_list = [img1, img2, img3]
    # img1 = img_list[0]

    def old_img(self):
        return self.img_list[int(self.img_index)]

    def get_img(self):
        self.count_frame += 1
        if self.count_frame == 5:
            self.count_frame = 0
            return self.next_img()
        else:
            return self.old_img()



    def blit(self, screen, key):

        ################ input & process ###########################
        ## check key_pressed
        # if key[pygame.K_RIGHT] == True:
        #     self.x +=1
        # if key[pygame.K_LEFT] == True:
        #     self.x -=1
        if key[pygame.K_UP] == True and self.mode == 'walk':
            self.jumping_speed = 15
            self.mode = 'jump'
        
        if self.mode == 'jump':
            self.jumping_speed -= 0.98 # js=9
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

        ############ display #####################
        # blit on screen
        img = self.get_img()
        position = (self.x, self.y)
        screen.blit(img, position)