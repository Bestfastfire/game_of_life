# pip install pygame

from screens.ranking_screen import RankingScreen
from screens.home_screen import HomeScreen
from screens.game_screen import GameScreen
import pygame as pg

pg.init()
screen = pg.display.set_mode((int(710 * 2.4), int(411 * 2.4)))
COLOR_INACTIVE = pg.Color('black')
COLOR_ACTIVE = pg.Color('red')
FONT = pg.font.Font(None, 32)
colors = [
    'Vermelho',
    'Verde',
    'Azul',
    'Branco'
]

players = [
    [
        '',
        400,
        colors[i],
        i
    ] for i in range(4)
]

current_screen = 'home'


def to_scene(screen_name):
    global current_screen, scenes, pg, screen, players
    current_screen = screen_name

    if current_screen == 'game':
        scenes['game'] = GameScreen(pg, screen, players, to_scene)


scenes = {
    'home': HomeScreen(pg, screen, FONT, COLOR_ACTIVE, COLOR_INACTIVE, colors, players, to_scene),
    'ranking': RankingScreen(pg, screen, to_scene)
}


def main():
    done = False

    while not done:
        scenes[current_screen].update()


main()

# print(f'Olá, seja bem vindo ao jogo da vida!\nPara começar:')
# while len(players) < PLAYER_LEN:
#     player = input(f'Digite o nome do jogador {len(players)+1} (máximo {PLAYER_LEN}):\n')
#
#     if player.lower() == 'f':
#         if len(players) < PLAYER_LEN:
#             print('Erro! Para continuar deve haver no mínimo 2 jogadores!')
#             continue
#
#         break
#
#     players.append([player, 400, 0])

print('Tudo pronto, vamos começar!')
# pgControl = GameScreen(PLAYER_LEN)
# pgControl.run(players)
