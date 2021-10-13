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
        self.walk_list = []

        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (int(50*.7), int(50)))
        self._set_position(self.current_position)

    def _set_position(self, position):
        self.current_position = position
        y = -20
        x = 25

        if self.current_player == 1:
            x += 40

        elif self.current_player == 2:
            y += 40

        elif self.current_player == 3:
            y += 40
            x += 40

        self.rect = self.image.get_rect()
        self.rect.topleft = int(self.current_position[0] + x),  \
                            int(self.current_position[1] + y)

    def move_to(self, index):
        self.walk_list = []

        # print(f'{self.position_index} | {index}')

        if self.position_index + index <= 0:
            index = 0

        # print(f'{self.position_index} | {index}')

        if self.position_index < index:
            for i in range(self.position_index, index+1):
                self.walk_list.append(self.controller.positions[i])

        else:
            for i in range(self.position_index, index-1, -1):
                self.walk_list.append(self.controller.positions[i])

        if len(self.walk_list) > 0:
            print('walking...')
            self.new_position = self.walk_list[0]
            self.position_index = index
            self.walking = True

            if self.position_index == self.controller.road_len-1:
                print('Fim de jogo!')

        # while position[0] != self.current_position[0]:
        #     self._set_position([self.current_position[0]+1, self.current_position[1]])
        #
        # self.walking = False

    def update(self):
        speed = 10

        if self.walking:
            # print(f'{self.new_position} | {self.current_position}')
            # for right
            if int(self.new_position[0]) > int(self.current_position[0]):
                if (self.current_position[0]+speed) > self.new_position[0]:
                    speed = self.new_position[0] - self.current_position[0]

                self._set_position([self.current_position[0]+speed, self.current_position[1]])

            # for left
            elif int(self.new_position[0]) < int(self.current_position[0]):
                if (self.current_position[0]-speed) < self.new_position[0]:
                    speed = self.current_position[0] - self.new_position[0]

                self._set_position([self.current_position[0]-speed, self.current_position[1]])

            # for down
            elif int(self.new_position[1]) > int(self.current_position[1]):
                if (self.current_position[1]+speed) > self.new_position[1]:
                    speed = self.new_position[1] - self.current_position[1]

                self._set_position([self.current_position[0], self.current_position[1] + speed])

            # for up
            elif int(self.new_position[1]) < int(self.current_position[1]):
                if (self.current_position[1]-speed) < self.new_position[1]:
                    speed = self.current_position[1] - self.new_position[1]

                self._set_position([self.current_position[0], self.current_position[1] - speed])

            else:
                if len(self.walk_list) > 1:
                    self.walk_list.pop(0)
                    self.new_position = self.walk_list[0]

                else:
                    self.walk_list = []
                    self.walking = False

            self.current_sprite += 1/5
            # print(f'current sprite: {self.current_sprite}')
            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (int(50*.7), int(50)))

            if self.current_sprite > 2:
                self.current_sprite = -1
