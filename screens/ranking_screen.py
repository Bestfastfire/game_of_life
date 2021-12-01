from widgets.mybutton import MyButton
from widgets.text import Text
from os import walk
import json


class RankingScreen:
    @staticmethod
    def _get_ranking():
        ranking = []

        file = open(f'./src/data/game_history.txt', 'r')
        history = file.read()

        history = str(history).split('\n')

        for item in history:
            try:
                item = item.replace('\'', '"')
                ranking.append(json.loads(str(item)))

            except:
                print('...')

        ranking = sorted(ranking, key=lambda x: x[1])
        ranking.reverse()

        return ranking[:11]

    def __init__(self, pg, screen, go_to):
        self.screen = screen
        self.pg = pg

        self.clock = self.pg.time.Clock()
        self.back = MyButton('Voltar', ((710 * 2.4) - 100, (int(411 * 2.4)) - 50), self.pg, 30, lambda: go_to('home'))
        self.background = self._generate_img('./src/background_home.png', 710 * 2.4, 411 * 2.4)

        self.texts = [
            Text(self.pg, ((710 * 2.4) / 2 - 100, 45 + (i * 45)), 30,
                 f'{i + 1}°: {player[0]} - R$ {player[1]}') for i, player in enumerate(RankingScreen._get_ranking())
        ]

    def _generate_img(self, src, width, height):
        img = self.pg.image.load(src)
        return self.pg.transform.scale(img, (int(width), int(height)))

    def update(self):
        self.screen.blit(self.background, (0, 0))

        for event in self.pg.event.get():
            if event.type == self.pg.QUIT:
                self.pg.quit()
                exit()

            self.back.click(event)

        for txt in self.texts:
            txt.draw(self.screen)

        self.back.draw(self.screen)
        self.pg.display.flip()
        self.clock.tick(30)
