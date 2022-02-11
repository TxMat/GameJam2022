from Button import Button
from CockList import CockList
from CockView import CockView
from Consts import *
from Monsanto import Monsanto
from State import State
from Sun import Sun
from Utils import *
from state_Expedition import ExpState
from state_Inventory import Inventory
from state_last_exp import LastExp
from state_levels import StateLevel


class Farm(State):
    def __init__(self, game, player):
        State.__init__(self, game)
        self.wantDay = False
        self.player = player
        self.isNight = False
        self.wantNight = False
        self.isMusicLoaded = False
        self.HUD = HUD(self.game, self.player)
        self.debug_grid = pygame.image.load("Assets/debug_grid.png")
        self.night_transition_background = pygame.image.load("Assets/transition.png")
        self.background_img_night = pygame.image.load("Assets/backgound_night.png")
        self.background_img_day = pygame.image.load("Assets/backgound_day.png").convert()
        self.background_img = self.background_img_day
        self.sun = Sun(self.game, (900, 30), 0.9)
        self.mosanto_collide = pygame.rect.Rect((0, 150), (160, 270))
        self.cave_collide = pygame.rect.Rect((700, 220), (280, 200))
        self.exp_chosen = []
        self.chosen_cocks = []
        self.pos_trans_x = WIDTH

    def update(self, delta_time, actions):
        if not self.isMusicLoaded:
            self.bgm()
            self.isMusicLoaded = True
        events = self.game.events
        self.sun.update(delta_time)
        self.HUD.update()
        for cock in self.player.cocks.values():
            cock.update(delta_time, self.game.events)
            if cock.ispressed:
                new_state = CockView(self.game, cock, self.player)
                new_state.enter_state()
        if self.HUD.cocks.ispressed:
            new_state = CockList(self.game, self.player)
            new_state.enter_state()
        if self.HUD.last_exp.ispressed:
            new_state = LastExp(self.game, self.player)
            new_state.enter_state()
        if self.HUD.inv.ispressed:
            new_state = Inventory(self.game, self.player)
            new_state.enter_state()
        mosanto_hover = self.mosanto_collide.collidepoint(pygame.mouse.get_pos())
        cave_hover = self.cave_collide.collidepoint(pygame.mouse.get_pos())
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and mosanto_hover:
                new_state = Monsanto(self.game, self.exp_chosen)
                new_state.enter_state()
            if event.type == pygame.MOUSEBUTTONDOWN and cave_hover:
                new_state = StateLevel(self.game, len(self.player.cocks), self.exp_chosen)
                new_state.enter_state()
                print("cave")
        if (self.exp_chosen):

            # DEBUG
            self.chosen_cocks = self.player.cocks
            # DEBUG
            if not self.wantNight:
                new_state = ExpState(self.game, self.exp_chosen[0], self.exp_chosen[1], self.chosen_cocks,
                                     self.player.last_exp)
                self.player.day += 1
                self.game.music_player.music.fadeout(1000)
                self.isMusicLoaded = False
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
        self.update_dn_cycle(surface)

    def update_dn_cycle(self, surface):
        if self.wantNight or self.wantDay:
            surface.blit(self.night_transition_background, (self.pos_trans_x, 0))
            self.pos_trans_x -= 30
        if self.wantNight:
            if self.pos_trans_x <= -50 and not self.isNight:
                self.background_img = self.background_img_night
                self.isNight = True
            if self.pos_trans_x <= -WIDTH * 2:
                self.wantNight = False
                self.pos_trans_x = WIDTH
        elif self.wantDay:
            if self.pos_trans_x <= -50 and self.isNight:
                self.background_img = self.background_img_day
                self.isNight = False
            if self.pos_trans_x <= -WIDTH * 2:
                self.wantDay = False
                self.pos_trans_x = WIDTH

    def bgm(self):
        self.game.music_player.music.load("Assets/Sounds/day_music.ogg")
        self.game.music_player.music.play(-1)


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
