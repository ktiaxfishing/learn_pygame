import random
import pygame
class MyCircle:
    def __init__(self, screen) -> None:
        #######
        # self.center = (random.randint(1,500),random.randint(1,500))
        self.screen = screen
        self.x = self.rand(500)
        self.y = self.rand(500)
        self.size = 0
        self.max_size = 100
        self.rate =  0.01 * self.rand(10)
        self.color = (self.rand(255),self.rand(255),self.rand(255))
        # self.color = (200,77,66)
    
    def rand(self,x):
        return random.randint(1,x)

    def draw(self):
        screen = self.screen
        x = self.x
        y = self.y
        size = self.size

        # this is old code
        pygame.draw.circle(screen, self.color, (x, y), size)
    
    def logic(self):
        # defind
        # size = self.size
        max_size = self.max_size
        # check size
        self.size += self.rate
        if self.size >= max_size:
            self.size = 0
            
            # new center
            x = random.randint(1,500)
            y = random.randint(1,500)
            self.x = x
            self.y = y
            self.color = (self.rand(255),self.rand(255),self.rand(255))
    