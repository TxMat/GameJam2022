import pygame.image

from Button import Button
from Consts import *
from State import State


class Rules(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.img = pygame.image.load("Assets/regles.png")
        self.bg_rect = self.img.get_rect()
        self.bg_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.close_btn = Button(self.game, 910, 60, "X")

    def update(self, dt, actions):
        self.close_btn.update(self.game.events)
        if actions["ok"] or actions["esc"] or self.close_btn.ispressed:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.img, self.bg_rect)
        self.close_btn.render(display)
