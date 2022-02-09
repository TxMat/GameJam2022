import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text="placeholder", size=50, color=(200, 200, 200)):
        super().__init__()
        self.game = game
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        font = pygame.font.Font(self.game.font_loc, size)
        text_surface = font.render(text, True, color)
        self.text_rect = text_surface.get_rect()
        self.text_rect.center = (x, y)
        self.base_btn = text_surface
        text_surface = font.render(text, True, (200, 30, 30))
        self.hoover_btn = text_surface
        self.btn = self.base_btn

    def update(self, events):
        hover = self.text_rect.collidepoint(pygame.mouse.get_pos())
        self.btn = self.base_btn
        if hover:
            self.btn = self.hoover_btn
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("clicked")


    def render(self, surface):
        surface.blit(self.btn, self.text_rect)
