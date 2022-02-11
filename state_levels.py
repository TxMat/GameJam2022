import pygame.image

import Level
from Button import Button
from Consts import *
from State import State


class StateLevel(State):
    def __init__(self, game, exp_chosen):
        super().__init__(game)
        self.debug_grid = pygame.image.load("Assets/debug_grid.png")
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.btn_dict = {}
        self.levels = Level.gen_level()
        self.choice = None
        self.strat = 0
        self.exp_chosen = exp_chosen
        counter = 0
        x = 300
        y = 150
        for level in self.levels:
            counter += 1
            self.btn_dict[level] = Button(self.game, x, y + counter * 100, level)

    def update(self, delta_time, actions):
        if actions["esc"]:
            self.exit_state()
        for key in self.btn_dict:
            self.btn_dict[key].update(self.game.events)
            if self.btn_dict[key].ispressed:
                self.choice = self.levels[key]
            # Il faut renvoyer un truc pour que la méthode où la StateLevel est créée dans farm s'occupe ensuite de créer une StateExpedition (après être passée à la nuit et avoir fait l'anim)
            # Dans la StateExpedition, on affiche et fait se dérouler pas à pas l'expédition, puis on finit par
            # renvoyer un récapitulatif, à partir duquel on change l'inventaire du joueur. Aussi, on affiche la vue du récap
            # ERRATUM : en fait non lol, mais c'est laid, mon dieu c'est laid. J'ai envie de vomir.
        if (self.choice):
            self.exp_chosen.append(self.choice)
            self.exp_chosen.append(self.strat)
            self.prev_state.wantNight = True
            self.exit_state()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.fill((70, 70, 70, 100), None, pygame.BLEND_RGBA_MULT)
        surface.blit(self.background_img, self.background_rect)
        for btn in self.btn_dict.values():
            btn.render(surface)
