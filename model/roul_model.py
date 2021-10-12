import pygame
from random import randint


class Roul(pygame.sprite.Sprite):
    __roul = [
       1, -2, 5, -1, 2, -5, 3, -2, 5, -1, 2, -5
    ]

    def __init__(self, controller, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            pygame.image.load(f'./src/sprites/roul/roul_{index}.png') for index in range(12)
        ]

        self.controller = controller
        self.current_sprite = 0
        self.height = int(height)
        self.width = int(width)

        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (int(self.width), int(self.height)))

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.rolling = False

        self.current_player = 0
        self.roul = 0
        self.last_roul = 0
        self.current = 0
        self.divisor = 6
        self.num = 0

    def roll(self, player):
        if self.rolling:
            return

        self.current_player = player
        self.roul = randint(0, 11)

        self.num = 360/12 * self.roul + (360 * 4)
        print(f'casas: {self.__roul[self.roul]}')

        self.last_roul = self.roul
        self.current_sprite = 2
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
                self.controller.move_player(self.current_player, self.__roul[self.roul])

