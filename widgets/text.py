class Text:
    def __init__(self, pg, pos, font, text):
        self.font = pg.font.SysFont("Arial", font)
        self.pg = pg

        self.text = self.font.render(text, 1, self.pg.Color("White"))
        self.x, self.y = pos

        self.size = self.text.get_size()
        self.rect = self.pg.Rect(self.x, self.y, self.size[0], self.size[1])
        self.surface = self.pg.Surface(self.size)
        self.change_text(text)

    def change_text(self, text):
        self.text = self.font.render(text, 1, self.pg.Color("White"))
        self.surface.blit(self.text, (0, 0))

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
