import pygame

class Paddle:

    WHITE = (255, 255, 255)
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100

    def __init__(self, x_pos, y_range):
        self.x = x_pos - self.PADDLE_WIDTH // 2
        self.min_y = y_range[0]
        self.max_y = y_range[1]
        self.y = (self.max_y - self.min_y - self.PADDLE_HEIGHT) // 2 + self.min_y

    def draw(self, screen):
        pygame.draw.rect(screen, self.WHITE, pygame.Rect((self.x, self.y), (self.PADDLE_WIDTH, self.PADDLE_HEIGHT)))