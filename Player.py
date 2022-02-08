from unicodedata import name
import Expedition

class Player():
    def __init__(self,name):
        self.nom = name
        self.day = 1
        self.cock_list = []
        self.inv_grain = {"base_grain" : 100}
        self.inv_ore = {}
        self.inv_adn = {}
        self.money = 100
        self.relation_monsanto = 1

    def buy_cock(self, cock_name):
        pass

    def set_adn(self,name,quant):
        if name in self.inv_adn:
            self.inv_adn[name]+= quant
        else:
            self.inv_adn[name] = quant

    def set_ore(self,name,quant):
        if name in self.inv_ore:
            self.inv_ore[name]+= quant
        else:
            self.inv_ore[name] = quant

    def free_cock(self, cock_id):
        self.cock_list.remove(cock_id)

    def buy_grain(self, grain_name,quant,dic_grain):
        self.gold -= dic_grain[name].price * quant
        if grain_name in self.inv_grain:
            self.inv_ore[grain_name]+= quant
        else:
            self.inv_ore[grain_name] = quant

    def send_to_mine(self, level, strat, cock_list):
        # strat int 0= aucun 1=minerai 2=ADN
        # exped = Expedition(game,level,strat,cock_list)
        pass
