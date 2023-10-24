import pygame
from colors import *

class Paddle(pygame.sprite.Sprite):

    UP = -1
    DOWN = 1
    MOVE_INCREMENT = 2

    WIDTH = 10
    HEIGHT = 100

    def __init__(self, x_pos, y_range):
        super().__init__()

        self.min_y = y_range[0]
        self.max_y = y_range[1]
        self.move_direction = 0

        self.image = pygame.Surface((Paddle.WIDTH, Paddle.HEIGHT))
        self.image.fill(Colors.WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x_pos - Paddle.WIDTH // 2
        self.rect.y = (self.max_y - self.min_y - Paddle.HEIGHT) // 2 + self.min_y

    def check_for_movement(self, up, down):
        if up:
            self.move_direction = Paddle.UP
        elif down:
            self.move_direction = Paddle.DOWN
        else:
            self.move_direction = 0

    def update(self):
        self.rect.y += self.move_direction * self.MOVE_INCREMENT
        if self.rect.y + Paddle.HEIGHT > self.max_y:
            self.rect.y = self.max_y - Paddle.HEIGHT
        elif self.rect.y < self.min_y:
            self.rect.y = self.min_y
