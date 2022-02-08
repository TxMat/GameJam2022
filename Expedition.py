from pickle import NONE
import pygame
import random

class Expedition():
    def __init__(self,game,level = None):
        self.strat = 0
        self.level = level
        self.length =  random.randint(3, 10)
        self.layout = None
        self.game = game
        self.mid_w, self.mid_h = game.WIDTH /2, game.HEIGHT /2 
        self.run_display = True
        self.background_img = pygame.image.load("Assets/backgound_day.png")
        self.minerai = {}
        for ores in level.ores:
            self.minerai[ores]=0
        self.dna = {}
        for dnas in level.dna:
            self.dna[dnas]=0

    def blit_screen(self):
        self.game.screen.blit(self.game.display,(0, 0))
        pygame.display.update()

    def avancement(self):
        print("le donjon fait"+ str(self.length))
        for i in range(self.length):
            rand = random.randint(0,3)
            if  rand == 1:
                self.minerai[random.choice(list(self.minerai))] += EventOre(self.game,self).display()
            elif rand ==2:
                EventGaz(self.game,self).display()
            elif rand ==3:
                EventRituel(self.game,self).display()
            else:
                print("pas de minerai")
        

class EventOre():
    def __init__(self, game,expedition):
        self.game = game
        self.expedition = expedition


    def display(self):
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
        return random.randint(1,8)


class EventGaz():
    def __init__(self, game,expedition):
        self.game = game
        self.expedition = expedition


    def display(self):
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


    def display(self):
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