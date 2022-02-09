class Grain():
    def __init__(self,
            name = "",
            price = 0,
            res_cost = 0,
            res_mat = "",
            hunger = 1,
            int_b = 0,
            sta_b = 0,
            str_b = 0,
            unlocked = False):
        self.name = name
        self.price = price
        self.res_cost = res_cost
        self.res_mat = res_mat
        self.hunger = hunger
        self.int_bonus = int_b
        self.sta_bonus = sta_b
        self.str_bonus = str_b
        self.is_unlocked = unlocked

    def grain_info(self):
            print("name: " + self.name)
            print("price: " + str(self.price))
            print("r_cost: " + str(self.res_cost))
            print("r_mat: " + self.res_mat)
            print("hunger: " + str(self.hunger))
            print("int bonus: " + str(self.int_bonus))
            print("sta bonus: " + str(self.sta_bonus))
            print("str bonus: " + str(self.str_bonus))
            print("unlocked : " + str(self.is_unlocked))

from random import randint, choice

def debug_grain(nb = 1) -> [Grain]:
    grains = []
    for i in range(nb):
        grains.append(Grain("Grain " + str(i+1), randint(100, 5000), randint(1, 50), "ADN " + str(randint(1, 10)), randint(1,5), randint(1,5), randint(1,5), randint(1,5), choice((True, False))))
        grains[i].grain_info()
        print("")
    return grains
