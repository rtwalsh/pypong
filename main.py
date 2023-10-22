import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

WIDTH = 800
HEIGHT = 600

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

arena = {
    "top": 100,
    "bottom": HEIGHT - 50,
    "left": 0,
    "right": WIDTH,
    "center": WIDTH // 2
}

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not done:
        screen.fill(BLACK)

        pygame.draw.line(screen, WHITE, (arena["left"], arena["top"]), (arena["right"], arena["top"]))
        pygame.draw.line(screen, WHITE, (arena["left"], arena["bottom"]), (arena["right"], arena["bottom"]))

        pos = 100
        on = False
        while pos < arena["bottom"]:
            if on:
                pygame.draw.line(screen, WHITE, (arena["center"], pos), (arena["center"], pos + 10))
            pos += 10
            on = not on

        pygame.display.flip()
        clock.tick(30)

pygame.quit()
