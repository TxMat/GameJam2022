from pickle import NONE
import pygame
import random
import Level
import Events

class Expedition():
    def __init__(self,
                strat: int = 0,
                cock_dic: dict = {},
                level: Level = None,
                length: int = random.randint(3, 10),
                layout = None,
                game = None,
                background_img = pygame.image.load("Assets/backgound_day.png")) -> None:
        self.strat = strat
        self.cock_dic = cock_dic
        self.level = level
        self.length = length
        self.end = False
        self.layout = layout
        #self.game = game
        #self.mid_w, self.mid_h = game.WIDTH / 2, game.HEIGHT / 2
        #self.run_display = True
        #self.bg_img = background_img
        self.loot_ores = {}
        self.loot_dna = {}
        for ore in level.ores:
            self.loot_ores[ore] = 0
        self.dna = {}
        for dna in level.dnas:
            self.loot_dna[dna] = 0
    #legacy content
   # def blit_screen(self):
     #   self.game.screen.blit(self.game.display, (0, 0))
     #   pygame.display.update()

    def gen_summary(self):
        summary = {}
        summary['ores'] = self.loot_ores
        summary['dnas'] = self.loot_dnas
        summary['level'] = self.level.name
        summary['party'] = list(self.cock_dic.keys())
        return summary

    def get_party_stats(self):
        stats = {"strength":0, "intel":0, "stamina":0}
        for cock in cock_dic.values():
            stats["strength"] += cock.g_strength()
            stats["intel"] += cock.g_intel()
            stats["stamina"] += cock.g_stamina()
        return stats

    def stop(self): # stop l"expedition , retire les ressources si y a pas la perks
        save_ressources = False
        for cock in self.cock_dic:
            for perk in cock.perks:
                if perk == "1up":
                    save_ressources= True
        if not save_ressources:
            for ore in self.loot_ores:
                self.loot_ores[ore] = 0  
            for dna in self.loot_dna:
                self.loot_dna[dna] = 0
        self.end = True

    def avancement(self):

        ore_luck = 0
        dna_luck = 0
        if self.strat == 1:  # minerai
            ore_luck = 2
        if self.strat == 2:  # dna
            dna_luck == 1

        print("le donjon fait " + str(self.length))
        for i in range(self.length):
            print("case :"+ str(i))
            if self.end:
                break
            rand = random.randint(0, 9)
            if rand in [1, 3 + ore_luck]:
                print("minerais")
                Events.ore().action(self)
            elif rand in [8 - dna_luck, 8]:
                print("adn")
                Events.dna().action(self)
            elif rand in [6, 7]:
                print("gaz")
                random.choice(list(Events.gen_gas().values())).action(self)
            elif rand == 9:
                print("rituel")
                random.choice(list(Events.gen_rituals()).values()).action(random.choice(list(self.cock_list.values())))
            else:
                print("il se passe rien")

        print("minerais : " + str(self.loot_ores))
        print("adn : " + str(self.loot_dna))


'''
# legacy content
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
'''
