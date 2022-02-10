import pygame.image
import Utils
from Consts import *
from Button import Button
from State import State

class Feeding(State):
    def __init__(self, game = None, cock = None, player = None):
        super().__init__(game)
        self.game = game
        self.cock = cock
        self.player = player
        self.close_btn = Button(self.game, 910, 90, "X")
        self.debug_grid = pygame.image.load("Assets/alpha_grid.png")
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        
    def update(self, delta_time, actions):
        self.close_btn.update(self.game.events)
        if actions["esc"] or self.close_btn.ispressed:
            self.exit_state()
        self.game.reset_keys()
        
    def render(self, surface):
        counter = 0
        surface.blit(self.background_img, self.background_rect)
        self.game.draw_text(surface, "Grains :", 40, 150, 200+50*counter, align="left")
        counter += 1
        for grain in self.player.inv_grain:
            self.game.draw_text(surface, grain + " : " + str(self.player.inv_grain[grain]), 30, 250, 200+50*counter, align="left")
            counter += 1
        self.close_btn.render(surface)
        
