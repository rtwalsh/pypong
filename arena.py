import pygame
from colors import *

class Net(pygame.sprite.Sprite):
    
    def __init__(self, top, bottom, position):
        super().__init__()

        self.image = pygame.Surface((1, bottom - top))
        self.image.fill(Colors.BLACK)
        self.image.set_colorkey(Colors.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = position
        self.rect.y = top
        
        on = False
        y = 0
        while y < bottom:
            if on:
                pygame.draw.line(self.image, Colors.WHITE, (0, y), (0, y + 10))
            y += 10
            on = not on

class Border():

    TOP = 0x01
    BOTTOM = 0x02

class Panel(pygame.sprite.Sprite):

    def __init__(self, width, height, top, border):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(Colors.BLACK)
        self.image.set_colorkey(Colors.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = top

        if border & Border.TOP:
            pygame.draw.line(self.image, Colors.WHITE, (0, 0), (self.rect.width, 0))

        if border & Border.BOTTOM:
            pygame.draw.line(self.image, Colors.WHITE, (0, self.rect.height - 1), (self.rect.width, self.rect.height - 1))

class Scoreboard(Panel):

    def __init__(self, width, height):
        super().__init__(width, height, 0, Border.BOTTOM)

