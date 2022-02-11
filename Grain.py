class Grain():
    def __init__(self,
                 name="",
                 price=0,
                 res_cost=0,
                 res_mat="",
                 hunger=1,
                 int_b=0,
                 sta_b=0,
                 str_b=0,
                 unlocked=False):
        self.name = name
        self.price = price
        self.res_cost = res_cost
        # self.res_mat = res_mat
        self.res_mat = name
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

def gen_grain():
    grain = {}
    grain["base"] = Grain("base", 5, 0, hunger=2, unlocked=True)
    grain["h1n1"] = Grain("h1n1", 10, 10, hunger=10, int_b=2, sta_b=2, str_b=2)
    grain["b5r3"] = Grain("b5r3", 200, 15, hunger=10, int_b=2, sta_b=54, str_b=2)
    grain["d1c3"] = Grain("d1c3", 500, 30, hunger=10, int_b=100, sta_b=0, str_b=0)
    grain["n1g8"] = Grain("n1g8", 800, 50, hunger=0, int_b=0, sta_b=40, str_b=0)
    grain["i8a5"] = Grain("i8a5", 1000, 60, hunger=10, int_b=5, sta_b=7, str_b=23)
    grain["z9g1"] = Grain("z9g1", 2000, 99, hunger=10, int_b=12, sta_b=22, str_b=100)
    grain["l5z5"] = Grain("l5z5", 3500, 120, hunger=10, int_b=13, sta_b=12, str_b=34)
    grain["b1t4"] = Grain("b1t4", 4500, 130, hunger=10, int_b=10, sta_b=31, str_b=40)
    grain["u8x1"] = Grain("u8x1", 4500, 500, hunger=10, int_b=53, sta_b=820, str_b=31)
    grain["y2w3"] = Grain("y2w3", 6000, 400, hunger=10, int_b=68, sta_b=15, str_b=35)
    grain["c0c5"] = Grain("c0c5", 6666, 300, hunger=10, int_b=15, sta_b=103, str_b=81)
    grain["e9y5"] = Grain("e9y5", 8000, 600, hunger=10, int_b=76, sta_b=97, str_b=46)
    grain["e8t1"] = Grain("e8t1", 10000, 9000, hunger=10, int_b=41, sta_b=35, str_b=301)
    grain["h8k3"] = Grain("h8k3", 12000, 1000, hunger=10, int_b=79, sta_b=75, str_b=67)
    grain["i2y4"] = Grain("i2y4", 18000, 1000, hunger=10, int_b=64, sta_b=79, str_b=97)
    return grain
