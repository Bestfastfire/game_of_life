class InputText:
    def __init__(self, pg, font, color_active, color_inactive, x, y, w, h, label, player, text=''):
        self.color_inactive = color_inactive
        self.color_active = color_active
        self.player = player
        self.label = label
        self.font = font
        self.pg = pg

        self.rect = self.pg.Rect(x, y, w, h)
        self.color = self.color_inactive
        self.text = text
        self.txt_surface = self.font \
            .render(self.label + ': ' + self.text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == self.pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active

            else:
                self.active = False

            self.color = self.color_active if self.active else self.color_inactive

        if event.type == self.pg.KEYDOWN:
            if self.active:
                if event.key == self.pg.K_RETURN:
                    print(self.text)
                    self.text = ''

                elif event.key == self.pg.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    text_s = self.font.render(self.label + ': ' +
                                              self.text + event.unicode, True, self.color)

                    if (text_s.get_width()) < 400:
                        self.text += event.unicode

                self.txt_surface = self.font.render(
                    self.label + ': ' + self.text, True, self.color)

                self.player[0] = self.text

    def update(self):
        width = 400
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        self.pg.draw.rect(screen, self.color, self.rect, 2)
