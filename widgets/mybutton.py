class MyButton:
    def __init__(self, text, pos, pg, font, to_do):
        self.font = pg.font.SysFont("Arial", font)
        self.pg = pg

        self.text = self.font.render(text, 1, self.pg.Color("White"))
        self.x, self.y = pos
        self.to_do = to_do

        self.size = self.text.get_size()
        self.rect = self.pg.Rect(self.x, self.y, self.size[0], self.size[1])
        self.surface = self.pg.Surface(self.size)
        self.change_text(text, 'black')

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, 1, self.pg.Color("White"))

        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = self.pg.mouse.get_pos()

        if event.type == self.pg.MOUSEBUTTONDOWN:
            if self.pg.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.to_do()
