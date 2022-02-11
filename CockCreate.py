from builtins import super

import pygame

from Button import Button
from Consts import *
from State import State
from TextInput import InputBox


class CockCreate(State):
    def __init__(self, game, player):
        super().__init__(game)
        self.game = game
        self.player = player
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.text_input = InputBox(WIDTH / 2, HEIGHT / 2, 400, 40)
        self.ok_btn = Button(self.game, WIDTH / 2 + 100, 450, "Valider")
        self.cancel_btn = Button(self.game, (WIDTH / 2) - 100, 450, "Annuler")

    def update(self, delta_time, actions):
        if actions["esc"] or self.cancel_btn.ispressed:
            self.exit_state()
        self.ok_btn.update(self.game.events)
        self.cancel_btn.update(self.game.events)
        self.text_input.handle_event(self.game.events)
        self.text_input.update()
        if self.text_input.issent or self.ok_btn.ispressed:
            self.player.buy_cock(self.player.cock_id, self.text_input.text)
            self.text_input.issent = False
            self.prev_state.need_refresh = True
            self.exit_state()
        self.game.reset_keys()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.blit(self.background_img, self.background_rect)
        self.text_input.draw(surface)
        self.ok_btn.render(surface)
        self.cancel_btn.render(surface)
        self.game.draw_text(surface, "Nom :", 50, WIDTH / 2, 300)
        self.game.draw_text(surface, "12 caracteres maximum", 20, WIDTH / 2, 350)
