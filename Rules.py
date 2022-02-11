import pygame.image

from Consts import *
from State import State


class Rules(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.img = pygame.image.load("Assets/regles.png")
        self.bg_rect = self.img.get_rect()
        self.bg_rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self, dt, actions):
        if actions["ok"] or actions["esc"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.img, self.bg_rect)
