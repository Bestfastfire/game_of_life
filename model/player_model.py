import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, controller, name, money, player=0):
        pygame.sprite.Sprite.__init__(self)
        self.money = money
        self.name = name

        print(f'p: {player}')
        self.sprites = [
            pygame.image.load(f'./src/sprites/player/p{player}_stopped.png'),
            pygame.image.load(f'./src/sprites/player/p{player}_walking.png'),
            pygame.image.load(f'./src/sprites/player/p{player}_walking.png')
        ]

        self.current_position = controller.positions[0]
        self.new_position = self.current_position
        self.controller = controller
        self.current_player = player
        self.position_index = 0
        self.current_sprite = 0
        self.walking = False

        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (int(50*.7), int(50)))
        self._set_position(self.current_position)

    def _set_position(self, position):
        self.current_position = position
        y = -40 + self.current_player * 25
        x = 40

        self.rect = self.image.get_rect()
        self.rect.topleft = int(self.current_position[0] + x),  int(self.current_position[1] + y)

    def move_to(self, index):
        self.new_position = self.controller.positions[index]
        self.position_index = index
        self.walking = True

        # while position[0] != self.current_position[0]:
        #     self._set_position([self.current_position[0]+1, self.current_position[1]])
        #
        # self.walking = False

    def update(self):
        if self.walking:
            # print(f'{self.new_position} | {self.current_position}')
            # for right
            if int(self.new_position[0]) > int(self.current_position[0]):
                self._set_position([self.current_position[0]+1, self.current_position[1]])

            # for left
            elif int(self.new_position[0]) < int(self.current_position[0]):
                self._set_position([self.current_position[0]-1, self.current_position[1]])

            # for down
            elif int(self.new_position[1]) > int(self.current_position[1]):
                self._set_position([self.current_position[0], self.current_position[1] + 1])

            # for up
            elif int(self.new_position[1]) < int(self.current_position[1]):
                self._set_position([self.current_position[0], self.current_position[1] - 1])

            else:
                self.walking = False

            self.current_sprite += 1/5
            # print(f'current sprite: {self.current_sprite}')
            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (int(50*.7), int(50)))

            if self.current_sprite > 2:
                self.current_sprite = -1
