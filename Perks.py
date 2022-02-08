from Cock import *

class Perks():
    def __init__(self,
                name: str ,
                icon = None,
                tier: int = 1,
                description: str = "",
                int_mod: int = 0,
                int_mult: float = 1,
                str_mod: int = 0,
                str_mult: float = 1,
                sta_mod: int = 0,
                sta_mult: float = 1):
        self.name = name
        self.ico = icon
        self.tier = tier
        self.desc = description
        self.int_mod = int_mod
        self.int_mult = int_mult
        self.str_mod = str_mod
        self.str_mult = str_mult
        self.sta_mod = sta_mod
        self.sta_mult = sta_mult

    def action(self, cock: Cock) -> None:
        #overridden by each perk
        pass
