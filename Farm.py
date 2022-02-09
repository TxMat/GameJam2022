import pygame

from Button import Button
from Player import Player
from State import State
from Utils import *


class Farm(State):
    def __init__(self, game, player):
        State.__init__(self, game)
        self.player = player
        self.isNight = False
        self.HUD = HUD(self.game, self.player)
        self.background_img = pygame.image.load("Assets/backgound_day.png").convert()
        self.sun = Sun(self.game)

    def update(self, delta_time, actions):
        self.sun.update(delta_time)
        self.HUD.update()

    def render(self, surface):
        surface.blit(self.background_img, (0, 0))
        self.sun.render(surface)
        self.HUD.render(surface)


class Sun:
    def __init__(self, game):
        self.game = game
        self.curr_frame, self.last_frame_update = 0, 0
        self.frame_list = frames_from_spritesheet("Assets/sun.png", 0, 0, 94, 94, 2)
        self.frame_to_show = scale(self.frame_list[0], 0.9)

    def update(self, delta_time):
        self.animate(delta_time)

    def render(self, surface):
        surface.blit(self.frame_to_show, (900, 30))

    def animate(self, delta_time):
        self.last_frame_update += delta_time
        if self.last_frame_update > 1:
            self.curr_frame = (self.curr_frame + 1) % len(self.frame_list)
            self.frame_to_show = self.frame_list[self.curr_frame]
            self.frame_to_show = scale(self.frame_to_show, 0.9)
            self.last_frame_update = 0


class HUD:
    def __init__(self, game, player):
        self.player = player
        self.game = game
        self.background_img = pygame.image.load("Assets/hud_lol.png")
        self.inv = Button(game, 260, 90, "Inventaire", 30)
        self.last_exp = Button(game, 475, 90, "Derniere expedition", 30)
        self.cocks = Button(game, 730, 90, "Liste des poulets", 30)
        self.menu_rect = self.background_img.get_rect()
        self.menu_rect.center = (self.game.WIDTH / 2, 60)

    def draw_plyr_name(self):
        pass

    def draw_day(self, surface):
        self.game.draw_text(surface, "Jour :", 30, 470, 35)
        self.game.draw_text(surface, str(self.player.day), 30, 520, 35)

    def draw_money(self, surface):
        self.game.draw_text(surface, "Argent :", 30, 260, 35)
        self.game.draw_text(surface, str(self.player.money), 30, 340, 35)

    def draw_cock_number(self, surface):
        self.game.draw_text(surface, "Nombre de Coqs :", 30, 700, 35)
        if len(self.player.cocks) < 20:
            self.game.draw_text(surface, str(len(self.player.cocks)), 30, 820, 35)
        else:
            self.game.draw_text(surface, "MAX", 30, 820, 35)

    def update(self):
        self.inv.update(self.game.events)
        self.last_exp.update(self.game.events)
        self.cocks.update(self.game.events)

    def render(self, surface):
        surface.blit(self.background_img, self.menu_rect)
        self.inv.render(surface)
        self.last_exp.render(surface)
        self.cocks.render(surface)
        self.draw_day(surface)
        self.draw_money(surface)
        self.draw_cock_number(surface)
