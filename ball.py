import pygame
import random
import math
from colors import *

class Ball(pygame.sprite.Sprite):

    MIN_ANGLE = -70
    MAX_ANGLE = -MIN_ANGLE
    HORIZONTAL = 0
    VERTICAL = 1

    def __init__(self, size, x_range, y_range):
        super().__init__()
        self.size = size
        center = ((x_range[1] - x_range[0]) // 2 + x_range[0], (y_range[1] - y_range[0]) // 2 + y_range[0])
        self.bounds = (x_range, (y_range[0] + self.size, y_range[1] - self.size))

        angle = self.to_radians(random.randint(Ball.MIN_ANGLE, Ball.MAX_ANGLE) + random.choice([0, 180]))
        self.delta_x = math.cos(angle)
        self.delta_y = math.sin(angle)
        self.speed = 5

        self.image = pygame.Surface((size * 2, size * 2))
        self.image.fill(Colors.BLACK)
        self.image.set_colorkey(Colors.BLACK)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, Colors.WHITE, (size, size), self.size)
        self.rect.x = center[0] - size
        self.rect.y = center[1] - size

    def update(self):
        self.rect.x += self.speed * self.delta_x
        self.rect.y += self.speed * self.delta_y
        if self.rect.x < self.bounds[0][0] or self.rect.x + self.size > self.bounds[0][1]:
            self.bounce(Ball.HORIZONTAL)

    def bounce(self, direction):
        if direction == Ball.HORIZONTAL:
            self.delta_x = -self.delta_x
        elif direction == Ball.VERTICAL:
            self.delta_y = -self.delta_y

    def to_radians(self, degrees):
        return degrees * math.pi / 180
