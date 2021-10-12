import random

N = 10
B = 3
R = 3
J = 1
P = 4

user_index = 0
bonus = [("Ganhou R$ 400,00", 400),
        ("Ganhou R$ 750,00", 750),
        ("Ganhou R$ 600,00", 600),
        ("Perdeu R$ 300,00.", -300),
        ("Perdeu R$ 500,00.", -500),
        ("Perdeu R$ 750.", -750)]


def put_users():
    users = []
    while len(users) < 2:
        nome = input("Digite seu nome:\n")
        users.append([nome, 500, 0])

    return users


def choice_user(users):
    return random.choice(users)


def rotate_roul():
    return random.randint(0, P-1)


def roleta(n):
    fim = 0
    for fim in range (0, n):
        valor = random.randint(-7, 7)
        fim = fim + valor
    return fim


def generate_positions(road):
    cont = 0
    while cont < B:
        position = random.randint(0, N-1)
        if road[position] == ' ':
            road[position] = "B"
            cont += 1

    cont = 0
    while cont < R:
        position = random.randint(0, N-1)
        if road[position] == ' ':
            road[position] = "R"
            cont += 1

    return road


def generate_road():
    return generate_positions([" "]*N)


def get_last_user(users):
    last = users[0]

    for item in users:
        if item[2] > last[2]:
            last = item

    return last


def get_winner_user(users):
    last = users[0]

    for item in users:
        if item[1] > last[1]:
            last = item

    return last


road = generate_road()
print(f'Caminho: {road}')
users = put_users()

while get_last_user(users)[2] < N-1:
    # print('Sorteando jogandor...')
    user = users[user_index]
    user_index += 1

    if user_index == 5:
        user_index = 0

    print(f'Vez do jogador {user[0]}')

    while input("Digite 'r' para girar roleta:\n").lower() != 'r':
        continue

    roul = rotate_roul()

    print(f'Pulou {roul} casa(s)')
    index = user[2] + roul

    if index >= len(road):
        index = len(road)-1

    user[2] = index

    if road[index] == 'R' or road[index] == 'B':
        rb = bonus[random.randint(3, 5) if road[index] == 'R' else random.randint(0, 2)]
        user[1] += rb[1]
        print(f'{rb[0]}')

    print(f'Lista atual: {users}\n\n')

print(f'O jogador {get_winner_user(users)[0]} ganhou!')
print(f'Lista de jogadores final: {users}')
