import random

import pygame

import Events
import Level


class Expedition():
    def __init__(self,
                 strat: int = 0,
                 cock_dic: dict = {},
                 level: Level = None,
                 length: int = random.randint(3, 10),
                 layout=None,
                 game=None,
                 background_img=pygame.image.load("Assets/backgound_day.png")) -> None:
        self.cock_dic = cock_dic
        self.level = level
        self.length = length
        self.end = False
        self.layout = layout
        self.pos = 0
        # self.game = game
        # self.mid_w, self.mid_h = game.WIDTH / 2, game.HEIGHT / 2
        # self.run_display = True
        # self.bg_img = background_img
        self.loot_ores = {}
        self.loot_dna = {}
        self.ore_luck = 0
        self.dna_luck = 0
        for ore in level.ores:
            self.loot_ores[ore] = 0
        self.dna = {}
        for dna in level.dnas:
            self.loot_dna[dna] = 0
        if strat == 1:  # minerai
            self.ore_luck = 2
        elif strat == 2:  # dna
            self.dna_luck == 1
        print("Taille donjon : " + str(self.length))

    def gen_summary(self):
        summary = {}
        print(self.level.name)
        summary['ores'] = self.loot_ores
        summary['dnas'] = self.loot_dna
        summary['level'] = self.level.name
        summary['party'] = list(self.cock_dic.keys())
        return summary

    def get_party_stats(self):
        stats = {"strength": 0, "intel": 0, "stamina": 0}
        for cock in cock_dic.values():
            stats["strength"] += cock.g_strength()
            stats["intel"] += cock.g_intel()
            stats["stamina"] += cock.g_stamina()
        return stats

    def stop(self):  # stop l"expedition , retire les ressources si y a pas la perks
        save_ressources = False
        for cock in self.cock_dic.values():
            for perk in cock.perks:
                if perk == "1up":
                    save_ressources = True
        if not save_ressources:
            for ore in self.loot_ores:
                self.loot_ores[ore] = 0
            for dna in self.loot_dna:
                self.loot_dna[dna] = 0
        self.end = True

    def hunger_cost(self, cost):
        for cock in self.cock_dic.values():
            if cock.hunger <= 0:
                self.end = 1
            else:
                cock.hunger -= cost
            cock.target_health = cock.hunger * 10

    def avancement(self):
        if self.pos < self.length and not self.end:
            print("case : " + str(self.pos))
            self.pos += 1
            rand = random.randint(0, 99)
            print(rand)
            if rand in range(0, 30 + self.ore_luck * 10):
                self.hunger_cost(4)
                print("minerais")
                print(Events.ore().action(self))
                return "ores"
            elif rand in range(70 - self.dna_luck * 10, 93):
                self.hunger_cost(4)
                print("adn")
                print(Events.dna().action(self))
                return "dna"
            elif rand in range(60, 65):
                self.hunger_cost(8)
                print("gaz")
                print(random.choice(list(Events.gen_gas().values())).action(self))
                return "gas"
            elif rand in range(94, 99):
                self.hunger_cost(8)
                print("rituel")
                if (self.cock_dic):  # DEBUG
                    print(random.choice(list(Events.gen_rituals().values())).action(
                        random.choice(list(self.cock_dic.values()))))
                return "ritual"
            else:
                self.hunger_cost(1)
                print("il se passe rien")
                return "none"
        else:
            print("minerais : " + str(self.loot_ores))
            print("adn : " + str(self.loot_dna))
            return "done"


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
