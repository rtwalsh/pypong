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

    NUMBER_WIDTH = 30
    NUMBER_HEIGHT = 50
    NUMBER_STROKE_WIDTH = 10
    NUMBER_MARGIN = 50

    def __init__(self, width, height):
        super().__init__(width, height, 0, Border.BOTTOM)

        self.initialize_numbers()


    def update(self):
        self.image.blit(self.numbers[1], (50, 20))
        self.image.blit(self.numbers[9], (self.rect.width - 50 - 30, 20))
        
    def initialize_numbers(self):
        self.numbers = []
        for i in range(0, 10):
            surface = pygame.Surface((Scoreboard.NUMBER_WIDTH, Scoreboard.NUMBER_HEIGHT))
            surface.fill(Colors.WHITE)
            self.numbers.append(surface)

        self.initialize_zero(self.numbers[0])
        self.initialize_one(self.numbers[1])
        self.initialize_two(self.numbers[2])
        self.initialize_three(self.numbers[3])
        self.initialize_four(self.numbers[4])
        self.initialize_five(self.numbers[5])
        self.initialize_six(self.numbers[6])
        self.initialize_seven(self.numbers[7])
        self.initialize_eight(self.numbers[8])
        self.initialize_nine(self.numbers[9])

    def initialize_zero(self, surface):
        pygame.draw.rect(surface, Colors.BLACK, 
                         (Scoreboard.NUMBER_STROKE_WIDTH, 
                          Scoreboard.NUMBER_STROKE_WIDTH, 
                          Scoreboard.NUMBER_STROKE_WIDTH, 
                          Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_one(self, surface):
        pygame.draw.rect(surface, Colors.BLACK, 
                         (0, 
                          0, 
                          Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH, 
                          Scoreboard.NUMBER_HEIGHT))

    def initialize_two(self, surface):
        pygame.draw.rect(surface, Colors.BLACK,
                          (0,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, Colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))
        
    def initialize_three(self, surface):
        pygame.draw.rect(surface, Colors.BLACK,
                          (0,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, Colors.BLACK,
                          (0,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))
        
    def initialize_four(self, surface):
        pygame.draw.rect(surface, Colors.BLACK,
                         (Scoreboard.NUMBER_STROKE_WIDTH,
                         0,
                         Scoreboard.NUMBER_STROKE_WIDTH,
                         Scoreboard.NUMBER_STROKE_WIDTH * 2))
        
        pygame.draw.rect(surface, Colors.BLACK,
                         (0,
                          Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_HEIGHT))

    def initialize_five(self, surface):
        pygame.draw.rect(surface, Colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, Colors.BLACK,
                          (0,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_six(self, surface):
        pygame.draw.rect(surface, Colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, Colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_seven(self, surface):
        pygame.draw.rect(surface, Colors.BLACK, 
                         (0, 
                          Scoreboard.NUMBER_STROKE_WIDTH, 
                          2 * Scoreboard.NUMBER_STROKE_WIDTH, 
                          Scoreboard.NUMBER_HEIGHT))

    def initialize_eight(self, surface):
        pygame.draw.rect(surface, Colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, Colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_nine(self, surface):
        pygame.draw.rect(surface, Colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, Colors.BLACK,
                          (0,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH * 2,
                           Scoreboard.NUMBER_STROKE_WIDTH))
