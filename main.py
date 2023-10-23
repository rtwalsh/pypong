import pygame
from arena import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

WIDTH = 800
HEIGHT = 600

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

arena = Arena(size)

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not done:
        screen.fill(BLACK)

        arena.draw(screen)
        
        pygame.display.flip()
        clock.tick(30)

pygame.quit()
