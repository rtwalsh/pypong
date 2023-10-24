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

arena = Arena(size)
paddle1 = Paddle(20, (arena.top, arena.bottom))
paddle2 = Paddle(arena.right - 20, (arena.top, arena.bottom))
ball = Ball(5, (arena.left, arena.right), (arena.top, arena.bottom))

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1)
all_sprites.add(paddle2)
all_sprites.add(ball)

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

        collisions = pygame.sprite.spritecollide(ball, paddles, False)
        for collision in collisions:
            ball.bounce(Ball.HORIZONTAL)
            break

        arena.draw(screen)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(30)

pygame.quit()
