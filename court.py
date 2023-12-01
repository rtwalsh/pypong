import pygame
import colors
#from ball import *

class Court:

    LEFT_PADDLE = -1
    RIGHT_PADDLE = 1

    def __init__(self, left, top, width, height):
        self.surface = pygame.Surface((width, height))
        self.x = left
        self.y = top
        self.game_objects = []

    def get_width(self):
        return self.surface.get_width()
    
    def get_center(self):
        return self.surface.get_rect().center
    
    def set_ball(self, ball):
        self.ball = ball
        self.add_object(ball)

    def set_paddle(self, paddle, which):
        if which == Court.LEFT_PADDLE:
            self.left_paddle = paddle
        else:
            self.right_paddle = paddle
        self.add_object(paddle)

    def add_object(self, obj):
        self.game_objects.append(obj)

    def update(self):
        for obj in self.game_objects:
            obj.update(self.surface.get_size())

        self.ball.check_for_contact([self.left_paddle, self.right_paddle])

    def draw(self, surface):
        self.surface.fill(colors.BLACK)
        right = self.surface.get_width() - 1
        bottom = self.surface.get_height() - 1
        pygame.draw.line(self.surface, colors.WHITE, (0, 0), (right, 0))
        pygame.draw.line(self.surface, colors.WHITE, (0, bottom), (right, bottom))
        self.draw_net()

        for obj in self.game_objects:
            obj.draw(self.surface)

        surface.blit(self.surface, (self.x, self.y))

    def draw_net(self):
        pos = 0
        center = self.surface.get_rect().centerx
        pen_down = False
        while pos < self.surface.get_height():
            if pen_down:
                pygame.draw.line(self.surface, colors.WHITE, (center, pos), (center, pos + 10))
            pos += 10
            pen_down = not pen_down
