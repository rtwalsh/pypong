import pygame
from colors import *

class Paddle:

    UP = -1
    DOWN = 1
    MOVE_INCREMENT = 2

    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100

    def __init__(self, x_pos, court, which):
        self.x = x_pos - self.PADDLE_WIDTH // 2
        self.y = court.get_center()[1] - self.PADDLE_HEIGHT // 2
        self.move_direction = 0
        court.set_paddle(self, which)

    def get_rect(self):
        return pygame.Rect((self.x, self.y), (Paddle.PADDLE_WIDTH, Paddle.PADDLE_HEIGHT))
    
    def draw(self, surface):
        pygame.draw.rect(surface, Colors.WHITE, self.get_rect())

    def check_for_movement(self, up, down):
        if up:
            self.move_direction = Paddle.UP
        elif down:
            self.move_direction = Paddle.DOWN
        else:
            self.move_direction = 0

    def update(self, bounds):
        self.y += self.move_direction * self.MOVE_INCREMENT
        if self.y + self.PADDLE_HEIGHT > bounds[1]:
            self.y = bounds[1] - self.PADDLE_HEIGHT
        elif self.y < 0:
            self.y = 0
