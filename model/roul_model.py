import pygame
from random import randint


class Roul(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            pygame.image.load(f'./src/sprites/roul/roul_{index}.png') for index in range(12)
        ]

        self.current_sprite = 0
        self.height = int(height)
        self.width = int(width)

        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (int(self.width), int(self.height)))

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.rolling = False

        self.last_roul = 0
        self.current = 0
        self.divisor = 6
        self.num = 0

    def roll(self):
        if self.rolling:
            return

        g = randint(0, 11)

        self.num = 360/12 * g + (360 * 4)
        print(f'g: {g}')

        self.current_sprite = 2
        self.last_roul = g
        self.current = 0
        self.divisor = 6
        self.rolling = True

    def update(self):
        if self.rolling:
            self.current_sprite += 24*0.5/self.divisor
            self.current += 360/self.divisor
            self.divisor += 0.5

            if int(self.current_sprite) > len(self.sprites)-1:
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

            if self.current >= self.num:
                self.rolling = False

