print("ok")
import pygame
import random
# Glom = 'hello'
class Glom:
    # def __init__(self):
    #     print('hello from glom')

    def __init__(self):
        self.cen_x = random.randint(1,500) 
        self.cen_y = random.randint(1,500)
        self.size =20

        
    def draw(self,screen,left,mouse_pos):
        self.size += 0.01
        if self.size >=50:
            self.__init__()
            return "-0.5"
        elif left == True:
            if self.is_clicked(mouse_pos) == True:
                self.__init__()
                return "+1"
            else:
                return "-1"
        pygame.draw.circle(screen, (0,0,255), (self.cen_x, self.cen_y), self.size)
        
        
      
    def is_clicked(self,mouse_pos):
        # radius, center, mouse
        # check for clicked
            # find x, y 
            # find diagonal
            # if diagonal less than radius mean hit
        # return true or false

        x = self.cen_x - mouse_pos[0]
        y = self.cen_y - mouse_pos[1]
        diagonal = (x**2 + y**2)**0.5
        if diagonal <= self.size:
            return True
        else:
            return False
