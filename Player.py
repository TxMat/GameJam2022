class Player():
    def __init__(self):
        self.nom = ""
        self.day = 1
        self.cock_list = []
        self.inv_grain = {"base_grain" : 100}
        self.inv_ore = {}
        self.inv_adn = {}
        self.money = 100
        self.relation_monsanto = 1

    def buy_cock(self, cock_name):
        pass

    def free_cock(self, cock_name):
        pass

    def buy_grain(self, grain_name):
        pass

    def send_to_mine(self, map_name, strat, cock_list):
        pass
