import pygame
import colors

class Paddle:

    UP = -1
    DOWN = 1
    MOVE_AMOUNT = 3

    WIDTH = 10
    HEIGHT = 75

    def __init__(self, court, which):
        self.x = court.get_paddle_x(which) - Paddle.WIDTH // 2
        self.y = court.get_paddle_y() - Paddle.HEIGHT // 2
        self.move_direction = 0
        court.add_object(self)

    def get_rect(self):
        return pygame.Rect((self.x, self.y), (Paddle.WIDTH, Paddle.HEIGHT))
    
    def draw(self, surface):
        pygame.draw.rect(surface, colors.WHITE, self.get_rect())

    def move(self, up, down):
        if up:
            self.move_direction = Paddle.UP
        elif down:
            self.move_direction = Paddle.DOWN
        else:
            self.move_direction = 0

    def update(self, bounds):
        self.y += self.move_direction * self.MOVE_AMOUNT
        if self.y + Paddle.HEIGHT > bounds[1]:
            self.y = bounds[1] - Paddle.HEIGHT
        elif self.y < 0:
            self.y = 0

    def is_touching(self, rect, h_bounce_value, v_bounce_value):
        front_face = (self.x, self.y, self.x, self.y + Paddle.HEIGHT)
        if rect.clipline(front_face):
            return h_bounce_value
        
        top_edge = (self.x, self.y, self.x + Paddle.WIDTH, self.y)
        bottom_edge = (self.x, self.y + Paddle.HEIGHT, self.x + Paddle.WIDTH, self.y + Paddle.HEIGHT)
        if rect.clipline(top_edge) or rect.clipline(bottom_edge):
            return v_bounce_value
        
        return None
