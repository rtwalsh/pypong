import pygame
import random
import math
from scorekeeper import *
import colors

class Ball:

    SIZE = 5
    MIN_ANGLE = -60
    MAX_ANGLE = -MIN_ANGLE
    HORIZONTAL = 0
    VERTICAL = 1
    BOUNCE_VARIANCE = 0.2
    INITIAL_SPEED = 5

    def __init__(self, court, scorekeeper):
        self.size = Ball.SIZE
        self.initial_position = court.get_center()
        court.set_ball(self)
        self.scorekeeper = scorekeeper
        self.bounce_sound = pygame.mixer.Sound("./assets/sounds/4359__noisecollector__pongblipf4.wav")
        
        self.initialize_ball()

    def initialize_ball(self):
        self.position = self.initial_position
        angle = math.radians(random.randint(Ball.MIN_ANGLE, Ball.MAX_ANGLE) + random.choice([0, 180]))
        self.delta_x = math.cos(angle)
        self.delta_y = math.sin(angle)
        self.speed = Ball.INITIAL_SPEED
        self.rally_count = 0

    def draw(self, surface):
        pygame.draw.circle(surface, colors.WHITE, self.position, self.size)

    def update(self, bounds):
        new_x = self.get_new_x()
        if new_x - self.size < 0:
            print("Point for right")
            self.scorekeeper.award_point(Scorekeeper.RIGHT_PLAYER)
            self.initialize_ball()
            return
        elif new_x + self.size > bounds[0]:
            print("Point for left")
            self.scorekeeper.award_point(Scorekeeper.LEFT_PLAYER)
            self.initialize_ball()
            return

        # if new_x < 0 or new_x > bounds[0]:
        #     self.bounce(Ball.HORIZONTAL)
        #     new_x = self.get_new_x()

        new_y = self.get_new_y()
        if new_y - self.size < 0 or new_y + self.size > bounds[1]:
            self.bounce(Ball.VERTICAL)
            new_y = self.get_new_y()

        self.position = (new_x, new_y)

    def get_new_x(self):
        return self.position[0] + self.speed * self.delta_x

    def get_new_y(self):
        return self.position[1] + self.speed * self.delta_y
    
    def bounce(self, direction):
        #self.bounce_sound.play()
        if direction == Ball.HORIZONTAL:
            self.delta_x = -self.delta_x
            self.delta_y += random.random() * Ball.BOUNCE_VARIANCE * random.choice([-1, 1])
        elif direction == Ball.VERTICAL:
            self.delta_y = -self.delta_y
            self.delta_x += random.random() * Ball.BOUNCE_VARIANCE * random.choice([-1, 1])

    def check_for_contact(self, objects):
        center_x, center_y = self.position
        diameter = 2 * self.size
        ball_rect = pygame.Rect(center_x - self.size, center_y - self.size, diameter, diameter)
        for object in objects:
            if object != self: #ball_rect.colliderect(object.get_rect()):
                bounce_direction = object.is_touching(ball_rect, Ball.HORIZONTAL, Ball.VERTICAL)
                if not bounce_direction is None:
                    print("Collision detected between", ball_rect, "and", object.get_rect())
                    self.bounce(bounce_direction) #Ball.HORIZONTAL)
                    self.rally_count += 1
                    if self.rally_count % 10 == 0:
                        self.speed += 1
                    break