print("ok")
import pygame
import random
# Glom = 'hello'
class Glom:
    # def __init__(self):
    #     print('hello from glom')

    def __init__(self):
        self.x = random.randint(1,500) 
        self.y = random.randint(1,500)
        self.size =20

        
    def draw(self,screen,mouse_pos,mouse_click):
        # print(mouse_pos,mouse:_click)
        if mouse_click == True: # and is_in_circle(radius,center,mouse_pos) == True:
            score= "+1"
        else:
            score = ""

        self.size += 0.1
        if self.size >=50:
            self.__init__()
        pygame.draw.circle(screen, (0,0,255), (self.x, self.y), self.size)
        return score
        
    # def area():
         