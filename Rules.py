import pygame.image

from Consts import *
from State import State


class Rules(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.img = pygame.image.load("Assets/panneaucredits.png")
        self.bg_rect = self.img.get_rect()
        self.bg_rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self, dt, actions):
        if actions["ok"] or actions["esc"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.img, self.bg_rect)
        self.game.draw_text(display, "Fait Par: Elsa BERNET, Quentin CARREL, Mathieu PONAL, Emmanuel ARNOUX-BONKOWSKI",
                            20, 500, 100)
        self.game.draw_text(display,
                            "Musique: Game-of-role - opening s5, T.E.S.5 - around the fire, the witcher3 - the nightingales",
                            20, 500, 120)
        self.game.draw_text(display, "Sprite: Nolla games - noita ", 20, 500, 140)
