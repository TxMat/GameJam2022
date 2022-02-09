import pygame.image
import Utils
from State import State


class LastExp(State):
    def __init__(self, game, player, summary = {'ores':[], 'dnas':[], 'level':[], 'party':[]}):
        super().__init__(game)
        self.debug_grid = pygame.image.load("Assets/alpha_grid.png")
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (self.game.WIDTH / 2, self.game.HEIGHT / 2)
        self.grid = -1
        self.player = player
        self.summary = summary

    def update(self, delata_time, actions):
        if actions["esc"]:
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
            Utils.draw_line(surface, (512,300), (512,550), 2)
            self.game.draw_text(surface, "Minerais :", 35, 225, 350, align="left")
            self.game.draw_text(surface, "Adn :", 35, 600, 350, align="left")


            # DEBUG
            """self.summary = {"ores":{"alu":5,
                                    "fer":6,
                                    "ardite":5648
                                    },
                            "dnas":{"h1n1":8,
                                    "h3q4":10,
                                    "g2z3":16426,
                                    },
                            "level":"le niveau ouais ouais",
                            "party":["michel", "mahmud", "herve", "emmanuel"]
                            }"""
            # DEBUG

            self.game.draw_text(surface, self.summary["level"], 40, 512, 250)
            if(len(self.summary['ores']) > 0):
                i = 0
                for name in self.summary['ores']:
                    self.game.draw_text(surface, name + " : " + str(self.summary['ores'][name]), 30, 225, 400 + i, align="left")
                    i += 50
            if(len(self.summary['dnas']) > 0):
                i = 0
                for name in self.summary['dnas']:
                    self.game.draw_text(surface, name + " : " + str(self.summary['dnas'][name]), 30, 600, 400 + i, align="left")
                    i += 50
            cock_names = "   ".join([name for name in self.summary["party"]] )
            self.game.draw_text(surface, cock_names, 40, 512, 625)
        if(self.grid > 0):
            surface.blit(self.debug_grid, (0, 0))
        # surface.blit(self)
