import pygame
import colors
from scorekeeper import *

class Scoreboard():

    TOP_MARGIN = 20
    SIDE_MARGIN = 50
    NUMBER_WIDTH = 30
    NUMBER_HEIGHT = 50
    NUMBER_STROKE_WIDTH = 10

    def __init__(self, scorekeeper, left, top, width, height):
        self.surface = pygame.Surface((width, height))
        self.x = left
        self.y = top
        self.scorekeeper = scorekeeper

        self.initialize_numbers()

    def update(self):
        pass

    def draw(self, surface):
        self.surface.fill(colors.BLACK)
        left_score = self.scorekeeper.get_score(Scorekeeper.LEFT_PLAYER)
        right_score = self.scorekeeper.get_score(Scorekeeper.RIGHT_PLAYER)
        self.surface.blit(self.numbers[left_score], (self.x + Scoreboard.SIDE_MARGIN, self.y + Scoreboard.TOP_MARGIN))
        self.surface.blit(self.numbers[right_score], (self.x + self.surface.get_width() - Scoreboard.SIDE_MARGIN - Scoreboard.NUMBER_WIDTH, self.y + Scoreboard.TOP_MARGIN))
        surface.blit(self.surface, (self.x, self.y))
        
    def initialize_numbers(self):
        self.numbers = []
        for _ in range(0, 10):
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
