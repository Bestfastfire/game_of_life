# pip install pygame
import sys
from controller.pygame_control import PGController

import sys
sys.setrecursionlimit(1000000)

PLAYER_LEN = 4

players = []
print(f'Olá, seja bem vindo ao jogo da vida!\nPara começar:')
while len(players) < PLAYER_LEN:
    player = input(f'Digite o nome do jogador {len(players)+1} (máximo {PLAYER_LEN}):\n')

    if player.lower() == 'f':
        if len(players) < PLAYER_LEN:
            print('Erro! Para continuar deve haver no mínimo 2 jogadores!')
            continue

        break

    players.append([player, 400, 0])

print('Tudo pronto, vamos começar!')
pgControl = PGController(PLAYER_LEN)
pgControl.run(players)
