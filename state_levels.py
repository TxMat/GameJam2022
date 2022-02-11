import pygame.image

import Level
import Utils
from Button import Button
from Consts import *
from State import State


class StateLevel(State):
    def __init__(self, game, cocknb, exp_chosen):
        super().__init__(game)
        self.cocknb = cocknb
        self.debug_grid = pygame.image.load("Assets/debug_grid.png")
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.btn_dict = {}
        self.levels = Level.gen_level()
        self.descs = []
        self.choice = None
        self.strat = 0
        self.exp_chosen = exp_chosen
        self.close_btn = Button(self.game, 910, 90, "X")
        self.grid = -1
        counter = 0
        x = WIDTH / 2
        y = 200
        for level in self.levels:
            self.descs.append(self.levels[level].desc)
            self.btn_dict[level] = Button(self.game, x, y + counter * 100, level)
            counter += 1

    def update(self, delta_time, actions):
        self.close_btn.update(self.game.events)
        if actions["esc"] or self.close_btn.ispressed:
            self.exit_state()
        if self.cocknb > 0:
            for key in self.btn_dict:
                self.btn_dict[key].update(self.game.events)
                if self.btn_dict[key].ispressed:
                    self.choice = self.levels[key]

            if (self.choice):
                self.exp_chosen.append(self.choice)
                self.exp_chosen.append(self.strat)
                self.prev_state.wantNight = True
                self.exit_state()
        if actions["right"]:
            self.grid *= -1
        self.game.reset_keys()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.fill((70, 70, 70, 100), None, pygame.BLEND_RGBA_MULT)
        surface.blit(self.background_img, self.background_rect)
        Utils.draw_line(surface, (200, 155), (830, 155), 2)
        self.game.draw_text(surface, "Inventaire", 100, WIDTH / 2, 110)
        if self.cocknb <= 0:
            self.game.draw_text(surface, "Vous n'avez aucun coq !", 50, WIDTH / 2, HEIGHT / 2 - 40)
            self.game.draw_text(surface, "Ajoutez-en dans 'Liste des coqs' avant d'aller miner", 30, WIDTH / 2,
                                HEIGHT / 2 + 40)
        else:
            counter = 0
            x = WIDTH / 2
            for btn in self.btn_dict.values():
                btn.render(surface)
                self.game.draw_text(surface, self.descs[counter], 30, x, 230 + counter * 100)
                counter += 1
        if self.grid > 0:
            surface.blit(self.debug_grid, (0, 0))
        self.close_btn.render(surface)
