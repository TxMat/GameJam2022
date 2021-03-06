from builtins import super

import pygame.image

import Utils
from Button import Button
from Consts import *
from Grain import gen_grain
from State import State


class Monsanto(State):
    def __init__(self, game, player):
        super().__init__(game)
        self.player = player
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.btn_array = []
        self.init_btn()
        self.close_btn = Button(self.game, 910, 90, "X")

    def update(self, delta_time, actions):
        self.close_btn.update(self.game.events)
        if actions["esc"] or self.close_btn.ispressed:
            self.exit_state()
        for btn in self.btn_array:
            if btn.ispressed:
                grains = gen_grain()
                if self.player.money >= grains[btn.grain_name].price:
                    if btn.grain_name not in self.player.inv_grain:
                        self.player.inv_grain[btn.grain_name] = 0
                    self.player.inv_grain[btn.grain_name] += 1
                    self.player.money -= grains[btn.grain_name].price
        self.update_btns()
        self.game.reset_keys()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.fill((70, 70, 70, 100), None, pygame.BLEND_RGBA_MULT)
        surface.blit(self.background_img, self.background_rect)
        self.draw_menu(surface)
        self.render_cases(surface)
        self.render_btns(surface)
        self.close_btn.render(surface)

    def draw_menu(self, surface):
        self.draw_text(surface)
        Utils.draw_line(surface, (295, 160), (295, 700), 1)
        Utils.draw_line(surface, (WIDTH / 2, 160), (WIDTH / 2, 700), 1)
        Utils.draw_line(surface, (725, 160), (725, 700), 1)
        Utils.draw_line(surface, (100, 150), (920, 150), 2)

    def render_cases(self, display):
        # key = name, val = obj
        # grain.rch
        # player.inv.idx name += grain
        x = 100
        y = 180
        count = 0
        for i in self.game.grains:
            grain = self.game.grains[i]
            self.game.draw_text(display, "Nom : " + str(i), 30, x, y, align="left")
            y += 20
            self.game.draw_text(display, "Recherche : " + str(grain.res_cost), 25, x, y, align="left")
            y += 20
            self.game.draw_text(display, "Cout : " + str(grain.price) + " $", 30, x, y, align="left")
            y += 20
            grain_nb = 0
            if i in self.player.inv_grain:
                grain_nb = self.player.inv_grain[i]
            self.game.draw_text(display, "Possedes : " + str(grain_nb), 30, x, y, align="left")
            y += 30
            count += 1
            if not count % 4:
                x += 215
                y = 180
            else:
                y += 50

    def init_btn(self):
        self.btn_array = []
        # key = name, val = obj
        x = 100
        y = 180
        count = 0
        for grain in self.game.grains:
            y += 90
            self.btn_array.append(Button(self.game, x + 85, y, "Acheter", 35))
            self.btn_array[count].grain_name = grain
            count += 1
            if not count % 4:
                x += 215
                y = 180
            else:
                y += 50

    def render_btns(self, surface):
        for button in self.btn_array:
            button.render(surface)

    def update_btns(self):
        for button in self.btn_array:
            button.update(self.game.events)

    def draw_text(self, surface):
        self.game.draw_text(surface, "Moussanto", 100, WIDTH / 2, 110)
