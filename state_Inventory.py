import pygame.image

import Utils
from Button import Button
from Consts import *
from State import State


class Inventory(State):
    def __init__(self, game, player):
        super().__init__(game)
        self.player = player
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.debug_grid = pygame.image.load("Assets/debug_grid.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.close_btn = Button(self.game, 910, 90, "X")
        self.sell_btn = Button(self.game, WIDTH / 2, 670, "Vendre vos minerais", 30)
        self.grid = -1

    def update(self, delta_time, actions):
        self.sell_btn.update(self.game.events)
        self.close_btn.update(self.game.events)
        if actions["esc"] or self.close_btn.ispressed:
            self.exit_state()
        if self.sell_btn.ispressed:
            print("sell")
            self.player.sell_all()
        if actions["right"] or actions["ok"]:  # DEBUG
            self.grid *= -1
        self.game.reset_keys()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.fill((70, 70, 70, 100), None, pygame.BLEND_RGBA_MULT)
        surface.blit(self.background_img, self.background_rect)
        self.draw_menu(surface)
        self.close_btn.render(surface)
        if self.grid > 0:
            surface.blit(self.debug_grid, (0, 0))

    def draw_menu(self, surface):
        self.sell_btn.render(surface)
        self.draw_text(surface)
        self.render_items(surface)
        Utils.draw_line(surface, (360, 160), (360, 700), 1)
        Utils.draw_line(surface, (660, 160), (660, 700), 1)
        Utils.draw_line(surface, (100, 150), (920, 150), 2)

    def draw_text(self, surface):
        self.game.draw_text(surface, "Inventaire", 100, WIDTH / 2, 110)
        self.game.draw_text(surface, "Grain :", 55, 218, 185, )
        self.game.draw_text(surface, "Minerais :", 55, 230 + 280, 185, )
        self.game.draw_text(surface, "ADNs :", 52, 218 + 290 + 280, 185, )

    def render_items(self, display):
        x = 130
        y = 240
        for i in self.player.inv_grain:
            val = self.player.inv_grain[i]
            self.game.draw_text(display, str(i) + " : " + str(val), 40, x, y, align="left")
            y += 30
        x += 280
        y = 250
        for i in self.player.inv_ore:
            val = self.player.inv_ore[i]
            self.game.draw_text(display, str(i) + " : " + str(val), 40, x, y, align="left")
            y += 30
        x += 290
        y = 250
        for i in self.player.inv_dna:
            val = self.player.inv_dna[i]
            self.game.draw_text(display, str(i) + " : " + str(val), 40, x, y, align="left")
            y += 30


"""

counter = 0
        self.game.draw_text(surface, "Minerais :", 40, 150, 200 + 50 * counter, align="left")
        counter += 1
        for ore in self.player.inv_ore:
            self.game.draw_text(surface, ore + " : " + str(self.player.inv_ore[ore]), 30, 250, 200 + 50 * counter,
                                align="left")
            counter += 1
        self.game.draw_text(surface, "ADN :", 40, 150, 200 + 50 * counter, align="left")
        counter += 1
        for dna in self.player.inv_dna:
            self.game.draw_text(surface, dna + " : " + str(self.player.inv_dna[dna]), 30, 250, 200 + 50 * counter,
                                align="left")
            counter += 1
        self.game.draw_text(surface, "Grains :", 40, 150, 200 + 50 * counter, align="left")
        counter += 1
        for grain in self.player.inv_grain:
            self.game.draw_text(surface, grain + " : " + str(self.player.inv_grain[grain]), 30, 250, 200 + 50 * counter,
                                align="left")
            counter += 1

"""
