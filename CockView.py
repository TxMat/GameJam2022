import random
from builtins import super

import pygame

import Utils
from Button import Button
from Cock import Cock
from Consts import *
from State import State


class CockView(State):
    def __init__(self, game, cock):
        super().__init__(game)
        self.game = game
        self.cock = cock
        self.debug_grid = pygame.image.load("Assets/debug_grid.png")
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.dummy_cock = Cock(None, -1, "dummy", 3)
        self.dummy_cock.curr_x = 80
        self.dummy_cock.curr_y = 50
        self.dummy_cock.display_health_bar = False
        self.dummy_cock.anim_mode = random.randint(0, 2)

    def update(self, delta_time, actions):
        self.dummy_cock.update(delta_time, self.game.events)
        if actions["esc"]:
            self.prev_state.need_refresh = True
            self.exit_state()
        self.game.reset_keys()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.blit(self.background_img, self.background_rect)
        self.dummy_cock.render(surface)
        self.draw_text(surface)
        self.draw_lines(surface)

    def draw_lines(self, surface):
        Utils.draw_line(surface, (WIDTH / 2, 200), (WIDTH / 2, 600), 2)
        Utils.draw_line(surface, (100, 170), (920, 170), 2)

    def draw_text(self, surface):
        self.game.draw_text(surface, self.cock.name, 100, WIDTH / 2, 120)
        self.game.draw_text(surface, "", 25, WIDTH / 2, 695)
