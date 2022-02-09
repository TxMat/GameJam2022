import pygame.image
import Utils
from State import State

class LastExp(State):
    def __init__(self, game, player):
        super().__init__(game)
        self.debug_grid = pygame.image.load("Assets/alpha_grid.png")
        self.background_img = pygame.image.load("Assets/menubg.png")
        self.background_rect = self.background_img.get_rect()
        self.background_rect.center = (self.game.WIDTH / 2, self.game.HEIGHT / 2)
        self.grid = 1
        self.player = player

    def update(self, delata_time, actions):
        if actions["left"]:
            print("bijour")
            self.exit_state()
        if actions["right"]:
            self.grid *= -1
        self.game.reset_keys()

    def render(self, surface):
        self.prev_state.render(surface)
        surface.fill((70,70,70,255), None, pygame.BLEND_RGBA_MULT)
        surface.blit(self.background_img, self.background_rect)
        self.game.draw_text(surface, "Resume de la derniere expedition :", 45, 512, 150)
        Utils.draw_line(surface, (250, 200), (750, 200), 2)
        if(len(self.player.last_exp) == 0):
            self.game.draw_text(surface, "Vous n'etes pas encore", 40, 512, 300)
            self.game.draw_text(surface, "parti en expedition !", 40, 512, 335)
        else:
            self.game.draw_text(surface, "Resultats :", 30, 250, 250)
        if(self.grid > 0):
            surface.blit(self.debug_grid, (0, 0))
        #surface.blit(self)
        
