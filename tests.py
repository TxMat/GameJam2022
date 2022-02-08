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

print("TODO: \n\
    dummy grain\n\
    dummy events\n\
    dummy perks\n\
    dummy levels\n\
    dummy player\n\
    dummy tree\n\
    dummy expedition")

