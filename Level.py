from random import randint


class Level():
    def __init__(self,
                 name: str = "",
                 background_img=None,
                 icon=None,
                 ore_list: list = ["metal 1", "metal 2", "metal 3"],
                 dna_list: list = ["adn 1", "adn 2", "adn 3"],
                 encounters_list: list = ["rencontre 1", "rencontre 2", "rencontre 3", "rencontre 4", "rencontre 5"],
                 description: str = "Rien a voir ici",
                 danger_lvl: int = 1,
                 length_range: tuple = (5, 10),
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


def gen_level():
    level = {}
    level["mine d'argent"] = Level(name="mine d'argent", ore_list=["cuivre", "argent", "emeraude"],
                                   dna_list=["h1n1", "b5r3", "d1c3"],
                                   description="Une mine d'argent, rien de plus... rien de moins", danger_lvl=1,
                                   length_range=(3, 8))
    level["mine dangereuse"] = Level(name="mine dangereuse", ore_list=["columbite", "granit", "saphir"],
                                     dna_list=["n1g8", "i8a5", "z9g1"], description="Une mine pleine de ressources",
                                     danger_lvl=3, length_range=(3, 15))
    level["mine d'or"] = Level(name="mine d'or", ore_list=["cuivre", "or", "emeraude"],
                               dna_list=["l5z5", "b1t4", "u8x1"],
                               description="Surement une des plus vielle que la terre ait portee", danger_lvl=2,
                               length_range=(10, 15))
    level["mine de diamant"] = Level(name="mine de diamant", ore_list=["fer", "platine", "plomb"],
                                     dna_list=["y2w3", "c0c5", "e9y5"], description="Elle brille meme de l'exterieur",
                                     danger_lvl=13, length_range=(3, 15))
    level["mine de l'extreme"] = Level(name="mine de l'extreme", ore_list=["rubis", "diamant", "francium"],
                                       dna_list=["e8t1", "h8k3", "i2y4"], description="Vous etes sur de vouloir renter ?",
                                       danger_lvl=67, length_range=(3, 15))
    return level
