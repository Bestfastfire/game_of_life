# from controller.pygame_control import PGController
import pygame


class RoadBlock(pygame.sprite.Sprite):
    def __init__(self, controller, x, y, width, height, text, index=0, vertical=False):
        # print(f'x: {x} | y: {y}')
        pygame.sprite.Sprite.__init__(self)
        self.controller = controller
        self.current_sprite = index
        self.vertical = vertical
        self.text = text
        self.x = x
        self.y = y

        self.height = height
        self.width = width

        self.sprites = [
            pygame.image.load('./src/road/blank_road.png').convert(),
            pygame.image.load('./src/road/luck_road.png').convert(),
            pygame.image.load('./src/road/bad_road.png').convert()
        ]

        self.update(self.current_sprite)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def update(self, index=0):
        # self.current_sprite = index
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (int(self.width), int(self.height)))

        if self.vertical:
            self.image = pygame.transform.rotate(self.image, 90)

        # self.rect = self.image.get_rect()
