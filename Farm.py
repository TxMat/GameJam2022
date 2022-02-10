import pygame

from Consts import *
from Button import Button
from CockList import CockList
from CockView import CockView
from state_last_exp import LastExp
from state_levels import StateLevel
from state_Expedition import ExpState
from state_Inventory import Inventory
from State import State
from Utils import *


class Farm(State):
    def __init__(self, game, player):
        State.__init__(self, game)
        self.wantDay = False
        self.player = player
        self.isNight = False
        self.wantNight = False
        self.HUD = HUD(self.game, self.player)
        self.debug_grid = pygame.image.load("Assets/debug_grid.png")
        self.night_transition_background = pygame.image.load("Assets/transition.png")
        self.background_img_night = pygame.image.load("Assets/backgound_night.png")
        self.background_img_day = pygame.image.load("Assets/backgound_day.png").convert()
        self.background_img = self.background_img_day
        self.sun = Sun(self.game)
        self.mosanto_collide = pygame.rect.Rect((0, 150), (160, 270))
        self.cave_collide = pygame.rect.Rect((700, 220), (280, 200))
        self.exp_chosen = []
        self.chosen_cocks = []
        self.pos_trans_x = WIDTH

    def update(self, delta_time, actions):
        events = self.game.events
        self.sun.update(delta_time)
        self.HUD.update()
        for cock in self.player.cocks.values():
            cock.update(delta_time, self.game.events)
            if cock.ispressed:
                new_state = CockView(self.game, cock, self.player)
                new_state.enter_state()
        if self.HUD.cocks.ispressed:
            self.player.money *= 2
            new_state = CockList(self.game, self.player)
            new_state.enter_state()
        if self.HUD.last_exp.ispressed:
            new_state = LastExp(self.game, self.player)
            new_state.enter_state()
        if self.HUD.inv.ispressed:
            new_state = Inventory(self.game,self.player)
            new_state.enter_state()
        mosanto_hover = self.mosanto_collide.collidepoint(pygame.mouse.get_pos())
        cave_hover = self.cave_collide.collidepoint(pygame.mouse.get_pos())
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and mosanto_hover:
                print("mosanto")
            if event.type == pygame.MOUSEBUTTONDOWN and cave_hover:
                new_state = StateLevel(self.game, self.exp_chosen)
                new_state.enter_state()
                print("cave")
        if(self.exp_chosen):


            # DEBUG
            self.chosen_cocks = self.player.cocks
            # DEBUG
            if not self.wantNight:
                new_state = ExpState(self.game, self.exp_chosen[0], self.exp_chosen[1], self.chosen_cocks, self.player.last_exp)
                new_state.enter_state()
                self.exp_chosen.clear()


    def render(self, surface):
        surface.blit(self.background_img, (0, 0))
        if not self.isNight:
            self.sun.render(surface)
        self.HUD.render(surface)
        for cock in self.player.cocks.values():
            cock.render(surface)
        # surface.blit(self.debug_grid, (0, 0))
        self.lanui(surface)

    def lanui(self, surface):
        if self.wantNight or self.wantDay:
            surface.blit(self.night_transition_background, (self.pos_trans_x, 0))
            self.pos_trans_x -= 30
        if self.wantNight:
            if self.pos_trans_x <= 0 and not self.isNight:
                self.background_img = self.background_img_night
                self.isNight = True
            if self.pos_trans_x <= -WIDTH*2:
                self.wantNight = False
                self.pos_trans_x = WIDTH
        elif self.wantDay:
            if self.pos_trans_x <= 0 and self.isNight:
                self.background_img = self.background_img_day
                self.isNight = False
            if self.pos_trans_x <= -WIDTH*2:
                self.wantDay = False
                self.pos_trans_x = WIDTH




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
        self.cocks = Button(game, 710, 90, "Liste des coqs", 30)
        self.menu_rect = self.background_img.get_rect()
        self.menu_rect.center = (self.game.WIDTH / 2, 60)

    def draw_plyr_name(self):
        pass

    def draw_day(self, surface):
        self.game.draw_text(surface, "Jour :", 30, 480, 35)
        self.game.draw_text(surface, str(self.player.day), 30, 480, 60)

    def draw_money(self, surface):
        self.game.draw_text(surface, "Argent :", 30, 280, 35)
        self.game.draw_text(surface, str(self.player.money), 30, 280, 60)

    def draw_cock_number(self, surface):
        self.game.draw_text(surface, "Nombre de Coqs :", 30, 700, 35)
        self.game.draw_text(surface, str(len(self.player.cocks)) + "/10", 30, 700, 60)

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
