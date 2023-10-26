import pygame
from arena import *
from paddle import *
from ball import *
from colors import *

pygame.init()

WIDTH = 800
HEIGHT = 600

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

scoreboard = Scoreboard(WIDTH, 100)
bottom_panel = Panel(WIDTH, 50, HEIGHT - 50, Border.TOP)

arena_top = scoreboard.rect.height
arena_bottom = HEIGHT - bottom_panel.rect.height

net = Net(arena_top, arena_bottom, WIDTH // 2)
paddle1 = Paddle(20, (arena_top, arena_bottom))
paddle2 = Paddle(WIDTH - 20, (arena_top, arena_bottom))
ball = Ball(5, (0, WIDTH), (arena_top, arena_bottom))

all_sprites = pygame.sprite.Group()
all_sprites.add(scoreboard)
all_sprites.add(bottom_panel)
all_sprites.add(net)
all_sprites.add(paddle1)
all_sprites.add(paddle2)
all_sprites.add(ball)

boundaries = pygame.sprite.Group()
boundaries.add(scoreboard)
boundaries.add(bottom_panel)

paddles = pygame.sprite.Group()
paddles.add(paddle1)
paddles.add(paddle2)

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not done:
        screen.fill(Colors.BLACK)

        keys = pygame.key.get_pressed()
        paddle1.check_for_movement(keys[pygame.K_w], keys[pygame.K_s])
        paddle2.check_for_movement(keys[pygame.K_UP], keys[pygame.K_DOWN])

        all_sprites.update()

        collisions = pygame.sprite.spritecollide(ball, boundaries, False)
        for collision in collisions:
            ball.bounce(Ball.VERTICAL)
            break

        collisions = pygame.sprite.spritecollide(ball, paddles, False)
        for collision in collisions:
            ball.bounce(Ball.HORIZONTAL)
            break

        collisions = pygame.sprite.spritecollide(paddle1, boundaries, False)
        for collision in collisions:
            paddle1.stop_moving()

        collisions = pygame.sprite.spritecollide(paddle2, boundaries, False)
        for collision in collisions:
            paddle2.stop_moving()
            
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(30)

pygame.quit()
