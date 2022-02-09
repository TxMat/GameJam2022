from Cock import *
from Events import *
from Expedition import *
from Farm import *
from Game import *
from Grain import *
from Level import *
from Perks import *
from Player import *
from Tree import *

def test_cock():
    print("Creation coq 1\n")
    cock_a = Cock(1,"coq 1")
    print("Infos coq 1\n")
    cock_a.info_cock()
    print("")
    print("Ponte coq 2 par coq 1\n")
    cock_b = cock_a.lay_egg(2,"coq 2")
    print("Fertilité coq 1: " + str(cock_a.fertile))
    print("Id enfant coq 1: " + str(cock_a.child))
    print("Infos coq 2\n")
    cock_b.info_cock()
    return (cock_a, cock_b)

def test_grain():
    grains = debug_grain(5) 
    return grains

def test_perk():
    class PerkFireproof(Perks):
        def __init__(self,
            name: str ,
            icon = None,
            tier: int = 1,
            description: str = "",
            int_mod: int = 0,
            int_mult: float = 1,
            str_mod: int = 5,
            str_mult: float = 5000,
            sta_mod: int = 0,
            sta_mult: float = 1):
            super().__init__(name, icon, tier, description, int_mod, int_mult, str_mod, str_mult, sta_mod, sta_mult)    

    def action(self, cock: Cock) -> None:
        #doesn't work
        cock.strength += 50000
    fireproof = PerkFireproof("fireproof")
    perks = [fireproof]
    for i in range(2,15):
        perks.append(Perks("Perk " + str(i), None, 0, "", randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50)))
    perks[1].tier = 2
    perks[2].tier = 2
    perks[3].tier = 2
    perks[4].tier = 3
    perks[5].tier = 3
    perks[6].tier = 3
    perks[7].tier = 4
    perks[8].tier = 4
    perks[9].tier = 4
    perks[10].tier = 4
    perks[11].tier = 4
    perks[12].tier = 5
    perks[13].tier = 5
    return perks

a = test_cock()
b = test_grain()
c = test_perk()
#a[0].add_perk("fireproof",{"fireproof":c[0]})

print("TODO: \n\
    dummy events\n\
    dummy perks\n\
    dummy levels\n\
    dummy player\n\
    dummy tree\n\
    dummy expedition")

