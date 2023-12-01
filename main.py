import pygame
from court import *
from scorekeeper import *
from scoreboard import *
from paddle import *
from ball import *
import colors

pygame.init()

WIDTH = 800
HEIGHT = 600

SCOREBOARD_HEIGHT = 100
BOTTOM_PANEL_HEIGHT = 50

FRAMES_PER_SECOND = 60

BALL_SIZE = 5
PADDLE_MARGIN = 20

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

court = Court(0, SCOREBOARD_HEIGHT, WIDTH, HEIGHT - SCOREBOARD_HEIGHT - BOTTOM_PANEL_HEIGHT)
scorekeeper = Scorekeeper()
scoreboard = Scoreboard(scorekeeper, 0, 0, WIDTH, SCOREBOARD_HEIGHT)
paddle1 = Paddle(PADDLE_MARGIN, court, Court.LEFT_PADDLE)
paddle2 = Paddle(court.get_width() - PADDLE_MARGIN, court, Court.RIGHT_PADDLE)
ball = Ball(BALL_SIZE, court, scorekeeper)

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not done:
        screen.fill(colors.BLACK)

        keys = pygame.key.get_pressed()
        paddle1.check_for_movement(keys[pygame.K_w], keys[pygame.K_s])
        paddle2.check_for_movement(keys[pygame.K_UP], keys[pygame.K_DOWN])

        court.update()
        scoreboard.update()

        court.draw(screen)
        scoreboard.draw(screen)
        pygame.display.flip()

        clock.tick(FRAMES_PER_SECOND)

pygame.quit()
