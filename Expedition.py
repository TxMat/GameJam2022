import pygame
import random

class Expedition():
    def __init__(self,game):
        self.strat = 0
        self.map_name = ""
        self.length =  random.randint(1, 8)
        self.layout = None
        self.game = game
        self.mid_w, self.mid_h = self.game.WIDTH /2, self.game.HEIGHT /2 
        self.run_display = True

    def blit_screen(self):
        self.game.window.blit(self.game.display,(0, 0))
        pygame.display.update()

class EventOre(Expedition):
    def __init__(self, game):
        Expedition.__init__(self,game)


    def Display_ore(self):
        print("affiche event ore")
        self.run_display = True
        while self.run_display:
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("ore event",20,self.mid_w,self.mid_h)
            self.blit_screen()


class EventGaz(Expedition):
    def __init__(self, game):
        Expedition.__init__(self,game)


    def Display_Gaz(self):
        print("affiche event gaz")
        self.run_display = True
        while self.run_display:
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("gaz event",20,self.mid_w,self.mid_h)
            self.blit_screen()


class EventRituel(Expedition):
    def __init__(self, game):
        Expedition.__init__(self,game)


    def Display_rituel(self):
        print("affiche event rituel")
        self.run_display = True
        while self.run_display:
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("rituel event",20,self.mid_w,self.mid_h)
            self.blit_screen()

