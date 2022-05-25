import pygame

class Cactus:
    def __init__(self, screen):
        w, h = pygame.display.get_surface().get_size()
        self.screen = screen
        self.x = w
        self.y = h - 80
        self.color = (255,0,0)
    def update(self):
        self.x -= 10
        self.draw()
    def draw(self):
        pos = self.x, self.y
        pygame.draw.circle(self.screen, self.color, pos, 30)