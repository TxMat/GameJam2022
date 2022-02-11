from builtins import super

import pygame.image

import Utils
from Button import Button
from CockCreate import CockCreate
from CockView import CockView
from Consts import *
from State import State


class CockList(State):
    def __init__(self, game, player):
        super().__init__(game)
        self.need_refresh = False
        self.player = player
        self.debug_grid = pygame.image.load("Assets/debug_grid.png")
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.btn_array = []
        self.create_btns()
        self.buy_btn = Button(self.game, WIDTH / 2, 670, "Acheter")
        self.close_btn = Button(self.game, 910, 90, "X")

    def update(self, delta_time, actions):
        self.close_btn.update(self.game.events)
        if self.need_refresh:
            self.create_btns()
            self.need_refresh = False
        if actions["esc"] or self.close_btn.ispressed:
            self.exit_state()
        if self.buy_btn.ispressed:
            new_state = CockCreate(self.game, self.player)
            new_state.enter_state()
        for btn in self.btn_array:
            if btn.ispressed:
                new_state = CockView(self.game, self.player.cocks[btn.cock_id], self.player)
                new_state.enter_state()
        self.update_btns()
        self.game.reset_keys()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.fill((70, 70, 70, 100), None, pygame.BLEND_RGBA_MULT)
        surface.blit(self.background_img, self.background_rect)
        self.draw_menu(surface)
        self.render_btns(surface)
        self.close_btn.render(surface)
        # surface.blit(self.debug_grid, (0, 0))

    def draw_menu(self, surface):
        if len(self.player.cocks) == MAX_COCKS:
            self.buy_btn.color = (159, 128, 67)
            self.buy_btn.ishoverable = False
            self.buy_btn.refresh()
        self.draw_text(surface)
        Utils.draw_line(surface, (WIDTH / 2, 200), (WIDTH / 2, 600), 2)
        Utils.draw_line(surface, (100, 150), (920, 150), 2)
        self.buy_btn.render(surface)

    def create_btns(self):
        self.btn_array = []
        x = 300
        y = 200
        count = 0
        for cock in self.player.cocks.values():
            self.btn_array.append(Button(self.game, x, y, cock.name))
            self.btn_array[count].cock_id = cock.id
            count += 1
            if count == 5:
                x += 420
                y = 200
            else:
                y += 100

    def render_btns(self, surface):
        for button in self.btn_array:
            button.render(surface)

    def update_btns(self):
        self.buy_btn.update(self.game.events)
        for button in self.btn_array:
            button.update(self.game.events)

    def draw_text(self, surface):
        cost = 0
        if 1 <= len(self.player.cocks) <= MAX_COCKS - 1:
            cost = 50
        elif len(self.player.cocks) == MAX_COCKS:
            cost = "---"
        self.game.draw_text(surface, "Liste Des Coqs", 100, WIDTH / 2, 110)
        self.game.draw_text(surface, "Cout : " + str(cost) + " $", 25, WIDTH / 2, 695)
