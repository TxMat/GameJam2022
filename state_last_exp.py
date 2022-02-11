import pygame.image

import Utils
from Button import Button
from State import State


class LastExp(State):
    def __init__(self, game, player, summary=None):
        super().__init__(game)
        if summary is None:
            summary = {'ores': [], 'dnas': [], 'level': [], 'party': []}
        self.debug_grid = pygame.image.load("Assets/alpha_grid.png")
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (self.game.WIDTH / 2, self.game.HEIGHT / 2)
        self.grid = -1
        self.player = player
        self.summary = self.player.last_exp
        self.close_btn = Button(self.game, 910, 90, "X")

    def update(self, delta_time, actions):
        self.close_btn.update(self.game.events)
        if actions["esc"] or self.close_btn.ispressed:
            self.exit_state()
        if actions["right"]:
            self.grid *= -1
        self.game.reset_keys()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.fill((70, 70, 70, 255), None, pygame.BLEND_RGBA_MULT)
        surface.blit(self.background_img, self.background_rect)
        self.game.draw_text(surface, "Resume de la derniere expedition :", 45, 512, 150)
        Utils.draw_line(surface, (225, 200), (775, 200), 2)
        if len(self.player.last_exp) == 0:
            self.game.draw_text(surface, "Vous n'etes pas encore", 40, 512, 300)
            self.game.draw_text(surface, "parti en expedition !", 40, 512, 335)
        else:
            # Niveau / dna / minerais / equipe
            Utils.draw_line(surface, (512, 300), (512, 550), 2)
            self.game.draw_text(surface, "Minerais :", 35, 225, 350, align="left")
            self.game.draw_text(surface, "Adn :", 35, 600, 350, align="left")
            self.game.draw_text(surface, self.summary["level"], 40, 512, 250)
            if len(self.summary['ores']) > 0:
                i = 0
                for name in self.summary['ores']:
                    self.game.draw_text(surface, name + " : " + str(self.summary['ores'][name]), 30, 225, 400 + i,
                                        align="left")
                    i += 50
            if len(self.summary['dnas']) > 0:
                i = 0
                for name in self.summary['dnas']:
                    self.game.draw_text(surface, name + " : " + str(self.summary['dnas'][name]), 30, 600, 400 + i,
                                        align="left")
                    i += 50
        self.close_btn.render(surface)
