from random import randint

class Level():
    def __init__(self,
                name: str,
                background_img = None,
                icon = None,
                ore_list: list = ["metal 1", "metal 2", "metal 3"],
                dna_list: list = ["adn 1", "adn 2", "adn 3"],
                encounters_list: list = ["rencontre 1", "rencontre 2", "rencontre 3", "rencontre 4", "rencontre 5"],
                description: str = "Rien a voir ici",
                danger_lvl: int = 1,
                length_range: tuple = (5,10),
                requirement: int = 0):
        self.name = name
        self.bg = background_img
        self.ico = icon
        self.ores = ore_list
        self.dnas = dna_list
        self.enc = encounters_list
        self.desc = description
        self.danger = danger_lvl
        self.len_range = length_range
        self.req = requirement

    def gen_len(self):
        return randint(self.len_range(0), self.len_range(1))
