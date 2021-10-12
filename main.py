# pip install pygame
import sys
from controller.pygame_control import PGController
sys.setrecursionlimit(1000000)

players = []
print(f'Olá, seja bem vindo ao jogo da vida!\nPara começar:')
while len(players) < 2:
    player = input(f'Digite o nome do jogador {len(players)+1} (máximo 4) ou f para continuar:\n')

    if player.lower() == 'f':
        if len(players) < 2:
            print('Erro! Para continuar deve haver no mínimo 2 jogadores!')
            continue

        break

    players.append([player, 400, 0])

print('Tudo pronto, vamos começar!')
pgControl = PGController()
pgControl.run(players)
