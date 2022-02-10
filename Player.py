from unicodedata import name
import Expedition
from Cock import Cock
from Consts import *


class Player():
    def __init__(self,
                 name="",
                 day=1,
                 cock_dict={},
                 inventory_grain={"base": 100},
                 inventory_ore={"metal 1": 50, "metal 2": 75, "metal 3": 100},
                 inventory_dna={"adn 1": 33, "adn 2": 66, "adn 3": 99},
                 money=100,
                 relation_monsanto=1,
                 last_exp = {},
                 cock_id = 0):
        self.name = name
        self.day = day
        self.cocks = cock_dict
        self.inv_grain = inventory_grain
        self.inv_ore = inventory_ore
        self.inv_dna = inventory_dna
        self.money = money
        self.rel = relation_monsanto
        self.last_exp = last_exp
        self.cock_id = cock_id

    def buy_cock(self, id, cock_name):
        if len(cock_name) == 0:
            cock_name = "Coq sans nom"
        if self.money < 50:
            print("Not enough money")
            return 1
        if len(self.cocks) == MAX_COCKS:
            print("Too many cocks")
            return 2
        self.money -= 50
        self.cocks[id] = Cock(self, id, cock_name)
        self.cock_id += 1
        return 0

    def set_adn(self, name, quant):
        if name in self.inv_adn:
            self.inv_adn[name] += quant
        else:
            self.inv_adn[name] = quant

    def set_ore(self, name, quant):
        if name in self.inv_ore:
            self.inv_ore[name] += quant
        else:
            self.inv_ore[name] = quant

    def free_cock(self, cock_id):
        self.cocks.pop(cock_id)

    def buy_grain(self, grain_name, quant, dic_grain):
        grain = dic_grain[grain_name]
        if (self.money < grain.price * quant):
            print("Not enough money")
            return 1
        self.gold -= grain.price * quant
        if grain_name in self.inv_grain:
            self.inv_ore[grain_name] += quant
        else:
            self.inv_ore[grain_name] = quant
        return 0

    def send_to_mine(self, level, strat, cock_dic):
        # strat int 0= aucun 1=minerai 2=ADN
        # exped = Expedition(game,level,strat,cock_list)
        length = level.gen_len
        return Expedition.Expedition(strat=strat, level=level, cock_dic=cock_dic, length=length)

