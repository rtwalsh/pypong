import pygame
import random
import math
from scorekeeper import *
from colors import *

class Ball:

    MIN_ANGLE = -60
    MAX_ANGLE = -MIN_ANGLE
    HORIZONTAL = 0
    VERTICAL = 1
    BOUNCE_VARIANCE = 0.2
    SPEED = 5

    def __init__(self, size, court, scorekeeper):
        self.size = size
        self.court = court
        self.court.set_ball(self)
        self.scorekeeper = scorekeeper

        self.initialize_ball()

    def initialize_ball(self):
        self.position = self.court.get_center()
        angle = math.radians(random.randint(Ball.MIN_ANGLE, Ball.MAX_ANGLE) + random.choice([0, 180]))
        self.delta_x = math.cos(angle)
        self.delta_y = math.sin(angle)
        self.speed = Ball.SPEED

    def draw(self, surface):
        pygame.draw.circle(surface, Colors.WHITE, self.position, self.size)

    def update(self, bounds):
        self.position = self.get_new_position(bounds)

    def get_new_position(self, bounds):
        new_x = self.get_new_x()
        if new_x - self.size < 0:
            print("Point for right")
            self.scorekeeper.award_point(Scorekeeper.RIGHT_PLAYER)
            self.initialize_ball()
            return self.position
        elif new_x + self.size > bounds[0]:
            print("Point for left")
            self.scorekeeper.award_point(Scorekeeper.LEFT_PLAYER)
            self.initialize_ball()
            return self.position
        
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
            self.delta_y += random.random() * Ball.BOUNCE_VARIANCE * random.choice([-1, 1])
        elif direction == Ball.VERTICAL:
            self.delta_y = -self.delta_y
            self.delta_x += random.random() * Ball.BOUNCE_VARIANCE * random.choice([-1, 1])

    def check_for_contact(self, paddles):
        center = self.position
        diameter = 2 * self.size
        ball_rect = pygame.Rect(center[0] - self.size, center[1] - self.size, diameter, diameter)
        for paddle in paddles:
            if ball_rect.colliderect(paddle.get_rect()):
                print("Collision detected between", ball_rect, "and", paddle.get_rect())
                self.bounce(Ball.HORIZONTAL)
                break