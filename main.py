import pygame
import time
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
WINNING_SCORE = 9

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

court = Court(0, SCOREBOARD_HEIGHT, WIDTH, HEIGHT - SCOREBOARD_HEIGHT - BOTTOM_PANEL_HEIGHT)
scorekeeper = Scorekeeper()
scoreboard = Scoreboard(scorekeeper, 0, 0, WIDTH, SCOREBOARD_HEIGHT)
left_paddle = Paddle(court, Court.LEFT_PADDLE)
right_paddle = Paddle(court, Court.RIGHT_PADDLE)
ball = Ball(court, scorekeeper)

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if scorekeeper.get_score(Scorekeeper.LEFT_PLAYER) == WINNING_SCORE or scorekeeper.get_score(Scorekeeper.RIGHT_PLAYER) == WINNING_SCORE:
        pygame.mixer.Sound("assets\sounds\mixkit-arcade-retro-game-over-213.wav").play()
        time.sleep(2)
        done = True

    if not done:
        screen.fill(colors.BLACK)

        keys = pygame.key.get_pressed()
        left_paddle.move(keys[pygame.K_w], keys[pygame.K_s])
        right_paddle.move(keys[pygame.K_UP], keys[pygame.K_DOWN])

        court.update()
        scoreboard.update()

        court.draw(screen)
        scoreboard.draw(screen)
        pygame.display.flip()

        clock.tick(FRAMES_PER_SECOND)


pygame.quit()

