import pygame.image

from Button import Button
from Consts import *
from State import State


class Feeding(State):
    def __init__(self, game, cock, player):
        super().__init__(game)
        self.need_refresh = False
        self.game = game
        self.cock = cock
        self.player = player
        self.close_btn = Button(self.game, 910, 90, "X")
        self.debug_grid = pygame.image.load("Assets/alpha_grid.png")
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.btn_array = []
        self.grid = -1

    def update(self, delta_time, actions):
        self.close_btn.update(self.game.events)
        if self.need_refresh:
            self.init_btn()
            self.need_refresh = False
        if actions["esc"] or self.close_btn.ispressed:
            self.exit_state()
        if actions["right"] or actions["ok"]:  # DEBUG
            self.grid *= -1
        self.update_btns()
        self.game.reset_keys()

    def render(self, surface):
        counter = 0
        surface.blit(self.background_img, self.background_rect)
        self.game.draw_text(surface, "Grains :", 40, 150, 200 + 50 * counter, align="left")
        counter += 1
        for grain in self.player.inv_grain:
            self.game.draw_text(surface, grain + " : " + str(self.player.inv_grain[grain]), 30, 250, 200 + 50 * counter,
                                align="left")
            counter += 1
        self.close_btn.render(surface)
        self.render_btns(surface)
        if self.grid > 0:
            surface.blit(self.debug_grid, (0, 0))

    def init_btn(self):
        self.btn_array = []
        x = 100
        y = 180
        count = 0
        for grain in self.player.inv_grain:
            val = self.player.inv_grain[grain]
            self.btn_array.append(Button(self.game, x + 85, y, str(grain), 35))
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
