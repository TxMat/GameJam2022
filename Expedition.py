import pygame
import random

class Expedition():
    def __init__(self,game):
        self.strat = 0
        self.map_name = ""
        self.length =  random.randint(1, 8)
        self.layout = None
        self.game = game
        self.mid_w, self.mid_h = game.WIDTH /2, game.HEIGHT /2 
        self.run_display = True
        self.background_img = pygame.image.load("Assets/backgound_day.png")

    def blit_screen(self):
        self.game.screen.blit(self.game.display,(0, 0))
        pygame.display.update()

    def avancement(self):
        for i in range(self.length):
            rand = random.randint(0,3)
            if  rand == 1:
                EventOre(self.game,self).Display_ore()
            elif rand ==2:
                EventGaz(self.game,self).Display_gaz()
            elif rand ==3:
                EventRituel(self.game,self).Display_rituel()
            else:
                print("pas de minerai")
        


class EventOre():
    def __init__(self, game,expedition):
        self.game = game
        self.expedition = expedition


    def Display_ore(self):
        print("affiche event ore")
        self.run_display = True
        while self.run_display:
            background_img = pygame.image.load("Assets/background_cave.png")
            self.game.screen.blit(background_img, (0, 0))
            self.game.draw_text("ore Event",80,self.game.WIDTH/2,70,self.game.WHITE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running, self.game.playing = False, False
                    self.run_display = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.run_display = False


class EventGaz():
    def __init__(self, game,expedition):
        self.game = game
        self.expedition = expedition


    def Display_gaz(self):
        print("affiche event gaz")
        self.run_display = True
        while self.run_display:
            background_img = pygame.image.load("Assets/background_cave.png")
            self.game.screen.blit(background_img, (0, 0))
            self.game.draw_text("gaz Event",80,self.game.WIDTH/2,70,self.game.WHITE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running, self.game.playing = False, False
                    self.run_display = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.run_display = False


class EventRituel():
    def __init__(self, game,expedition):
        self.game = game
        self.expedition = expedition


    def Display_rituel(self):
        print("affiche event rituel")
        self.run_display = True
        while self.run_display:
            background_img = pygame.image.load("Assets/background_cave.png")
            self.game.screen.blit(background_img, (0, 0))
            self.game.draw_text("rituel Event",80,self.game.WIDTH/2,70,self.game.WHITE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running, self.game.playing = False, False
                    self.run_display = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.run_display = False