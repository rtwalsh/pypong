import pygame
import random
import math
from colors import *
from scorekeeper import *

class Ball(pygame.sprite.Sprite):

    MIN_ANGLE = -70
    MAX_ANGLE = -MIN_ANGLE
    HORIZONTAL = 0
    VERTICAL = 1
    BOUNCE_VARIANCE = 0.2

    def __init__(self, scorekeeper, size, x_range, y_range):
        super().__init__()

        self.scorekeeper = scorekeeper

        self.size = size
        self.arena_bounds = (x_range, (y_range[0] + self.size, y_range[1] - self.size))
        self.arena_center = ((self.arena_bounds[0][1] - self.arena_bounds[0][0]) // 2 + self.arena_bounds[0][0], (self.arena_bounds[1][1] - self.arena_bounds[1][0]) // 2 + self.arena_bounds[1][0])

        self.image = pygame.Surface((size * 2, size * 2))
        self.image.fill(Colors.BLACK)
        self.image.set_colorkey(Colors.BLACK)
        self.rect = self.image.get_rect()

        pygame.draw.circle(self.image, Colors.WHITE, (size, size), self.size)

        self.speed = 5

        self.initialize_ball()

    def initialize_ball(self):
        self.rect.x = self.arena_center[0] - self.size
        self.rect.y = self.arena_center[1] - self.size

        angle = math.radians(random.randint(Ball.MIN_ANGLE, Ball.MAX_ANGLE) + random.choice([0, 180]))
        self.delta_x = math.cos(angle)
        self.delta_y = math.sin(angle)

    def update(self):
        self.rect.x += self.speed * self.delta_x
        self.rect.y += self.speed * self.delta_y

        if self.rect.x < self.arena_bounds[0][0]:
            self.scorekeeper.award_point(Scorekeeper.RIGHT_PLAYER)
            self.initialize_ball()
            self.update()

        if self.rect.x + self.size > self.arena_bounds[0][1]:
            self.scorekeeper.award_point(Scorekeeper.LEFT_PLAYER)
            self.initialize_ball()
            self.update()

    def bounce(self, direction):
        if direction == Ball.HORIZONTAL:
            self.delta_x = -self.delta_x
            self.delta_y += random.random() * Ball.BOUNCE_VARIANCE * random.choice([-1, 1])
        elif direction == Ball.VERTICAL:
            self.delta_y = -self.delta_y
            self.delta_x += random.random() * Ball.BOUNCE_VARIANCE * random.choice([-1, 1])
