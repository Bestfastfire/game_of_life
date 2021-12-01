from pygame.locals import *
# from model.colors import *
from model.roul_model import Roul
from model.player_model import Player
from random import randint, shuffle
from model.board_texts import BoardTexts
from sys import exit

from model.road_block import *


class GameScreen:
    def __init__(self, pg, screen, players, width=710 * 2.4, height=411 * 2.4, fps=30):
        self.players_len = len(players)
        self.height = int(height)
        self.width = int(width)
        self.fps = fps
        self.pg = pg

        self.roul = Roul(self, self.width * .15, self.width * .15, self.width - (self.width * 0.15) - self.width * 0.05,
                         self.width * .002)
        self.background = self._generate_img('./src/background.jpg', self.width, self.height)

        self.screen = screen
        self.all_sprites = self.pg.sprite.Group()
        self.positions = []
        self.road_txts = []
        self.road_len = 51
        self.rv_list = []

        self._create_road(12, self.road_len, 15, 15)
        self.current_player = 0
        self.old_player = 0
        self.players = []

        self.run(self.players)
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

                    self._put_road(texts, missing, x, y, rw, rh, i)
                    i += 1

                    y -= rh

                    if i < size:
                        self._put_road(texts, missing, x, y, rw, rh, i)
                        x += -rw if inFinal else +rw
                        invert = inFinal
                        i += 1

                        if i < size:
                            self._put_road(texts, missing, x, y, rw, rh, i)
                            i += 1

                    continue

                else:
                    if invert:
                        x -= rw

                    else:
                        x += rw

            self._put_road(texts, missing, x, y, rw, rh, i, i == 0)
            i += 1

    def _put_road(self, texts, missing, x, y, width, height, road_index, start=False):
        index = 0

        if not start:
            shuffle(missing)
            index = randint(0, len(missing) - 1)

        txt = texts[missing[index]]

        self.all_sprites.add(RoadBlock(self, x, y, width, height, txt[0][0], missing[index]))

        if missing[index] > 0:
            # print(f'index {road_index} -> {txt[0][1]}')
            self.rv_list.append([road_index, txt[0][1]])

        if not start:
            # max 19
            letter_len = width / 14
            txt_len = len(txt[0][0]) * letter_len
            self.put_text(txt[0][0], 14, x + (width - txt_len) / 2, y + height / 2 - 10)

        missing.pop(index)
        txt.pop(0)

    def get_txt(self, txt, fontsize):
        font = pygame.font.SysFont('arial', fontsize, True, False)
        return font.render(txt, True, (0, 0, 0))

    def put_text(self, txt, fontsize, x, y):
        self.road_txts.append([self.get_txt(txt, fontsize), (x, y)])

    def update_text(self, txt, index):
        item = self.road_txts[index]
        self.road_txts[index] = [self.get_txt(txt, 14), item[1]]

    def _generate_img(self, src, width, height):
        img = self.pg.image.load(src)
        return self.pg.transform.scale(img, (int(width), int(height)))

    def _get_road_block(self, road_index):
        for item in self.rv_list:
            if item[0] == road_index:
                return item[1]

        return 0

    def move_player(self, player, index):
        p = self.players[player]
        n = p.position_index + index
        right_index = p.position_index + index
        # print(self.road_txts[len(self.road_txts)-1].text)

        if n > 0:
            if n >= self.road_len - 1:
                p.move_to(self.road_len - 1)
                right_index = self.road_len - 1

            else:
                p.move_to(p.position_index + index)

        else:
            right_index = 0
            p.move_to(0)

        block_money = self._get_road_block(right_index)

        p.money = p.money + block_money

        # print(f'text: {self.players_len}')
        self.update_text(f'{p.name}: R$ {p.money}',
                         len(self.road_txts) + player - self.players_len)

        print(f'a: {len(self.road_txts)} | b: {player} | c: {self.players_len}')
        print(f'player: {player} move to {p.position_index + index} -> {p.money}')

    def run(self, players):
        self.all_sprites.add(self.roul)

        for k, p in enumerate(players):
            self.players.append(Player(self, p[0], p[1], k + 1))
            player = self.players[k]

            self.put_text(f'{player.name}: R$ {player.money}', 14, 40, 40 + k * 15)
            self.all_sprites.add(player)

    def update(self):
        self.pg.time.Clock().tick(self.fps)
        self.screen.blit(self.background, (0, 0))

        for event in self.pg.event.get():
            if event.type == QUIT:
                self.pg.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if not self.players[self.old_player].walking:
                        self.roul.roll(self.current_player)
                        self.old_player = self.current_player
                        self.current_player += 1

                        if self.current_player > len(self.players) - 1:
                            self.current_player = 0

        self.all_sprites.draw(self.screen)
        self.all_sprites.update()

        for txt in self.road_txts:
            self.screen.blit(txt[0], txt[1])

        # self.screen.blit(roul, ())
        self.pg.display.flip()
