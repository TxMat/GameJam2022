import pygame.image

from State import State


class CockList(State):
    def __init__(self, game, player):
        super().__init__(game)
        self.player = player
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (self.game.WIDTH/2, self.game.HEIGHT/2)

    def update(self, delta_time, actions):
        if actions["esc"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.fill((100, 100, 100, 100), None, pygame.BLEND_RGBA_MULT)
        surface.blit(self.background_img, self.background_rect)
