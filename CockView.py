import random
from builtins import super

import pygame

import Utils
from Button import Button
from Cock import Cock
from Consts import *
from State import State
from state_Feeding import Feeding


class CockView(State):
    def __init__(self, game, cock, player = None):
        super().__init__(game)
        #print(player)
        self.game = game
        self.cock = cock
        self.player = player
        self.debug_grid = pygame.image.load("Assets/alpha_grid.png")
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.dummy_cock = Cock(None, -1, "dummy", 3)
        self.dummy_cock.curr_x = 80
        self.dummy_cock.curr_y = 50
        self.dummy_cock.display_health_bar = False
        self.dummy_cock.anim_mode = random.randint(0, 2)
        self.close_btn = Button(self.game, 910, 90, "X")
        self.feed_btn = Button(self.game, 512, 660, "Nourrir")
        self.grid = -1

    def update(self, delta_time, actions):
        self.close_btn.update(self.game.events)
        self.feed_btn.update(self.game.events)
        self.dummy_cock.update(delta_time, self.game.events)
        if actions["esc"] or self.close_btn.ispressed:
            self.prev_state.need_refresh = True
            self.exit_state()
        if self.feed_btn.ispressed:
            print("nourrir")
            new_state = Feeding(self.game, self.cock, self.player)
            new_state.enter_state()
        if actions["right"] or actions["ok"]: #DEBUG
            self.grid *= -1
        self.game.reset_keys()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.blit(self.background_img, self.background_rect)
        self.dummy_cock.render(surface)
        if self.grid > 0:
            surface.blit(self.debug_grid, (0, 0))
        self.draw_text(surface)
        self.draw_lines(surface)
        self.feed_btn.render(surface)
        self.close_btn.render(surface)

    def draw_lines(self, surface):
        Utils.draw_line(surface, (WIDTH / 2, 200), (WIDTH / 2, 600), 2)
        Utils.draw_line(surface, (100, 170), (920, 170), 2)

    def draw_text(self, surface):
        x = 150
        self.game.draw_text(surface, self.cock.name, 100, WIDTH / 2, 120)
        self.game.draw_text(surface, "Intelligence : " + str(self.cock.g_intel()), 40, x, 280, align="left")
        self.game.draw_text(surface, "Force : " + str(self.cock.g_strength()), 40, x, 320, align="left")
        self.game.draw_text(surface, "Endurance : " + str(self.cock.g_stamina()), 40, x, 360, align="left")
        self.game.draw_text(surface, "Satiete : " + str(self.cock.hunger) + " / " + str(self.cock.max_hunger), 40, x, 430, align="left")
        txt = "Enfant : Aucun"
        if self.cock.child:
            txt = str(self.cock.child)
        self.game.draw_text(surface, txt, 40, x, 500, align="left")
        txt = "Parent : Aucun"
        if self.cock.parent:
            txt = str(self.cock.parent)
        self.game.draw_text(surface, txt, 40, x, 540, align="left")
        txt = "Fertile : Non"
        if self.cock.fertile:
            txt = "Fertile : Oui"
        self.game.draw_text(surface, txt, 40, x, 580, align="left")



