import pygame

class Paddle:

    UP = -1
    DOWN = 1
    MOVE_INCREMENT = 2

    WHITE = (255, 255, 255)
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100

    def __init__(self, x_pos, y_range):
        self.x = x_pos - self.PADDLE_WIDTH // 2
        self.min_y = y_range[0]
        self.max_y = y_range[1]
        self.y = (self.max_y - self.min_y - self.PADDLE_HEIGHT) // 2 + self.min_y
        self.move_direction = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.WHITE, pygame.Rect((self.x, self.y), (self.PADDLE_WIDTH, self.PADDLE_HEIGHT)))

    def check_for_movement(self, up, down):
        if up:
            self.move_direction = Paddle.UP
        elif down:
            self.move_direction = Paddle.DOWN
        else:
            self.move_direction = 0

    def update(self):
        self.y += self.move_direction * self.MOVE_INCREMENT
        if self.y + self.PADDLE_HEIGHT > self.max_y:
            self.y = self.max_y - self.PADDLE_HEIGHT
        elif self.y < self.min_y:
            self.y = self.min_y
