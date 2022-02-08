from pickle import NONE
import pygame
import random


class Expedition():
    def __init__(self, game, level=None, cock_list={}, strat=0):
        self.strat = 0
        self.cock_list = cock_list
        self.level = level
        self.length = random.randint(3, 10)
        self.layout = None
        self.game = game
        self.mid_w, self.mid_h = game.WIDTH / 2, game.HEIGHT / 2
        self.run_display = True
        self.background_img = pygame.image.load("Assets/backgound_day.png")
        self.minerai = {}
        for ores in level.ores:
            self.minerai[ores] = 0
        self.dna = {}
        for dnas in level.dna:
            self.dna[dnas] = 0

    def blit_screen(self):
        self.game.screen.blit(self.game.display, (0, 0))
        pygame.display.update()

    def avancement(self):
        ore_luck = 0
        dna_luck = 0
        if self.strat == 1:  # minerai
            ore_luck = 2
        if self.strat == 2:  # dna
            dna_luck == 1
        print("le donjon fait " + str(self.length))
        for i in range(self.length):
            rand = random.randint(0, 9)
            if rand in [1, 3 + ore_luck]:
                self.minerai[random.choice(list(self.minerai))] += EventOre(self.game, self).display()
            elif rand in [8 - dna_luck, 8]:
                self.dna[random.choice(list(self.dna))] += EventDna(self.game, self).display()
            elif rand in [6, 7]:
                EventGaz(self.game, self).display()
            elif rand == 9:
                EventRituel(self.game, self).display()
            else:
                print("pas de minerai")


class EventOre():
    def __init__(self, game, expedition):
        self.game = game
        self.expedition = expedition

    def display(self):
        print("affiche event ore")
        self.run_display = True
        while self.run_display:
            background_img = pygame.image.load("Assets/background_cave.png")
            self.game.screen.blit(background_img, (0, 0))
            self.game.draw_text("ore Event", 80, self.game.WIDTH / 2, 70, self.game.WHITE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running, self.game.playing = False, False
                    self.run_display = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.run_display = False
        return random.randint(1, 8)


class EventGaz():
    def __init__(self, game, expedition):
        self.game = game
        self.expedition = expedition

    def display(self):
        print("affiche event gaz")
        self.run_display = True
        while self.run_display:
            background_img = pygame.image.load("Assets/background_cave.png")
            self.game.screen.blit(background_img, (0, 0))
            self.game.draw_text("gaz Event", 80, self.game.WIDTH / 2, 70, self.game.WHITE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running, self.game.playing = False, False
                    self.run_display = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.run_display = False


class EventDna():
    def __init__(self, game, expedition):
        self.game = game
        self.expedition = expedition

    def display(self):
        print("affiche event dna")
        self.run_display = True
        while self.run_display:
            background_img = pygame.image.load("Assets/background_cave.png")
            self.game.screen.blit(background_img, (0, 0))
            self.game.draw_text("dna Event", 80, self.game.WIDTH / 2, 70, self.game.WHITE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running, self.game.playing = False, False
                    self.run_display = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.run_display = False
        return random.randint(1, 2)


class EventRituel():
    def __init__(self, game, expedition):
        self.game = game
        self.expedition = expedition

    def display(self):
        print("affiche event rituel")
        r_list = ["Satanique", "Goy-ish", "Maudit"]
        random.choice(list(self.expedition.cock_list.values())).add_ritual(random.choice(r_list))
        self.run_display = True
        while self.run_display:
            background_img = pygame.image.load("Assets/background_cave.png")
            self.game.screen.blit(background_img, (0, 0))
            self.game.draw_text("rituel Event", 80, self.game.WIDTH / 2, 70, self.game.WHITE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running, self.game.playing = False, False
                    self.run_display = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.run_display = False
