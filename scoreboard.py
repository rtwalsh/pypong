import pygame
import colors
from scorekeeper import *

class Scoreboard():

    NUMBER_TOP = 20
    NUMBER_WIDTH = 30
    NUMBER_HEIGHT = 50
    NUMBER_STROKE_WIDTH = 10
    NUMBER_MARGIN = 50

    def __init__(self, scorekeeper, left, top, width, height):
        self.surface = pygame.Surface((width, height))
        self.surface.fill(colors.BLACK)
        self.x = left
        self.y = top

        self.initialize_numbers()
        self.scorekeeper = scorekeeper

    def update(self):
        self.surface.blit(self.numbers[self.scorekeeper.get_score(Scorekeeper.LEFT_PLAYER)], (self.x + Scoreboard.NUMBER_MARGIN, self.y + Scoreboard.NUMBER_TOP))
        self.surface.blit(self.numbers[self.scorekeeper.get_score(Scorekeeper.RIGHT_PLAYER)], (self.x + self.surface.get_width() - Scoreboard.NUMBER_MARGIN - Scoreboard.NUMBER_WIDTH, self.y + Scoreboard.NUMBER_TOP))
        
    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))
        
    def initialize_numbers(self):
        self.numbers = []
        for i in range(0, 10):
            surface = pygame.Surface((Scoreboard.NUMBER_WIDTH, Scoreboard.NUMBER_HEIGHT))
            surface.fill(colors.WHITE)
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
        pygame.draw.rect(surface, colors.BLACK, 
                         (Scoreboard.NUMBER_STROKE_WIDTH, 
                          Scoreboard.NUMBER_STROKE_WIDTH, 
                          Scoreboard.NUMBER_STROKE_WIDTH, 
                          Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_one(self, surface):
        pygame.draw.rect(surface, colors.BLACK, 
                         (0, 
                          0, 
                          Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH, 
                          Scoreboard.NUMBER_HEIGHT))

    def initialize_two(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                          (0,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))
        
    def initialize_three(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                          (0,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, colors.BLACK,
                          (0,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))
        
    def initialize_four(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                         (Scoreboard.NUMBER_STROKE_WIDTH,
                         0,
                         Scoreboard.NUMBER_STROKE_WIDTH,
                         Scoreboard.NUMBER_STROKE_WIDTH * 2))
        
        pygame.draw.rect(surface, colors.BLACK,
                         (0,
                          Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_HEIGHT))

    def initialize_five(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, colors.BLACK,
                          (0,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH - Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_six(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_seven(self, surface):
        pygame.draw.rect(surface, colors.BLACK, 
                         (0, 
                          Scoreboard.NUMBER_STROKE_WIDTH, 
                          2 * Scoreboard.NUMBER_STROKE_WIDTH, 
                          Scoreboard.NUMBER_HEIGHT))

    def initialize_eight(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_nine(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                          (Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, colors.BLACK,
                          (0,
                           Scoreboard.NUMBER_HEIGHT - 2 * Scoreboard.NUMBER_STROKE_WIDTH,
                           Scoreboard.NUMBER_STROKE_WIDTH * 2,
                           Scoreboard.NUMBER_STROKE_WIDTH))
