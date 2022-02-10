import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text="placeholder", size=50, color=(134, 62, 29)):
        super().__init__()
        self.hoover_btn = None
        self.base_btn = None
        self.text_rect = None
        self.game = game
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.size = size
        self.refresh()
        self.btn = self.base_btn
        self.ispressed = False
        self.ishoverable = True

    def update(self, events):
        hover = self.text_rect.collidepoint(pygame.mouse.get_pos())
        self.btn = self.base_btn
        self.ispressed = False
        if hover and self.ishoverable:
            self.btn = self.hoover_btn
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and hover:
                self.ispressed = True

    def render(self, surface):
        surface.blit(self.btn, self.text_rect)

    def refresh(self):
        font = pygame.font.Font(self.game.font_loc, self.size)
        text_surface = font.render(self.text, True, self.color)
        self.text_rect = text_surface.get_rect()
        self.text_rect.center = (self.x, self.y)
        self.base_btn = text_surface
        text_surface = font.render(self.text, True, (189, 77, 28))
        self.hoover_btn = text_surface
