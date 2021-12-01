from widgets.input_text import InputText
from widgets.mybutton import MyButton
from tkinter import messagebox
from tkinter import *


class HomeScreen:
    def __init__(self, pg, screen, font, color_active, color_inactive, players, go_to):
        self.color_inactive = color_inactive
        self.color_active = color_active
        self.color = self.color_inactive
        self.players = players
        self.screen = screen
        self.font = font
        self.pg = pg

        self.go_to = go_to
        self.clock = self.pg.time.Clock()

        self.input_boxes = [
            InputText(self.pg, self.font, self.color_active, self.color_inactive,
                      int((710 * 2.4 / 2) - 200), 100 + (k * 50), 300, 32, f'Player {k + 1}', p) for k, p in
            enumerate(players)
        ]

        self.init_game = MyButton(" Iniciar Game ", (int(710 * 2.4 / 2 - 180),
                                                         int(480 * .65)), self.pg, 30, self.start_game)

        self.ranking = MyButton(" Ranking ", (int(710 * 2.4 / 2 + 20),
                                                  int(480 * .65)), self.pg, 30, lambda: go_to('ranking'))

        self.active = False
        self.text = ''
        self.done = False

    def start_game(self):
        miss = 0

        for p in self.players:
            if str(p[0]).strip() == '':
                miss += 1

        if miss > 2:
            Tk().wm_withdraw()
            messagebox.showinfo('Erro', 'Por favor, '
                                        'preencha pelo meno o nome de 2 jogadores para continuar')

        else:
            i = 0
            while i < len(self.players):
                if i >= len(self.players):
                    break

                if str(self.players[i][0]).strip() == '':
                    self.players.pop(i)

                else:
                    i += 1

            self.go_to('game')

    def update(self):
        for event in self.pg.event.get():
            if event.type == self.pg.QUIT:
                self.pg.quit()
                exit()

            for box in self.input_boxes:
                box.handle_event(event)

            self.ranking.click(event)
            self.init_game.click(event)

        for box in self.input_boxes:
            box.update()

        self.screen.fill((30, 30, 30))
        for box in self.input_boxes:
            box.draw(self.screen)

        self.ranking.draw(self.screen)
        self.init_game.draw(self.screen)
        self.pg.display.flip()
        self.clock.tick(30)
