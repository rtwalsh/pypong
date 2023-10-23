import pygame
from arena import *
from paddle import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

WIDTH = 800
HEIGHT = 600

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

arena = Arena(size)
paddle1 = Paddle(20, (arena.top, arena.bottom))
paddle2 = Paddle(arena.right - 20, (arena.top, arena.bottom))

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not done:
        screen.fill(BLACK)

        keys = pygame.key.get_pressed()
        paddle1.check_for_movement(keys[pygame.K_w], keys[pygame.K_s])
        paddle1.update()

        paddle2.check_for_movement(keys[pygame.K_UP], keys[pygame.K_DOWN])
        paddle2.update()

        arena.draw(screen)
        paddle1.draw(screen)
        paddle2.draw(screen)

        pygame.display.flip()
        clock.tick(30)

pygame.quit()
