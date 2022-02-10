import Utils
import pygame.image
from Button import Button
from State import State
from Consts import *

class Inventory(State):
    def __init__(self, game, player):
        super().__init__(game)
        self.player = player
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect =  self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.close_btn = Button(self.game, 910, 90, "X")

    def update(self, delta_time, actions):
        self.close_btn.update(self.game.events)
        if actions["esc"] or self.close_btn.ispressed:
            self.exit_state()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.fill((70, 70, 70, 100), None, pygame.BLEND_RGBA_MULT)
        surface.blit(self.background_img, self.background_rect)
        counter = 0
        self.game.draw_text(surface, "Minerais :", 40, 150, 200+50*counter, align="left")
        counter += 1
        for ore in self.player.inv_ore:
            self.game.draw_text(surface, ore + " : " + str(self.player.inv_ore[ore]), 30, 250, 200+50*counter, align="left")
            counter += 1
        self.game.draw_text(surface, "ADN :", 40, 150, 200+50*counter, align="left")
        counter += 1
        for dna in self.player.inv_dna:
            self.game.draw_text(surface, dna + " : " + str(self.player.inv_dna[dna]), 30, 250, 200+50*counter, align="left")
            counter += 1
        self.game.draw_text(surface, "Grains :", 40, 150, 200+50*counter, align="left")
        counter += 1
        for grain in self.player.inv_grain:
            self.game.draw_text(surface, grain + " : " + str(self.player.inv_grain[grain]), 30, 250, 200+50*counter, align="left")
            counter += 1
        self.close_btn.render(surface)

