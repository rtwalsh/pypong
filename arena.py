import pygame

class Arena:

    WHITE = (255, 255, 255)

    def __init__(self, screen_size):
        self.top = 100
        self.left = 0
        self.bottom = screen_size[1] - 50
        self.right = screen_size[0]
        self.center = (self.right - self.left) // 2

    def draw(self, screen):
        pygame.draw.line(screen, self.WHITE, (self.left, self.top), (self.right, self.top))
        pygame.draw.line(screen, self.WHITE, (self.left, self.bottom), (self.right, self.bottom))

        self.draw_net(screen)

    def draw_net(self, screen):
        pos = 100
        on = False
        while pos < self.bottom:
            if on:
                pygame.draw.line(screen, self.WHITE, (self.center, pos), (self.center, pos + 10))
            pos += 10
            on = not on
