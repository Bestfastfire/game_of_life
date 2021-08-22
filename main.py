# pip install pygame
import sys
from controller.pygame_control import PGController
sys.setrecursionlimit(1000000)

pgControl = PGController()
pgControl.run()

# import pygame
# from pygame.locals import *
# from sys import exit
# import random
#
# pygame.init()
#
# width = 640
# height = 480
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Jogo da Vida')
# clock = pygame.time.Clock()
#
# font = pygame.font.SysFont('arial', 40, True, True)
# points = 0
#
# y = height / 2
# x = width / 2
#
# wy = random.randint(50, 430)
# wx = random.randint(40, 600)
#
#
# class Frog(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.sprites = [
#             pygame.image.load(f'./src/sprites/frog/attack_{index}.png').convert() for index in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         ]
#
#         self.sprite_actual = 0
#         self.image = self.sprites[self.sprite_actual]
#         self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))
#
#         self.rect = self.image.get_rect()
#         self.rect.topleft = 100, 100
#         self.animation = False
#
#     def attack(self):
#         self.animation = True
#
#     def update(self):
#         if self.animation:
#             self.sprite_actual += 0.5
#             if self.sprite_actual >= len(self.sprites):
#                 self.sprite_actual = 0
#                 self.animation = False
#
#             self.image = self.sprites[int(self.sprite_actual)]
#             self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))
#
#
# all_sprites = pygame.sprite.Group()
# frog = Frog()
# all_sprites.add(frog)
#
#
# while True:
#     clock.tick(30)
#     screen.fill((0, 0, 0))
#     message = f'Pontos: {points}'
#     title = font.render(message, True, (255, 255, 255))
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#
#         # on press key
#         if event.type == KEYDOWN:
#             if event.key == K_SPACE:
#                 frog.attack()
#
#         # if event.type == KEYDOWN:
#         #     if event.key == K_a:
#         #         x += -10
#         #
#         #     if event.key == K_d:
#         #         x += 10
#         #
#         #     if event.key == K_w:
#         #         y += -10
#         #
#         #     if event.key == K_s:
#         #         y += 10
#
#     # hold key
#     if pygame.key.get_pressed()[K_a]:
#         x += -10
#
#     if pygame.key.get_pressed()[K_d]:
#         x += 10
#
#     if pygame.key.get_pressed()[K_w]:
#         y += -10
#
#     if pygame.key.get_pressed()[K_s]:
#         y += 10
#
#     player = pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))
#     wall = pygame.draw.rect(screen, (0, 0, 255), (wx, wy, 40, 50))
#
#     # collision
#     if wall.colliderect(player):
#         wy = random.randint(50, 430)
#         wx = random.randint(40, 600)
#         points += 1
#
#     # if y >= height:
#     #     y = 0
#     #
#     # y += 1
#     # pygame.draw.circle(screen, (0, 0, 255), (250, 350), 40)
#     # pygame.draw.line(screen, (255, 255, 0), (390, 0), (390, 600), 4)
#
#     screen.blit(title, (400, 40))
#     all_sprites.draw(screen)
#     all_sprites.update()
#     pygame.display.flip()
