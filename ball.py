import pygame
import random
import math

class Ball:

    WHITE = (255, 255, 255)

    def __init__(self, size, x_range, y_range):
        self.size = size
        self.position = ((x_range[1] - x_range[0]) // 2 + x_range[0], (y_range[1] - y_range[0]) // 2 + y_range[0])
        self.bounds = (x_range, (y_range[0] + self.size, y_range[1] - self.size))

        angle = self.to_radians(random.randint(-60, 60) + random.choice([0, 180]))
        self.delta_x = math.cos(angle)
        self.delta_y = math.sin(angle)
        self.speed = 5

    def draw(self, screen):
        pygame.draw.circle(screen, self.WHITE, self.position, self.size)

    def update(self):
        new_x = self.position[0] + self.speed * self.delta_x
        new_y = self.position[1] + self.speed * self.delta_y
        self.position = (new_x, new_y)
        if new_x < self.bounds[0][0] or new_x > self.bounds[0][1]:
            self.delta_x = -self.delta_x

        if new_y < self.bounds[1][0] or new_y > self.bounds[1][1]:
            self.delta_y = -self.delta_y

    def to_radians(self, degrees):
        return degrees * math.pi / 180