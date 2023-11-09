import pygame
import random
import math
from colors import *

class Ball:

    MIN_ANGLE = -70
    MAX_ANGLE = -MIN_ANGLE
    HORIZONTAL = 0
    VERTICAL = 1

    def __init__(self, size, court):
        self.size = size
        self.position = court.get_center()
        court.set_ball(self)

        angle = math.radians(random.randint(Ball.MIN_ANGLE, Ball.MAX_ANGLE) + random.choice([0, 180]))
        self.delta_x = math.cos(angle)
        self.delta_y = math.sin(angle)
        self.speed = 5

    def draw(self, surface):
        pygame.draw.circle(surface, Colors.WHITE, self.position, self.size)

    def update(self, bounds):
        self.position = self.get_new_position(bounds)

    def get_new_position(self, bounds):
        new_x = self.get_new_x()
        if new_x - self.size < 0 or new_x + self.size > bounds[0]:
            self.bounce(Ball.HORIZONTAL)
            new_x = self.get_new_x()

        new_y = self.get_new_y()
        if new_y - self.size < 0 or new_y + self.size > bounds[1]:
            self.bounce(Ball.VERTICAL)
            new_y = self.get_new_y()

        return (new_x, new_y)

    def get_new_x(self):
        return self.position[0] + self.speed * self.delta_x

    def get_new_y(self):
        return self.position[1] + self.speed * self.delta_y
    
    def bounce(self, direction):
        if direction == Ball.HORIZONTAL:
            self.delta_x = -self.delta_x
        elif direction == Ball.VERTICAL:
            self.delta_y = -self.delta_y
