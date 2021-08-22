import pygame

from pygame.locals import *
# from model.colors import *
from random import randint, shuffle
from model.board_texts import BoardTexts
from sys import exit

from model.road_block import *


class PGController:
    def __init__(self, width=710 * 2, height=411 * 2, fps=30):
        self.height = height
        self.width = width
        self.pg = pygame
        self.fps = fps
        self.pg.init()

        self.screen = self.pg.display.set_mode((self.width, self.height))
        self.all_sprites = self.pg.sprite.Group()
        self.road_txts = []

        self._create_road(12, 51, 12, 12)
        # self.all_sprites.add()

    def _create_road(self, horizontal_size=12, size=50, luck_roads=10, bad_roads=10):
        margin = self.width * 0.05

        rw = (self.width - margin * 2) / horizontal_size
        rh = rw * 0.714

        y = self.height - margin - rh
        x = self.width * 0.05

        # 0: blank, 1: luck, 2: bad
        texts = BoardTexts.generate_list(size, luck_roads, bad_roads)
        missing = [0 for i in range(size - bad_roads - luck_roads)] \
                  + [1 for i in range(luck_roads)] \
                  + [2 for i in range(bad_roads)]

        invert = False

        i = 0
        while i < size:
            if i > 0:
                inFinal = x >= (self.width * ((horizontal_size - 2) * rw) / self.width + margin + 10)
                inStart = x <= (rw + margin - 10) and invert

                if inFinal or inStart:
                    y -= rh

                    self._put_road(texts, missing, x, y, rw, rh)
                    i += 1

                    y -= rh

                    if i < size:
                        self._put_road(texts, missing, x, y, rw, rh)
                        x += -rw if inFinal else +rw
                        invert = inFinal
                        i += 1

                        if i < size:
                            self._put_road(texts, missing, x, y, rw, rh)
                            i += 1

                    continue

                else:
                    if invert:
                        x -= rw

                    else:
                        x += rw

            self._put_road(texts, missing, x, y, rw, rh, i == 0)
            i += 1

    def _put_road(self, texts, missing, x, y, width, height, start=False):
        index = 0

        if not start:
            shuffle(missing)
            index = randint(0, len(missing) - 1)

        txt = texts[missing[index]]

        self.all_sprites.add(RoadBlock(self, x, y, width, height, txt[0], missing[index]))

        if not start:
            # max 19
            letter_len = width/14
            txt_len = len(txt[0]) * letter_len
            self.put_text(txt[0], 14, x + (width - txt_len)/2, y+height/2-10)

        missing.pop(index)
        txt.pop(0)

    def put_text(self, txt, fontsize, x, y):
        font = pygame.font.SysFont('arial', fontsize, True, False)
        title = font.render(txt, True, (0, 0, 0))
        self.road_txts.append([title, (x, y)])

    def run(self):
        background = self.pg.image.load('./src/background.jpg').convert()
        background = self.pg.transform.scale(background, (self.width, self.height))

        while True:
            self.pg.time.Clock().tick(self.fps)
            self.screen.blit(background, (0, 0))

            for event in self.pg.event.get():
                if event.type == QUIT:
                    self.pg.quit()
                    exit()

            self.all_sprites.draw(self.screen)
            self.all_sprites.update()

            for txt in self.road_txts:
                self.screen.blit(txt[0], txt[1])

            self.pg.display.flip()
