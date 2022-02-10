import pygame.image

from Expedition import Expedition
from Consts import *
import Utils
from State import State

class ExpState(State):
    def __init__(self, game, level, strat, cock_dic, summary):
        super().__init__(game)
        self.level = level
        self.strat = strat
        self.cock_dic = cock_dic
        self.Expedition = Expedition(level = self.level, strat = self.strat, cock_dic = self.cock_dic)
        self.background_img = pygame.image.load("Assets/map.png")
        self.s_case = pygame.image.load("Assets/case.png")
        self.s_rit = pygame.image.load("Assets/pentagramme.png")
        self.s_ore = pygame.image.load("Assets/minerais.png")
        self.s_dna = pygame.image.load("Assets/adn.png")
        self.s_gas = pygame.image.load("Assets/gaz.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.debug_grid = pygame.image.load("Assets/alpha_grid.png")
        self.grid = -1
        self.cases = []
        self.ongoing = True
        self.summary = summary

    def update(self, delta_time, actions):
        if(actions["esc"]):
            self.summary.clear()
            summ = self.Expedition.gen_summary()
            for key in summ:
                self.summary[key] = summ[key]
            self.prev_state.wantDay = True
            self.exit_state()
        if actions["right"]:
            self.grid *= -1
        self.game.reset_keys()
        if(self.ongoing):
            self.step()

    def render(self, surface):
        surface.blit(self.background_img, self.background_rect)
        counter = 0
        for event in self.cases:
            rows = int(counter/7)
            pos = (50+counter*135 - 945*rows, 150 + rows*135)
            surface.blit(self.s_case, pos)
            if event == "ores":
                surface.blit(self.s_ore, (pos))
            elif event == "dna":
                surface.blit(self.s_dna, (pos))
            elif event == "gas":
                surface.blit(self.s_gas, (pos))
            elif event == "ritual":
                surface.blit(self.s_rit, (pos))
            counter += 1

        if(self.grid > 0):
            surface.blit(self.debug_grid, (0, 0))

    def step(self):
        resultat = self.Expedition.avancement()
        if resultat != "done":
            self.cases.append(resultat)
        else:
            self.ongoing = 0
        


