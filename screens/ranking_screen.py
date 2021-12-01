from widgets.mybutton import MyButton
from widgets.text import Text
from os import walk
import json


class RankingScreen:
    @staticmethod
    def _get_winner_ranking(my_list):
        player = my_list[0]

        for item in my_list:
            if int(item[2]) > int(player[2]):
                player = item

        return player[0], player[2]

    @staticmethod
    def _get_ranking():
        ranking = []

        for (dirpath, dirnames, filenames) in walk('./data/'):
            for file in filenames:
                print(f'{file}')
                if '.txt' in file:
                    # try:
                    file = open(file, 'r')
                    historico = file.read()
                    last = str(historico).split('\n')
                    last = last[len(last) - 2]

                    last = last.replace('\'', '"')
                    last = json.loads(str(last))

                    ranking.append(RankingScreen._get_winner_ranking(last))

        ranking = sorted(ranking, key=lambda x: x[1])
        ranking.reverse()

        return ranking[:11]

    def __init__(self, pg, screen, go_to):
        self.screen = screen
        self.pg = pg

        self.clock = self.pg.time.Clock()
        self.back = MyButton('Voltar', ((710 * 2.4) - 100, (int(411 * 2.4)) - 50), self.pg, 30, lambda: go_to('home'))

        self.texts = [
            Text(self.pg, ((710 * 2.4)/2-100, 45 + (i * 45)), 30,
                 f'{i+1}° - {player[0]} - R$ {player[1]}') for i, player in enumerate(RankingScreen._get_ranking())
        ]

        # self.texts = [
        #     Text(self.pg, (900 / 2 - 100, 100 + (0 * 45)), 30,
        #          f'Teste - R$ {1000}')
        # ]

    def update(self):
        for event in self.pg.event.get():
            if event.type == self.pg.QUIT:
                self.pg.quit()
                exit()

            self.back.click(event)

        self.screen.fill((30, 30, 30))

        for txt in self.texts:
            txt.draw(self.screen)

        self.back.draw(self.screen)
        self.pg.display.flip()
        self.clock.tick(30)
